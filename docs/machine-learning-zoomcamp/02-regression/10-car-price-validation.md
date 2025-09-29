---
title: "10. Validating an ML Model"
parent: "Module 02: Regression"
nav_order: 10
---

# Validating a Machine Learning Model with a Proper Validation Set (Lesson 10)

<iframe width="560" height="315" src="https://www.youtube.com/embed/rawGPXg2ofE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

In this lesson we stop “peeking” at training performance and **evaluate the model the right way**—on a **separate validation split**. We’ll factor our feature prep into a reusable function, retrain on the training split, and report **RMSE** on the validation split. From here on, this will be the pattern for every improvement.

---

## Why validation (not training) error?

Training error almost always looks optimistic because the model has already “seen” those rows. To estimate **generalization**, we:

1. **Train** on `df_train`.
2. **Validate** on `df_val` (never used during training).
3. Keep `df_test` untouched until the very end.

---

## Step 1 — A reusable feature-prep function

Two lessons ago we hardcoded our feature prep inline. Let’s encapsulate it so we can apply **the same transformation** to train/val/test without drift.

```python
import numpy as np

NUMERIC_COLS = [
    "engine_hp",
    "engine_cylinders",
    "highway_mpg",
    "city_mpg",
    "popularity",
]

def prepare_X(df):
    """
    Select baseline numeric features and make a clean design matrix X.
    Applies the *same* steps for train/val/test to avoid leakage or drift.
    """
    df_num = df[NUMERIC_COLS].copy()
    df_num.fillna(0, inplace=True)           # baseline imputation
    return df_num.values                     # (m, n)
```

Key idea: **one function, one definition of “X.”** No silent differences between splits.

---

## Step 2 — Training: normal equation (as before)

We’ll reuse the minimal trainer that adds a bias column and solves the normal equations. (Any equivalent solver—`lstsq`, `pinv`—is fine.)

```python
def add_bias_column(X):
    m = X.shape[0]
    return np.hstack([np.ones((m, 1)), X])

def train_linear_regression_normal(X, y):
    X_aug = add_bias_column(X)
    XtX   = X_aug.T @ X_aug
    Xty   = X_aug.T @ y
    w_aug = np.linalg.solve(XtX, Xty)   # switch to lstsq/pinv if singular
    w0, w = w_aug[0], w_aug[1:]
    return w0, w

def predict_linear(X, w0, w):
    return w0 + X @ w                    # predictions in *log* space
```

---

## Step 3 — Metric: RMSE (unchanged)

```python
def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_pred - y_true) ** 2))
```

Remember: our targets are **log-transformed** (`y = log1p(msrp)`), so predictions are in log space too. You may compute RMSE in log space or invert both with `expm1` and compute **dollar RMSE**—just be consistent.

---

## Step 4 — Train on train, evaluate on validation

```python
# Build design matrices
X_train = prepare_X(df_train)
X_val   = prepare_X(df_val)

# y_* were created earlier as log1p(msrp)
w0, w = train_linear_regression_normal(X_train, y_train)

# Predict on *validation*
y_val_pred_log = predict_linear(X_val, w0, w)

# RMSE in log space
val_rmse_log = rmse(y_val, y_val_pred_log)

# (Optional) RMSE in dollars
y_val_pred = np.expm1(y_val_pred_log)
y_val_true = np.expm1(y_val)
val_rmse_dollars = rmse(y_val_true, y_val_pred)

print("Validation RMSE (log):", val_rmse_log)
print("Validation RMSE ($):  ", val_rmse_dollars)
```

Now you have a **single number** that reflects generalization quality for this baseline.

---

## Common pitfalls (avoid these)

* **Different prep between splits.** Always call the same `prepare_X` for train/val/test.
* **Using training rows for RMSE.** Only compute the reported metric on **validation** (test only once at the very end).
* **Mixing spaces.** Don’t compare log predictions to dollar targets (or vice versa). Either both log or both dollars.
* **Data leakage.** Never compute imputations/statistics on the full dataset. (For this baseline we used a fixed value—0—so no fit-time statistics were leaked. When you switch to mean/median, compute them on **train** and apply to val/test.)

---

## Quick checklist

* [x] Split: train / val / (test later)
* [x] Single source of truth for feature prep: `prepare_X`
* [x] Train on train only
* [x] Predict on val only
* [x] Report RMSE (log and/or \$), clearly labeled

---

## What’s next

With a trustworthy **validation RMSE**, we can begin **improving the model** and keeping only changes that **lower** that number:

* Better imputation (e.g., train median + missing-indicator features).
* Add **categorical features** (one-hot for `make`, `model`, `transmission_type`, etc.).
* **Regularization** (Ridge) to stabilize weights as feature space grows.

Each change → retrain on train → recompute **validation RMSE** with the **same** `prepare_X` logic. Keep the improvement if the metric moves in the right direction.
