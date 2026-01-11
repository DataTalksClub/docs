---
title: "12. Categorical Variables"
parent: "Module 2: Machine Learning for Regression"
nav_order: 12
---

# Categorical Variables

<iframe width="560" height="315" src="https://www.youtube.com/embed/sGLAToAAMa4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


**Goal:** fold *categorical* information (make, fuel type, transmission, etc.) into our linear model, do it in a reproducible way across train/validation/test, and understand why the seemingly simple step can wreck the normal-equation solver if we’re careless.

---

## 1) What are categorical variables?

Columns whose values are **names/labels** rather than magnitudes: `make`, `model`, `engine_fuel_type`, `transmission_type`, `driven_wheels`, `vehicle_size`, `vehicle_style`, `market_category`, etc.

Caveat: some columns look numeric but are **categorical by nature**. Example: `number_of_doors` (2, 3, 4). Treating it as a real number implies linear spacing (“3 doors is halfway between 2 and 4”); that’s not meaningful for price.

---

## 2) The standard encoding: one-hot (a.k.a. dummy variables)

Given a column like `number_of_doors` with values {2, 3, 4}, create **one binary column per value**:

```
doors_2, doors_3, doors_4  ∈ {0,1}
```

Each row has 1 in exactly one of these columns (or 0s if missing/unknown).

You can do this manually:

```python
d = df.copy()
for v in [2, 3, 4]:
    d[f"doors_{v}"] = (d["number_of_doors"] == v).astype(int)
```

> Tip: if `number_of_doors` sometimes comes as strings (“two”), normalize to integers before encoding, or map others to an `"unknown"` bucket.

---

## 3) Integrate with `prepare_X` (without mutating inputs)

We extend our earlier feature builder (which already handles numerics and `age`) to also add one-hot columns. **Don’t** mutate the original dataframe; always work on a copy. Also, don’t keep appending to the global “base” list—clone it first.

```python
import numpy as np

NUMERIC_COLS = ["engine_hp", "engine_cylinders", "highway_mpg", "city_mpg", "popularity"]
REFERENCE_YEAR = 2017

def prepare_X(df, categories=None, door_values=(2,3,4), reference_year=REFERENCE_YEAR):
    """
    Build design matrix with numerics + age + selected categorical dummies.

    - df: any split (train/val/test)
    - categories: dict {col: [top values]} built from TRAIN ONLY (see §4)
    """
    d = df.copy()

    # Derived numeric: age
    d["age"] = np.maximum(0, reference_year - d["year"])

    # Start features with numerics + age (copy to avoid mutating a shared list)
    features = list(NUMERIC_COLS) + ["age"]

    # One-hot for number_of_doors (categorical, even if numeric-looking)
    for v in door_values:
        col = f"doors_{v}"
        d[col] = (d["number_of_doors"] == v).astype(int)
        features.append(col)

    # General categorical one-hots (top-K per column)
    if categories is not None:
        for col, top_values in categories.items():
            # Optionally normalize case/whitespace for robustness
            src = d[col].fillna("__nan__")
            for v in top_values:
                name = f"{col}__{v}"
                d[name] = (src == v).astype(int)
                features.append(name)

    # Basic numeric imputation (can swap to median later)
    d[features] = d[features].fillna(0)

    # Return the dense matrix for our linear solver
    return d[features].values
```

---

## 4) Selecting which categories to include (do this on **train only**)

Some columns have **dozens or thousands** of distinct values (e.g., `model`). Encoding them all explodes the feature space and destabilizes the normal equation. A pragmatic baseline is to keep just the **top-K most frequent values** per categorical column.

Build the *catalog* of chosen values **from the training data**, then reuse it verbatim for val/test:

```python
CATEGORICAL_COLS = [
    "make", "engine_fuel_type", "transmission_type", "driven_wheels",
    "market_category", "vehicle_size", "vehicle_style"
]

def top_k_categories(df_train, cols=CATEGORICAL_COLS, k=5):
    cats = {}
    for c in cols:
        # Normalize missing to a sentinel so it can be selected if it’s common
        vc = df_train[c].fillna("__nan__").value_counts()
        cats[c] = vc.head(k).index.tolist()
    return cats

categories = top_k_categories(df_train, k=5)

# Build matrices consistently
X_train = prepare_X(df_train, categories=categories)
X_val   = prepare_X(df_val,   categories=categories)
```

