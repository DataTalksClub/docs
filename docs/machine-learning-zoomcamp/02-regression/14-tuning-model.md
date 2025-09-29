---
title: "14. Tuning Model"
parent: "Module 2: Machine Learning for Regression"
nav_order: 14
---

# Lesson 14 — Finding the best regularization strength for Ridge regression

<iframe width="560" height="315" src="https://www.youtube.com/embed/lW-YVxPgzQw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Why we’re doing this

Last time we added **regularization** (Ridge) to tame exploding weights from one-hot features. Ridge introduces a single knob, the regularization strength **λ** (your `r`). Turn it too low and the model stays wobbly; too high and it becomes a flat, underfitting pancake. Today we’ll **pick λ systematically** using the **validation set**.

---

## What “best” means here

We’ll define “best” as the value of λ that **minimizes validation RMSE** (the same RMSE we’ve been using on the **log-price** target). That gives us a number we can defend: the model that generalizes best to unseen-but-similar data.

> Tiny reminder: our target is `log1p(price)`. RMSE is therefore measured in *log-dollars*. That’s fine for model selection. If you want intuition in dollars later, you can convert predictions back with `expm1` and compute RMSE there as well (that’s essentially RMSLE vs. RMSE on original scale trade-offs).

---

## The search plan (simple, solid, and fast)

1. **Fix the data pipeline.**

   * Use the same `prepare_x(df)` for **both** train and validation.
   * Build category lists (top-K values per categorical feature) **from train only**, reuse on validation.
   * Keep the **same column order** for X across splits.

2. **Choose a grid of λ values** on a **logarithmic scale**. For example:

   $$
   \lambda \in \{0, 10^{-6}, 10^{-5}, 10^{-4}, 10^{-3}, 10^{-2}, 10^{-1}, 1, 10\}.
   $$

   * `0` gives you the non-regularized baseline.
   * The rest span several orders of magnitude so we don’t miss the sweet spot.

3. **For each λ in the grid**:

   * Train: $(X_{\text{train}}^\top X_{\text{train}} + \lambda D)^{-1} X_{\text{train}}^\top y_{\text{train}}$
     (with **no penalty on the intercept**; i.e., the first diagonal entry in $D$ is 0, the rest are 1s).
   * Predict on **validation**: $\hat{y}_{\text{val}} = X_{\text{val}} w$.
   * Compute **RMSE** on validation.

4. **Pick λ with the lowest validation RMSE.**

   * If multiple λ’s tie within noise, prefer the **larger** one (slightly more shrinkage = safer).

5. **Retrain** one last time with the chosen λ on the **train set** (we’ll fold val in later when we finalize).

---

## Reading the output you’ll print

You’ll likely print a row per λ, something like:

```
lambda=0        bias=HUGE           rmse=HIGH
lambda=1e-6     bias=reasonable     rmse=↓
lambda=1e-4     bias=stable         rmse=↓ a bit more
lambda=1e-2     bias=stable         rmse=best (or near-best)
lambda=1        bias=shrunk         rmse=↑ (underfitting)
lambda=10       bias=tiny           rmse=↑↑
```

The typical pattern: dramatic improvement from 0 → small λ, a broad **flat minimum** somewhere around $10^{-3}$–$10^{-1}$, then degradation as λ gets large.

If your printout suggests λ≈0.01 performs best (as you saw), that’s a perfectly reasonable choice.

---

## Guardrails and gotchas

* **Dummy variable trap:** keep an intercept **or** all dummies minus one per category, not both. (Ridge helps numerically but can’t fix a logical redundancy.)
* **Feature consistency:** `prepare_x` must build **the same columns** for train and validation. Lock in the category list from train; unseen categories in validation should simply produce all-zeros across the corresponding one-hots (or map to an “other” flag if you added one).
* **Randomness:** If shuffling affects your split, set a **random seed** so the search is reproducible while you iterate.
* **Metric scale:** Remember your RMSE is on the **log** target; that’s intentional. Don’t mix scales mid-experiment.

---

## Optional polish (nice to have)

* **Plot RMSE vs. log10(λ).** It’s easier to see the U-shape and pick the stable zone.
* **K-fold cross-validation** on train instead of a single validation split if your dataset is small or you want a more robust pick.
* **Nested CV** if you’re publishing results or need strict separation between model selection and performance estimation. For a practical project, the train/val/test scheme is usually sufficient.

---

## What happens next

You now have the λ that behaves best on validation. In the **next lesson**, we’ll do the final sanity check:

1. Retrain with that λ (often on **train + validation** to use all the signal).
2. Evaluate **once** on the held-out **test** set to report the final RMSE.
3. Convert a few predictions back to dollars to sanity-check they make sense.

That’s the full loop: **regularize → tune λ → lock it in → test**.
