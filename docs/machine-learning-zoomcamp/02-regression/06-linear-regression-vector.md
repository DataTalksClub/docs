---
title: "06. Linear Regression in Vector & Matrix Form"
parent: "Module 02: Regression"
nav_order: 6
---


# Linear Regression in Vector & Matrix Form

<iframe width="560" height="315" src="https://www.youtube.com/embed/YkyevnYyAww" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


In the last lesson we wrote linear regression **for a single example** as a sum of feature contributions plus a bias. Now we’ll generalize that idea into a compact **vector** form (dot product) and then to the **matrix–vector** form that works on the entire dataset at once. This lets us compute predictions efficiently and reason about dimensions clearly.

---

## 1) Quick recap: single example, scalar form

For one car (one row of features) with $n$ features, we wrote the prediction as

$$
\hat{y}_i \;=\; w_0 \;+\; \sum_{j=1}^{n} w_j\,x_{ij}
$$

* $x_{ij}$: the $j$-th feature of the $i$-th example
* $w_0$: bias (intercept)
* $w_j$: weight for feature $j$

This is the scalar version: one number plus a sum over feature–weight products.

---

## 2) Dot product view (vector form)

Group the features of example $i$ into a **feature vector** $\mathbf{x}_i \in \mathbb{R}^n$ and the weights into $\mathbf{w} \in \mathbb{R}^n$. Then the sum becomes a **dot product**:

$$
\hat{y}_i \;=\; w_0 \;+\; \mathbf{w}^\top \mathbf{x}_i
$$

Same computation, just cleaner notation. In code, if `x_i` and `w` are 1-D arrays of length `n`, then:

```python
pred_i = w0 + np.dot(w, x_i)     # or: w0 + x_i @ w
```

---

## 3) Fold the bias into the dot product

The bias “hangs outside” the dot. We can incorporate it by **augmenting** the feature vector with a leading 1 and the weight vector with the bias:

$$
\tilde{\mathbf{x}}_i \;=\; \begin{bmatrix} 1 \\ \mathbf{x}_i \end{bmatrix} \in \mathbb{R}^{n+1}, 
\quad
\tilde{\mathbf{w}} \;=\; \begin{bmatrix} w_0 \\ \mathbf{w} \end{bmatrix} \in \mathbb{R}^{n+1}
$$

Now:

$$
\hat{y}_i \;=\; \tilde{\mathbf{w}}^\top \tilde{\mathbf{x}}_i
$$

This trick simplifies code because **all predictions become pure dot products**.

**Implementation pattern:**

```python
# x_i: shape (n,)
x_i_aug = np.concatenate(([1.0], x_i))   # shape (n+1,)
pred_i  = x_i_aug @ w_aug                # w_aug includes bias
```

---

## 4) From one row to all rows: matrix–vector form

Stack all $m$ augmented feature vectors $\tilde{\mathbf{x}}_i^\top$ as rows of a matrix $\mathbf{X} \in \mathbb{R}^{m \times (n+1)}$. Then predictions for **all** examples are a single matrix–vector product:

$$
\hat{\mathbf{y}} \;=\; \mathbf{X}\,\tilde{\mathbf{w}}
\quad\text{with}\quad
\mathbf{X}=
\begin{bmatrix}
1 & x_{11} & \dots & x_{1n} \\
1 & x_{21} & \dots & x_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
1 & x_{m1} & \dots & x_{mn} \\
\end{bmatrix}
$$

* Shapes: $\mathbf{X}$ is $(m \times (n{+}1))$, $\tilde{\mathbf{w}}$ is $((n{+}1) \times 1)$, so $\hat{\mathbf{y}}$ is $(m \times 1)$.

**NumPy pattern:**

```python
# X: (m, n) raw features
X_aug = np.hstack([np.ones((m, 1)), X])  # (m, n+1)
y_hat = X_aug @ w_aug                    # (m,)
```

That’s the whole model application in one line.

---

## 5) Minimal reference implementation

Below is a tiny, self-contained “predict” path that mirrors the math above. (Training will set `w_aug`; here we only show forward prediction.)

```python
import numpy as np

def add_bias_column(X):
    """Add a leading column of ones to X (m, n) -> (m, n+1)."""
    m = X.shape[0]
    return np.hstack([np.ones((m, 1)), X])

def predict_matrix(X, w_aug):
    """
    X: (m, n)  raw features (without bias column)
    w_aug: (n+1,) weights including bias
    returns: (m,) predictions in the model's target space
    """
    X_aug = add_bias_column(X)           # (m, n+1)
    return X_aug @ w_aug                 # (m,)
```

**For a single row:**

```python
def predict_row(x_i, w_aug):
    """
    x_i: (n,) one example
    w_aug: (n+1,)
    """
    x_i_aug = np.concatenate(([1.0], x_i))  # (n+1,)
    return x_i_aug @ w_aug
```

---

## 6) Working with log-transformed targets

If your target is $y = \log(1+\text{msrp})$ (as in previous lessons), the model’s output is in **log space**. Convert back to dollars with:

```python
y_pred_log = predict_matrix(X_val, w_aug)
y_pred     = np.expm1(y_pred_log)   # inverse of log1p
```

Be consistent: decide whether you’ll compute metrics **in log space** (e.g., RMSE of log targets) or **in dollars** (invert first, then compute RMSE). Both are legitimate; just be explicit.

---

## 7) Shapes, pitfalls, and good habits

* **Bias handling:** Add the column of ones yourself and set `fit_intercept=False` in libraries **or** let the library handle the intercept. Don’t do both.
* **Shape mismatches:** A common error is mixing row-vectors and column-vectors. Prefer 2-D feature matrices `(m, n)` and 1-D weight arrays `(n,)` (or `(n+1,)` for augmented). Use the `@` operator; avoid ambiguous broadcasting.
* **Copy vs view:** When you create `X_aug`, use concatenation/stacking (as above) to avoid mutating the original `X`.
* **Float dtypes:** Ensure numeric columns are `float` before matrix multiplies; implicit object dtypes will slow or break operations.

---

## 8) Why this matters

* The dot-product and matrix–vector view is not just notation—**it unlocks vectorized computation**, which is orders of magnitude faster than Python loops.
* Once in matrix form, training (solving for $\tilde{\mathbf{w}}$) becomes a linear-algebra problem, which we’ll tackle next (normal equations, gradient methods, and the role of regularization).

---

## 9) Where the weights come from (teaser)

We haven’t set the values of $\tilde{\mathbf{w}}$ yet. That’s the **learning** step: choose $\tilde{\mathbf{w}}$ to minimize a loss (typically mean squared error in log space) on the **training** split. In the next lesson we’ll derive and implement that, then evaluate on **validation**.
