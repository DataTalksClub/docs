---
title: "08. Baseline Model"
parent: "Module 02: Regression"
nav_order: 8
---


# Building a Baseline Car Price Model

<iframe width="560" height="315" src="https://www.youtube.com/embed/SvPpMMYtYbU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

In this lesson we turn the math and plumbing from the previous sessions into a **baseline model** for predicting car prices. The goal is not “best possible performance” yet—it’s a clean, minimal pipeline that runs end-to-end, so we can (a) verify our data path and (b) establish a benchmark to improve later.

We’ll:

1. select a small set of **numeric features**,
2. handle **missing values** pragmatically,
3. train **linear regression** (on the log-transformed target), and
4. make a quick **in-sample sanity check** of predictions—then tee up proper evaluation with RMSE next.

---

## 1) Pick a minimal feature set

For a baseline, we’ll restrict ourselves to straightforward numeric columns. From the dataframe, we’ll use:

* `engine_hp` (engine horsepower)
* `engine_cylinders`
* `highway_mpg`
* `city_mpg`
* `popularity`

These are easy to feed to a linear model and already numeric after our earlier cleaning.

```python
numeric_cols = [
    "engine_hp",
    "engine_cylinders",
    "highway_mpg",
    "city_mpg",
    "popularity",
]

df_train_base = df_train[numeric_cols].copy()
df_val_base   = df_val[numeric_cols].copy()
df_test_base  = df_test[numeric_cols].copy()
```

---

## 2) Handle missing values (simple, explicit)

You will likely see `NaN` in `engine_hp` and `engine_cylinders`. A **baseline** approach is to fill missing values with **0** and move on. It’s not semantically perfect (no car has “0 cylinders”), but it’s fast and often adequate for a first pass.

> Why 0 can be “OK enough” here: with linear regression, a 0 in a feature effectively **removes** its contribution for that row. You’re telling the model “ignore this feature for this sample.” We’ll revisit better imputation later (median/mean, model-based, or adding a missingness indicator).

```python
for part in (df_train_base, df_val_base, df_test_base):
    part.fillna(0, inplace=True)
```

Double-check:

```python
df_train_base.isna().sum()
```

Everything should be zero.

---

## 3) Build X and y (remember: y is log1p(msrp))

We prepared our targets earlier as `y_* = log1p(msrp)`. Keep using those for stability with skewed price distributions.

```python
X_train = df_train_base.values  # (m_train, 5)
X_val   = df_val_base.values    # (m_val, 5)
X_test  = df_test_base.values   # (m_test, 5)

# Already computed earlier when we split and transformed:
# y_train = np.log1p(original_train_msrp)
# y_val   = np.log1p(original_val_msrp)
# y_test  = np.log1p(original_test_msrp)
```

---

## 4) Train linear regression (normal equation)

We’ll reuse a minimal trainer from the previous lesson that adds the bias column and solves the normal equation.

```python
import numpy as np

def add_bias_column(X):
    m = X.shape[0]
    return np.hstack([np.ones((m, 1)), X])

def train_linear_regression_normal(X, y):
    X_aug = add_bias_column(X)
    XtX   = X_aug.T @ X_aug
    Xty   = X_aug.T @ y
    w_aug = np.linalg.solve(XtX, Xty)  # robust enough for baseline; see notes below
    w0, w = w_aug[0], w_aug[1:]
    return w0, w

w0, w = train_linear_regression_normal(X_train, y_train)
```

> If `np.linalg.solve` complains about singularity (high collinearity), switch to a more robust solver for a baseline:
>
> ```python
> w_aug = np.linalg.lstsq(add_bias_column(X_train), y_train, rcond=None)[0]
> w0, w = w_aug[0], w_aug[1:]
> ```

---

## 5) In-sample predictions (sanity check, not evaluation)

Make predictions on the **training** data to check for obvious pathologies (e.g., completely flat predictions, dtype mistakes, etc.).

```python
def predict_linear(X, w0, w):
    return w0 + X @ w  # still in log space

y_train_pred_log = predict_linear(X_train, w0, w)
```

A quick overlay of the **training target** vs **training predictions** (both in log space) can reveal gross mismatches:

```python
import matplotlib.pyplot as plt

plt.hist(y_train_pred_log, bins=50, alpha=0.6, label="pred (log)")
plt.hist(y_train,          bins=50, alpha=0.6, label="true (log)")
plt.legend(); plt.title("In-sample check (log space)"); plt.show()
```

What you may observe for this simple baseline:

* The **peak positions** of predicted vs true distributions don’t align perfectly.
* Predictions can be **shifted lower** (systematic underestimation), reflecting that the feature set is small and we haven’t used categorical signals (e.g., `make`, `model`) or better imputations yet.

This is fine—remember: it’s a **baseline**.

---

## 6) Why we don’t trust this chart for performance

An in-sample histogram is only a **sanity check**. It says nothing about **generalization**. For real assessment we’ll compute **RMSE** on the **validation** split, not the training set, and we’ll be explicit about the space:

* **Log space RMSE**: compare `y_val` to `y_val_pred_log` (model outputs).
* **Dollar RMSE**: compare `expm1(y_val)` to `expm1(y_val_pred_log)`.

We’ll formalize this in the next lesson.

---

## 7) Baseline takeaway and next steps

What we now have:

* A **minimal numeric-only feature set**
* A **simple missingness strategy** (zeros)
* A **trained linear model** with intercept
* An **in-sample sanity check** confirming the pipeline behaves as expected

What’s next:

* Introduce **RMSE** and evaluate on the **validation** set.
* Iterate: try **median imputation**, add **categorical encodings** (one-hot for `make`, `model`, `transmission_type`, etc.), and compare RMSE to this baseline.
* Add **regularization** (Ridge) to stabilize weights when we expand features.

This is the benchmark we’ll try to beat.
