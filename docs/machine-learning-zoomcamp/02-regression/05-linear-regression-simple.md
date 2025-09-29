---
title: "05. Linear Regression"
parent: "Module 02: Regression"
nav_order: 5
---


# Linear Regression

<iframe width="560" height="315" src="https://www.youtube.com/embed/Dn1eTQLsOdA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


In this lesson we introduce **linear regression** and build up from an intuitive, single-example view to the compact mathematical form you’ll use in code. We’ll also connect predictions in **log space** back to **dollars** using `expm1`, consistent with the `log1p(msrp)` target we prepared earlier.

---

## What linear regression is (and when to use it)

* **Problem type:** regression — the output is a **number** (here: car price).
* **Idea:** predict a target $y$ from input features $x$ using a **linear function** of those features.

At a high level:

$$
\hat{y} = g(x) \quad\text{with}\quad g \text{ chosen to be linear}
$$

Because we trained/plan to train on $\log(1 + \text{msrp})$, our model will output values in **log space**. We’ll invert with $\text{expm1}$ at the end to report prices in dollars.

---

## Start with one car (single-example view)

Take a single row from **training** data (we only use train to fit/illustrate the model):

* **Engine horsepower:** $x_1 = 453$
* **City MPG:** $x_2 = 11$
* **Popularity:** $x_3 = 86$

Collect these into a feature vector $\mathbf{x}_i = (x_{i1}, x_{i2}, x_{i3})$.

We want a function $g$ that maps this $\mathbf{x}_i$ to a **predicted log-price** that’s close to the true (log) price.

---

## The linear model, first as a sum

Linear regression assumes:

$$
\hat{y}_i \;=\; w_0 \;+\; w_1 x_{i1} \;+\; w_2 x_{i2} \;+\; w_3 x_{i3}
$$

* $w_0$ is the **bias** (intercept): the baseline prediction if we “knew nothing” about the car.
* $w_j$ is the **weight** for feature $x_{ij}$: how much the prediction changes when that feature increases by 1 unit, holding others fixed.

Compactly, for $n$ features:

$$
\hat{y}_i \;=\; w_0 \;+\; \sum_{j=1}^{n} w_j x_{ij}
$$

Vector form (you’ll see/implement this soon):

$$
\hat{y}_i \;=\; w_0 \;+\; \mathbf{w}^\top \mathbf{x}_i
$$

---

## A concrete plug-in example

Suppose (just for illustration) we pick:

* $w_0 = 7.17$
* $w_1 = 0.01$ (horsepower)
* $w_2 = 0.04$ (city MPG)
* $w_3 = 0.002$ (popularity)

Then for our car:

$$
\hat{y}_i
= 7.17 + 0.01\cdot 453 + 0.04\cdot 11 + 0.002\cdot 86
\approx 12.31
$$

This $\hat{y}_i$ is in **log space** because our target is $\log(1+\text{msrp})$. Convert back to dollars with:

$$
\widehat{\text{msrp}} \;=\; \operatorname{expm1}(\hat{y}_i)
$$

Numerically, that gives roughly **\$222,000** for this car, which matches the intuition that high horsepower and low city MPG are associated with costlier cars.

> Notes on interpretation
>
> * **Bias $w_0$:** the baseline (log) price with all features at zero (not literally meaningful if zero is outside the data range, but still useful mathematically).
> * **Weights:** positive $w_j$ means “more of $x_j$ → higher predicted price (in log space)”; negative means the opposite. Magnitudes are on the log scale; a unit change in $x_j$ adds $w_j$ to $\log(1+\text{price})$, i.e., a **multiplicative** change in price after exponentiation.

---

## From one row to the whole training matrix

Let $\mathbf{X}$ be the **feature matrix** (rows = cars, columns = features) and $\mathbf{y}$ be the vector of targets (here, $y_i = \log(1+\text{msrp}_i)$).

Across all training examples:

$$
\hat{\mathbf{y}} \;=\; w_0 \cdot \mathbf{1} \;+\; \mathbf{X}\mathbf{w}
$$

Training linear regression means “**find $w_0,\mathbf{w}$ that minimize error**” between $\hat{\mathbf{y}}$ and $\mathbf{y}$ on the training set, typically by minimizing **mean squared error** in log space. In code you’ll either:

* implement the math directly (normal equations / gradient methods), or
* use a library routine and focus on data prep + evaluation.

---

## Why we stayed in log space (and how to invert)

Because prices have a **long right tail**, modeling $\log(1+\text{msrp})$ yields:

* a more symmetric, bell-shaped target,
* more stable optimization,
* errors that behave closer to **relative** errors in the original units.

At prediction time:

* Model outputs $\hat{y} = \log(1+\widehat{\text{msrp}})$.
* Convert to dollars with `np.expm1(\hat{y})`.

When you evaluate in dollars (e.g., RMSE in \$), remember to invert predictions first.

---

## What comes next

* Generalize from one example to **vectorized code** for many rows.
* Fit $w_0, \mathbf{w}$ on the **training** split, measure **RMSE** on **validation**.
* Keep the **test** split untouched until the end for an unbiased final check.

That’s the full path from the intuitive sum of feature-contributions to a working linear model you can train and evaluate.
