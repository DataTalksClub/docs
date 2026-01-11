---
title: "16. Summary"
parent: "Module 2: Machine Learning for Regression"
nav_order: 16
---

# Module 2 Recap — Regression Project

<iframe width="560" height="315" src="https://www.youtube.com/embed/_qI01YXbyro" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Goal

Predict car MSRP from tabular features (make, model, year, specs, etc.).

## Data prep & EDA

* **Cleaning:** lowercased column names, replaced spaces with underscores; normalized string values.
* **EDA:** MSRP had a **long tail** → applied `log1p(msrp)` to stabilize variance and help models.
* **Missing values:** identified with `isna().sum()`; for baseline, filled numeric NAs with **0** (simple, not always ideal).

## Validation framework

* Split into **train / val / test** (60/20/20).
* Wrote a reusable `prepare_x(df)` to:

  * Build numeric features (+ **age = 2017 - year**).
  * Add chosen categorical one-hots (e.g., top-K per category).
  * Fill NAs consistently.
  * Return **NumPy arrays** with fixed column order.

## Linear regression, from scratch

* Started with scalar form → vector **dot product** → full **matrix × vector** form.
* Trained via **normal equation**: $w=(X^\top X)^{-1}X^\top y$.
* Baseline used only numeric features → OK but underfit.

## Metric

* **RMSE** on the **validation set** (computed in log space to match target transform).

## Feature engineering

* **Age** feature gave a **big improvement**.
* Added **categoricals** with one-hot (e.g., number\_of\_doors, make, fuel, transmission, driven\_wheels, size, style, market\_category).
* First attempt blew up (huge weights/RMSE) → **collinearity** made $X^\top X$ numerically unstable.

## Regularization (Ridge)

* Fixed instability by **adding λ to the diagonal** of $X^\top X$:
  $w=(X^\top X+\lambda D)^{-1}X^\top y$ (no penalty on intercept).
* Tuned **λ** on validation (grid of values); several close—picked a small λ that stabilized and slightly improved RMSE.

## Final model & test

* Retrained on **train+val** with best λ; evaluated once on **test** → similar RMSE to val (good generalization).
* Single-car inference: build a one-row DataFrame from a dict → `prepare_x` → predict log price → `expm1` to get dollars.

## What to save for serving

* `w0`, `w`, **feature order**, **category vocab** (top-K lists), NA-fill rules, and constants (e.g., reference year for age).

## Pitfalls you handled

* Target long tail → log transform.
* Data leakage → kept test unseen until the end.
* Feature drift → froze vocab/order in `prepare_x`.
* Multicollinearity → ridge regularization.
* Objective eval → RMSE on validation, then confirm on test.

## Next steps

* Try better missing-value strategies (median/mean per group).
* Add interactions/nonlinearities or switch to tree-based models (Random Forest, GBMs).
* Migrate to **scikit-learn** pipelines for cleaner training/serving.
