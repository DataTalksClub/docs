---
title: "7. Training the Model (Normal Equation)"
parent: "Module 2: Machine Learning for Regression"
nav_order: 7
---

# Training the Model (Normal Equation)

<iframe width="560" height="315" src="https://www.youtube.com/embed/hx6nak-Y11g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

In the last lesson we learned how to **apply** a linear model once the weights are known. Today we answer the question: **how do we find those weights** from data?

We’ll start from the model in vector/matrix form, explain why the “naïve inverse” doesn’t work, derive the **normal equation**, handle the **bias (intercept)** correctly, and implement a clean NumPy training routine. We’ll finish with practical notes on stability and what to do when things go wrong.

---

## 1) Recap and objective

Our model predicts the target (here, `log1p(msrp)`) with a linear function of features:

$$
\hat{\mathbf{y}} \;=\; \mathbf{X}\,\tilde{\mathbf{w}}
$$

* $\mathbf{X} \in \mathbb{R}^{m \times (n+1)}$ is the **design matrix** (features for $m$ examples).
  The **first column is all ones** for the intercept, followed by $n$ feature columns.
* $\tilde{\mathbf{w}} \in \mathbb{R}^{(n+1)}$ stacks the **bias** $w_0$ and the $n$ weights $w_1,\dots,w_n$.
* $\hat{\mathbf{y}}$ are predictions **in log space**.

**Goal:** choose $\tilde{\mathbf{w}}$ so that predictions are as close as possible to the true targets $\mathbf{y}$ on the **training set**.

---

## 2) Why we don’t “just invert X”

If we (wrongly) treated $\mathbf{X}\,\tilde{\mathbf{w}}=\mathbf{y}$ as a square linear system, we might try
$\tilde{\mathbf{w}}=\mathbf{X}^{-1}\mathbf{y}$. But $\mathbf{X}$ is almost always **rectangular** (many rows, fewer columns), so $\mathbf{X}^{-1}$ **doesn’t exist**.

What we actually want is the **closest** solution in the least-squares sense:

$$
\min_{\tilde{\mathbf{w}}} \ \|\mathbf{X}\,\tilde{\mathbf{w}} - \mathbf{y}\|_2^2
$$

This gives the classic **normal equation**.

---

## 3) Normal equation (least squares solution)

Multiply both sides of $\mathbf{X}\,\tilde{\mathbf{w}} \approx \mathbf{y}$ by $\mathbf{X}^\top$:

$$
\mathbf{X}^\top \mathbf{X}\,\tilde{\mathbf{w}} \;=\; \mathbf{X}^\top \mathbf{y}
$$

If $\mathbf{X}^\top \mathbf{X}$ is **invertible** (it’s square $(n{+}1)\times(n{+}1)$), the minimizer is

$$
\boxed{\;\tilde{\mathbf{w}} \;=\; (\mathbf{X}^\top \mathbf{X})^{-1}\,\mathbf{X}^\top \mathbf{y}\;}
$$

This $\tilde{\mathbf{w}}$ is the **least-squares** solution (proofs in standard texts such as *The Elements of Statistical Learning*).

> Practical note: even when invertible, **don’t literally invert** matrices in code. Solve the system instead (numerically more stable).

---

## 4) Handling the intercept (bias) cleanly

You have two equivalent options:

* **Augment $\mathbf{X}$** with a leading column of ones and learn $w_0$ as part of $\tilde{\mathbf{w}}$ (what we’ll do here), **or**
* Let a library handle the intercept (e.g., scikit-learn’s `fit_intercept=True`).

**Never do both**.

---

## 5) Minimal NumPy implementation (normal equation)

We’ll write a small trainer that:

1. adds the bias column,
2. builds the Gram matrix $G=\mathbf{X}^\top\mathbf{X}$,
3. solves $G\,\tilde{\mathbf{w}}=\mathbf{X}^\top\mathbf{y}$.

```python
import numpy as np

def add_bias_column(X):
    """Add an intercept column of ones to feature matrix X (m, n) -> (m, n+1)."""
    m = X.shape[0]
    return np.hstack([np.ones((m, 1)), X])

def train_linear_regression_normal(X, y):
    """
    Train linear regression via the normal equation.

    X : (m, n)  feature matrix (no bias column)
    y : (m,)    target vector (e.g., log1p(msrp))

    Returns:
        w0 : float           bias (intercept)
        w  : (n,) np.ndarray weights for the n features
    """
    X_aug = add_bias_column(X)                # (m, n+1)
    XtX   = X_aug.T @ X_aug                   # (n+1, n+1)
    Xty   = X_aug.T @ y                       # (n+1,)

    # Prefer solve() to inv() for numerical stability
    w_aug = np.linalg.solve(XtX, Xty)         # (n+1,)
    w0, w = w_aug[0], w_aug[1:]
    return w0, w

def predict_linear(X, w0, w):
    """Predict in the model's target space (here: log1p)."""
    return w0 + X @ w

def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred) ** 2))
```

**Usage with our pipeline (log target):**

```python
# X_train, y_train are your training features/targets (y is log1p(msrp))
w0, w = train_linear_regression_normal(X_train, y_train)

# Validation in log space
y_val_pred_log = predict_linear(X_val, w0, w)
val_rmse_log = rmse(y_val, y_val_pred_log)

# Or convert to dollars for human-readable error
y_val_pred = np.expm1(y_val_pred_log)
y_val_true = np.expm1(y_val)                 # invert the validation targets too
val_rmse_dollars = rmse(y_val_true, y_val_pred)
```

Be explicit about which space your metric lives in (log vs dollars) and stick to it consistently.

---

## 6) Shapes and sanity checks

* $\mathbf{X}$: $(m, n)$ (no bias column yet)
* $\mathbf{X}_{\text{aug}}$: $(m, n{+}1)$ after adding ones
* $\tilde{\mathbf{w}}$: $(n{+}1,)$
* Predictions: $(m,)$

Common pitfalls:

* **Mismatched shapes** due to missing bias column.
* **Object dtypes** sneaking into `X` (ensure floats).
* Forgetting to **invert predictions with `expm1`** when reporting in dollars.

---

## 7) Numerical stability & when the inverse “doesn’t exist”

`np.linalg.solve(XtX, Xty)` needs $\mathbf{X}^\top\mathbf{X}$ to be **non-singular** (full rank). Problems arise when features are:

* **Collinear** (one is a linear combination of others),
* **Duplicated**, or
* Have wildly different scales (ill-conditioning).

**Fixes:**

* Use the **pseudo-inverse**:
  `w_aug = np.linalg.pinv(X_aug) @ y` (robust to singular `XtX`).
* Use **`np.linalg.lstsq`**:
  `w_aug, *_ = np.linalg.lstsq(X_aug, y, rcond=None)` (preferred in many cases).
* Add **regularization** (Ridge): solve $(X^\top X + \lambda I)\,w = X^\top y$. We’ll cover this soon.

Scaling features (e.g., standardization) also improves conditioning and numerical behavior.

---

## 8) End-to-end training checklist

1. **Use only the training split** to fit $w_0, w$.
2. **Predict on validation**; compute RMSE (either in log space or dollars).
3. Keep the **test split untouched** until the very end.
4. If you trained on `log1p(msrp)`, remember to use `np.expm1` before reporting dollar errors.

---

## 9) What’s next

You now have a working training routine for linear regression via the normal equation. Next, we’ll:

* compare with **iterative solvers** (gradient descent),
* add **regularization** to handle collinearity and stabilize solutions,
* and examine how these choices affect validation RMSE.
