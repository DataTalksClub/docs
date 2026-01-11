---
title: "13. Regularization"
parent: "Module 2: Machine Learning for Regression"
nav_order: 13
---

# Regularization: keeping linear regression sane

<iframe width="560" height="315" src="https://www.youtube.com/embed/91ve3EJlHBc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Where we left off

We just expanded our feature space with a bunch of categorical variables (via one-hot encoding) and folded that into `prepare_X`. On paper that should have helped. Instead, validation RMSE shot up and the learned weights exploded to ridiculous values. Time to talk about **regularization**—what it is, why we need it, and how to apply it cleanly.

---

## The normal equation, and where it goes sideways

Our linear model predicts

$$
\hat{y} \;=\; Xw,
$$

and the “closed form” solution for the weights is the **normal equation**:

$$
\hat{w} \;=\; (X^\top X)^{-1}X^\top y.
$$

The matrix $G=X^\top X$ is called the **Gram matrix**. The normal equation works only if we can compute $G^{-1}$. Two common failure modes:

1. **Non-invertible (singular) $X^\top X$.**
   This happens when some columns of $X$ are **exact linear combinations** of others (perfect multicollinearity). Example: duplicate columns, or the **dummy variable trap**—including *all* one-hot indicators for a categorical column **and** an intercept. In that case, the columns sum to the intercept and you’ve got linear dependence.

2. **Numerically ill-conditioned $X^\top X$.**
   Even if there isn’t *exact* duplication, columns can be *almost* linear combinations (e.g., two one-hots that co-occur in near lockstep, or lots of very rare/sparse dummies). Then $X^\top X$ has tiny eigenvalues; inverting it amplifies noise and you get gigantic, unstable coefficients. You might not see an outright “singular matrix” error, just wild numbers and terrible validation error.

If your RMSE jumped and the coefficients look absurd, you’ve almost certainly hit (2), often encouraged by (1).

---

## Why our car model triggered this

* We added many 0/1 dummy columns (some rare).
* We kept an intercept **and** all dummies for a category → dummy variable trap.
* Even apart from the trap, rare categories and correlated indicators make $X^\top X$ poorly conditioned.
* The normal equation dutifully tries to invert it and goes off the rails.

We need to **stabilize** the inversion.

---

## The idea of regularization (Ridge / L2)

Regularization gently discourages large weights. For linear regression, the most common form is **Ridge regression** (L2):

$$
\hat{w} \;=\; (X^\top X \;+\; \lambda I)^{-1} X^\top y.
$$

That tiny $\lambda I$ on the diagonal does two things:

* **Numerical stability:** it **shifts** every eigenvalue of $X^\top X$ upward by $\lambda$. No more near-zero eigenvalues → no more exploding inverse.
* **Statistical bias/variance trade-off:** larger $\lambda$ shrinks coefficients toward 0, reducing variance (overfitting) at the cost of a bit of bias.

> Subtle but important: we usually **do not penalize the intercept**. Implementation-wise, that means adding $\lambda$ on the diagonal for feature weights but leaving the intercept row/column unpenalized. (If your code folds the intercept into $X$ as a leading column of ones, you can add $\lambda$ only to the last $p$ dimensions, not to the first.)

**Limits to build intuition**

* $\lambda = 0$ → ordinary least squares (your current unstable solution).
* $\lambda \to \infty$ → all coefficients go to 0 (model predicts a flat line near the intercept).

---

## A cleaner training function (concept)

You already have a `train_linear_regression` that forms $X^\top X$, inverts it, and multiplies by $X^\top y$. The regularized variant changes only one line:

1. Build design matrix **with** intercept in the data (a column of ones up front).
2. Compute $G = X^\top X$.
3. Add $\lambda$ to the diagonal **except** the intercept position.
4. Solve $(G + \lambda D) w = X^\top y$ where $D$ is diag(0, 1, 1, …, 1).
5. Return $w_0$ (bias) and $w$ (feature coefficients).

Under the hood this is Ridge. If you ever switch to off-the-shelf libraries, this corresponds to `Ridge(alpha=λ, fit_intercept=True)`.

---

## Regularization vs. the dummy trap

Ridge will **stabilize** many near-dependencies, but it doesn’t *remove* exact linear dependence. If you keep the intercept and **every** dummy for a category, the columns are perfectly collinear, and even $\lambda I$ can’t cure the logical redundancy—you’ll still be in trouble or, at best, get arbitrary solutions.

**Do one (or both):**

* **Drop one dummy per categorical column** (use it as the baseline).
* **Use Ridge** to handle the remaining near-collinearity and sparse rarities.

That combo is robust and standard.

---

## Picking the regularization strength $\lambda$

$\lambda$ is a genuine **hyperparameter**. Here’s a simple, reliable routine:

1. Choose a search grid on a **log scale**, e.g.
   $\{10^{-6}, 10^{-5}, …, 10^{0}, 10^{1}\}$.
2. For each $\lambda$: train on **train**, evaluate RMSE on **validation** (using the same `prepare_X` that produced your train features).
3. Pick the $\lambda$ with the **lowest validation RMSE**.
4. Lock that in, then later retrain on train+validation and test once at the end.

**Heuristics**

* If coefficients are still huge or RMSE is unstable → increase $\lambda$.
* If RMSE steadily worsens as $\lambda$ grows → you’re over-shrinking; move down.

---

## Practical guardrails (so you don’t relive the pain)

* **Build category lists on train only.** Use top-K most frequent values per categorical column; treat everything else as “other” (or drop rare ones) to keep the feature space compact.
* **Drop one dummy per categorical group** if you keep an intercept.
* **Impute consistently** (your 0-fill for numerics is fine for baselines; median/mean is also common).
* **Keep a deterministic column order** from train and reuse it for val/test.
* **Prefer a stable solver.** If you’re not using Ridge, at least swap a raw matrix inverse for a numerically safer routine (`lstsq`, pseudo-inverse). Ridge is still the better fix.

---

## What to expect after adding Ridge

* Validation RMSE should **drop** back to a sensible number—often **better** than your numeric-only baseline because the model can now safely use categorical signal.
* Coefficients become **smaller** and far less erratic; the intercept returns to a reasonable scale.
* Training remains fast—Ridge adds a tiny constant-time tweak to the normal equation.

---

## Why adding $\lambda I$ works (quick geometric intuition)

Think of $X^\top X$ as stretching space along its principal directions (eigenvectors). When one direction has almost no variance (tiny eigenvalue), inverting that stretch requires dividing by an almost-zero—kaboom. Adding $\lambda I$ lifts every eigenvalue by $\lambda$, so the dangerous divisions never happen. It’s like putting a ruler under a wobbly table leg.

---

## Wrap-up

* The blow-up after adding many dummies wasn’t mystical—it was **multicollinearity** and **ill-conditioning**.
* **Ridge (L2) regularization** fixes the numerics and reduces overfitting:

  $$
  \hat{w} = (X^\top X + \lambda I)^{-1} X^\top y
  $$

  (usually without penalizing the intercept).
* Combine Ridge with **drop-one-dummy** and **top-K categories** for a sturdy baseline.
* Choose $\lambda$ by **validation search** on a log scale.

Next up: we’ll actually **tune $\lambda$**, compare RMSE across candidates, and lock in a well-regularized model for car price prediction.
