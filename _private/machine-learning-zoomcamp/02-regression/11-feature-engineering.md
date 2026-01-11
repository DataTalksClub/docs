---
title: "11. Feature Engineering"
parent: "Module 2: Machine Learning for Regression"
nav_order: 11
---


# Adding Car Age to Improve the Baseline

<iframe width="560" height="315" src="https://www.youtube.com/embed/-aEShw4ftB0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


**Goal:** enrich our baseline numeric-only model by adding a simple but high-signal feature: **car age**. We’ll (1) motivate *age vs. year*, (2) compute age safely, (3) integrate it into a reusable `prepare_X` function without mutating inputs, and (4) retrain/evaluate on the validation split. You’ll see that a single, well-chosen transformation can materially reduce error.

---

## Why use **age** instead of **year**?

Modeling with `year` encodes a direction (“larger number = newer”), but linear models respond more naturally to a quantity that grows with depreciation: **age = current\_year − year**. Age tends to correlate *linearly* with log-price for much of the range (with exceptions for classics), which makes it a strong baseline signal.

* Newer car → **smaller age** → typically **higher** price.
* Older car → **larger age** → typically **lower** price.

In our dataset, assume data were collected in **2017**, so we’ll use `reference_year = 2017`.

---

## Implementation details (and pitfalls to avoid)

* Compute `age = reference_year - year`.
* Clamp negative ages (future model years) to **0**.
* Don’t mutate the caller’s dataframe inside `prepare_X`; make a **copy**.
* Keep the exact **same transformation** for train/val/test to avoid leakage or drift.

---

## Updated feature prep: add `age`

We’ll extend our baseline numeric features:

```python
NUMERIC_COLS = [
    "engine_hp",
    "engine_cylinders",
    "highway_mpg",
    "city_mpg",
    "popularity",
]
```

…and add `age`:

```python
import numpy as np

REFERENCE_YEAR = 2017  # from dataset context; parameterize if needed

def prepare_X(df, reference_year=REFERENCE_YEAR):
    """
    Build the design matrix X with baseline numeric features + computed 'age'.
    Does not mutate the input dataframe.
    """
    d = df.copy()  # avoid side effects

    # Compute age and clamp to [0, ∞)
    d["age"] = np.maximum(0, reference_year - d["year"])

    # Select features (baseline + age)
    features = NUMERIC_COLS + ["age"]
    d = d[features].copy()

    # Baseline imputation: fill numerics with 0
    # (Simple but consistent across splits; we can improve later.)
    d.fillna(0, inplace=True)

    return d.values  # (m, n_features)
```

> Sanity check: With `age` included, your feature count should increase from **5** to **6**.

---

## Train on train, evaluate on validation

(Using the linear-regression code from earlier lessons.)

```python
def add_bias_column(X):
    m = X.shape[0]
    return np.hstack([np.ones((m, 1)), X])

def train_linear_regression_normal(X, y):
    X_aug = add_bias_column(X)
    XtX   = X_aug.T @ X_aug
    Xty   = X_aug.T @ y
    # If singular, switch to np.linalg.lstsq or add ridge.
    w_aug = np.linalg.solve(XtX, Xty)
    w0, w = w_aug[0], w_aug[1:]
    return w0, w

def predict_linear(X, w0, w):
    return w0 + X @ w

def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_pred - y_true) ** 2))

# Build matrices
X_train = prepare_X(df_train)
X_val   = prepare_X(df_val)

# y_* are in log space: y = log1p(msrp)
w0, w = train_linear_regression_normal(X_train, y_train)

# Validate
y_val_pred_log = predict_linear(X_val, w0, w)
val_rmse_log   = rmse(y_val, y_val_pred_log)

# (Optional) report in dollars
y_val_pred = np.expm1(y_val_pred_log)
y_val_true = np.expm1(y_val)
val_rmse_$ = rmse(y_val_true, y_val_pred)

print("Validation RMSE (log):", val_rmse_log)
print("Validation RMSE ($):  ", val_rmse_$)
```

**What to expect:** In practice, adding `age` often yields a clear improvement. In the walkthrough, validation RMSE (log) dropped from roughly **0.76 → 0.51**—a large gain for a single engineered feature. Your exact numbers will vary by split and cleaning, but directionally this is common.

---

## Quick visual: predictions vs. truth (validation)

A simple overlay helps confirm we’re moving in the right direction:

```python
import matplotlib.pyplot as plt

plt.hist(y_val_pred_log, bins=50, alpha=0.6, label="pred (log)")
plt.hist(y_val,          bins=50, alpha=0.6, label="true (log)")
plt.legend(); plt.title("Validation — log targets vs. predictions");
plt.show()
```

You should see the **peaks align better** versus the numeric-only baseline. There will still be regions where the model underfits (e.g., extreme tails). That’s expected at this stage.

---

## Notes & extensions

* **Parameterize `reference_year`:** if you’re unsure, use the dataset’s collection year or `df["year"].max()` (but fix it based on **train** to avoid peeking).
* **Nonlinearity:** price-age relationships aren’t perfectly linear. Later, try **piecewise** or **polynomial** terms (e.g., `age`, `age^2`) and regularize.
* **Imputation:** replace the 0-fill with **train medians** and add **missingness indicators** (e.g., `is_engine_hp_missing`).
* **Regularization:** when you expand features, switch to **Ridge** to stabilize weights.

---

## Where we are, what’s next

We upgraded our baseline with a single, information-dense feature while keeping the pipeline clean and reproducible:

* `prepare_X` **does not mutate** inputs,
* consistent transforms across **train/val/test**,
* measurable improvement in **validation RMSE**.

Next up: incorporate **categorical variables** (e.g., `make`, `model`, `transmission_type`) via one-hot encoding and validate the gains.
