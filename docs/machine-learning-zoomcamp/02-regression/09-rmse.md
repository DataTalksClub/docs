---
title: "9. Evaluating a Regression Model with RMSE"
parent: "Module 2: Machine Learning for Regression"
nav_order: 9
---


# Evaluating a Regression Model with RMSE

<iframe width="560" height="315" src="https://www.youtube.com/embed/0LWoFtbzNUM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


In the last lesson we trained a **baseline linear regression** using only numeric features and looked at its predictions qualitatively. Now we need a **quantitative** way to say how good (or bad) it is. Enter **RMSE — Root Mean Squared Error**. In this lesson we’ll define RMSE, unpack what it measures, implement it in a few lines of NumPy, and show exactly how to use it with our validation split.

---

## Why RMSE?

Visual checks (overlaid histograms, scatterplots) are useful, but they don’t give a single number you can compare across experiments. RMSE gives you:

* a **single scalar** that summarizes the typical prediction error,
* sensitivity to **large mistakes** (squares penalize big residuals),
* an interpretable unit: **same units as the target** (if the target is in dollars, RMSE is dollars; if it’s log-price, RMSE is in log units).

---

## Definition

For a dataset with $m$ examples, predictions $\hat{y}_i$ and true targets $y_i$:

$$
\mathrm{RMSE} \;=\; \sqrt{\frac{1}{m}\sum_{i=1}^{m}\left(\hat{y}_i - y_i\right)^2}
$$

Read it left-to-right:

1. compute the **error** $(\hat{y}_i - y_i)$ for each example,
2. **square** each error (makes negatives positive and punishes large errors),
3. take the **mean** of those squared errors,
4. take the **square root** to return to the original units.

---

## Tiny worked example (by hand)

Suppose:

* predictions: $[10,\; 9,\; 11,\; 10]$
* actuals:     $[ 9,\; 9,\; 10.5,\; 11.5]$

Errors: $[1,\; 0,\; 0.5,\; -1.5]$
Squared: $[1,\; 0,\; 0.25,\; 2.25]$
Mean squared error: $(1 + 0 + 0.25 + 2.25)/4 = 0.875$
RMSE: $\sqrt{0.875} \approx 0.935$

That “0.935” is in the **same units as the inputs**. If these were log-targets, it’s a log error; if they were dollars, it’s dollars.

---

## Implementation (NumPy)

A clean, vectorized version:

```python
import numpy as np

def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_pred - y_true) ** 2))
```

That’s all you need.

---

## Where to compute RMSE in our pipeline

We trained the model on **log-transformed** targets (`y = log1p(msrp)`). That gives us two valid choices:

### Option A — RMSE in log space (what the model actually predicts)

```python
y_val_pred_log = w0 + X_val @ w    # from your trained linear model
rmse_log = rmse(y_val, y_val_pred_log)
print("Validation RMSE (log space):", rmse_log)
```

**Interpretation tip:** if you had used plain `log(msrp)`, then `exp(rmse_log)` is the typical **multiplicative** error factor. With `log1p`, it’s similar for large prices; exact interpretation is slightly shifted for small prices.

### Option B — RMSE in dollars (human-friendly)

```python
y_val_pred = np.expm1(y_val_pred_log)
y_val_true = np.expm1(y_val)
rmse_dollars = rmse(y_val_true, y_val_pred)
print("Validation RMSE ($):", rmse_dollars)
```

Pick **one** and stick with it for comparisons. I usually track **both** during development: log RMSE for optimization, dollar RMSE for stakeholder reporting.

---

## Common pitfalls (avoid these)

* **Mixing splits:** compute RMSE on the **validation** set, not the training set (and reserve the test set for the very end).
* **Mismatched spaces:** don’t compare `log` predictions to **dollar** targets (or vice versa). Either both log or both dollars.
* **NaNs in features or targets:** ensure you imputed or removed them before predicting; otherwise your RMSE can silently become `nan`.
* **Shape/broadcast bugs:** `y_pred` and `y_true` must align (same length, same ordering).

---

## What a good number looks like

* **Relative sense:** compare RMSEs between models; **lower is better**.
* **Absolute sense (log space):** smaller log-RMSE means predictions are tighter multiplicatively. For rough intuition, if `rmse_log ≈ 0.2`, that’s about a ±22% multiplicative error factor (since `exp(0.2) ≈ 1.22`).
* **Absolute sense (dollars):** in \$, RMSE tells you a typical error size; e.g., “on average we’re off by about \$3,800.”

---

## Next steps

* Compute **validation RMSE** for your baseline numeric-only model.
* Use it as a **benchmark**.
* Then iterate: better imputation (e.g., medians), add **categorical encodings** (make, model, transmission…), and consider **regularization** (Ridge). Each time, recompute validation RMSE and keep the improvement if it’s real.

That’s how you turn a qualitative impression into a quantitative, defensible evaluation.