> Why this matters: If you re-compute “top 5” on validation, the chosen levels might differ, so your design matrices won’t align (different columns). Build once, reuse everywhere.

---

## 5) What actually helps?

* **`age`**: usually a large gain (we already saw that).
* **`number_of_doors`**: often *minor* improvement—the signal is weak compared to age, engine specs, make.
* **`make`**: a modest, consistent improvement (brand effects on price).
* Other small-cardinality columns (`transmission_type`, `driven_wheels`, `engine_fuel_type`) often help slightly.

Expect small, incremental drops in validation RMSE as you add these. It’s normal that the jump from adding `age` dwarfs the rest.

---

## 6) The gotcha: why your RMSE suddenly explodes

> Symptom: after adding “a lot” of dummies, your validation RMSE jumps from \~0.5 to **\~41**, coefficients are gigantic, and `w0` is some absurd value in scientific notation.

**Root causes (often combined):**

1. **Dummy variable trap (perfect multicollinearity):**
   For each categorical column, the sum of all its dummies equals 1. If you *also* include an intercept (bias) column, the columns are linearly dependent. That makes $X^TX$ **singular or ill-conditioned**, and the normal equation $(X^TX)^{-1}X^Ty$ blows up.

   * **Fix (classic):** for each category, **drop one dummy** (baseline level), or
   * **Alternative:** remove the intercept (we keep it), or
   * **Better in practice:** keep intercept **and** use **regularization (Ridge)**, which stabilizes the inversion.

2. **Too many sparse columns vs. rows:**
   If you add many rare categories (lots of zeros, few ones), $X^TX$ becomes near-singular (huge condition number). Ridge helps again.

3. **Inconsistent columns across splits:**
   If train and validation design matrices don’t have identical columns in the same order, you’ll multiply by the wrong weights. Always build columns from train and **reindex** other splits accordingly (the pattern above with a fixed `categories` dict guarantees this).

4. **Data leakage/peeking:**
   Recomputing top-K on validation changes the features and can make comparisons meaningless.

**Takeaway:** exploding coefficients aren’t “bad linear regression”—they’re a **numerical stability** problem caused by collinearity and a brittle inversion step.

---

## 7) Practical guardrails

* **Drop-one-dummy per categorical group** when using a plain normal equation **or** just move to **Ridge** (next lesson).
* **Keep an intercept** (bias) term; it makes models easier to interpret.
* **Stabilize the solve:** prefer `np.linalg.lstsq` or `np.linalg.pinv` over a raw inverse when prototyping; switch to Ridge for production.
* **Control cardinality:** use top-K or an `"other"` bucket; avoid one-hotting `model` at full granularity initially.
* **Deterministic schema:** build the set of columns from **train only** and reuse everywhere.

---

## 8) Minimal drop-one-dummy tweak (if you stick with the normal equation)

If you’re not ready for regularization yet, drop one level per categorical column:

```python
def prepare_X_drop_first(df, categories, ...):
    d = df.copy()
    d["age"] = np.maximum(0, REFERENCE_YEAR - d["year"])
    features = list(NUMERIC_COLS) + ["age"]

    # doors: drop one (e.g., doors_4 as baseline)
    for v in (2,3):  # drop 4
        name = f"doors_{v}"
        d[name] = (d["number_of_doors"] == v).astype(int)
        features.append(name)

    # categoricals: drop the first level in each list as baseline
    for col, values in categories.items():
        for v in values[1:]:  # skip the first (baseline)
            name = f"{col}__{v}"
            d[name] = (d[col].fillna("__nan__") == v).astype(int)
            features.append(name)

    d[features] = d[features].fillna(0)
    return d[features].values
```

This eliminates perfect linear dependence with the intercept.

---

## 9) Summary

* We converted categorical columns into **one-hot features** and folded them into `prepare_X` cleanly (no input mutation, consistent schema).
* `age` and `make` usually yield visible improvements; `number_of_doors` is a small bump at best.
* Adding many dummies can **break** the normal equation due to **multicollinearity** (dummy variable trap) and **ill-conditioning**.
* Quick fixes: **drop one dummy per category** or switch to a more robust solver; real fix: **regularization**.

**Next lesson:** we’ll tackle **numerical stability** head-on with **regularization (Ridge)** so we can safely add richer categorical sets without melting the solver—and we’ll quantify the gains on the validation split.
