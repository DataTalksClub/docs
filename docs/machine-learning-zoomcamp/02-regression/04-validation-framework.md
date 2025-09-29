---
title: "04. Validation Framework"
parent: "Module 02: Regression"
nav_order: 4
---


# Setting Up the Validation Framework

<iframe width="560" height="315" src="https://www.youtube.com/embed/ck0IfiPaQi0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


In this lesson, we’ll build a **reproducible validation framework** for our car-price model. Concretely, we will:

1. **Split** the dataset into **train**, **validation**, and **test** subsets (60% / 20% / 20%).
2. **Shuffle** the rows to break any accidental order in the data.
3. **Extract targets** (`y`) with a **log1p** transform for stability.
4. **Remove the target** from the feature tables to prevent leakage.
5. **Reset indices** and verify sizes so the pipeline is tidy and reproducible.

This gives us a clean, dependable base to evaluate models before we start tuning or engineering features.

---

## 1) Why we split into train/validation/test

* **Train**: used to fit parameters.
* **Validation**: used repeatedly to choose models/hyperparameters.
* **Test**: touched **once**, at the very end, as an unbiased estimate of performance.

Keeping the test set isolated ensures we don’t “tune to the test” by accident.

---

## 2) Decide the split sizes (60/20/20) and compute counts

We’ll compute integer sizes using the total number of rows `n`. Because rounding can cause sums to drift, compute **train** as the **remainder** after picking **val** and **test**.

```python
import numpy as np
import pandas as pd

# df is your cleaned DataFrame
n = len(df)

n_val  = int(round(0.20 * n))
n_test = int(round(0.20 * n))
n_train = n - n_val - n_test

n, n_train, n_val, n_test
```

This guarantees `n_train + n_val + n_test == n`.

---

## 3) Shuffle indices for a fair split

Real datasets often come with structure (e.g., grouped by manufacturer or time). Splitting sequentially can push an entire group into one split (bad). We’ll **shuffle** row indices and **seed** the RNG for reproducibility.

```python
np.random.seed(2)             # reproducible splits
idx = np.arange(n)            # 0..n-1
np.random.shuffle(idx)        # in-place shuffling
```

Now take contiguous chunks **from the shuffled index** for each split:

```python
idx_train = idx[:n_train]
idx_val   = idx[n_train:n_train + n_val]
idx_test  = idx[n_train + n_val:]
```

---

## 4) Slice the DataFrame by iloc with shuffled indices

Use `iloc` with the shuffled index arrays to create the three DataFrames:

```python
df_train = df.iloc[idx_train].copy()
df_val   = df.iloc[idx_val].copy()
df_test  = df.iloc[idx_test].copy()
```

We `.copy()` to avoid chained-assignment pitfalls.

---

## 5) Reset the row indices (optional but tidy)

The split DataFrames will carry the original row indices. Resetting makes them clean and easier to inspect:

```python
for part in (df_train, df_val, df_test):
    part.reset_index(drop=True, inplace=True)
```

---

## 6) Build the target vectors (`y`) with log1p

We will predict **`msrp`**. As discussed in the previous lesson, `msrp` has a long right tail; applying a log transform (**`np.log1p`**) compresses extremes and often stabilizes regression.

```python
y_train = np.log1p(df_train['msrp']).values
y_val   = np.log1p(df_val['msrp']).values
y_test  = np.log1p(df_test['msrp']).values
```

Notes:

* We store them as **NumPy arrays** (models expect arrays).
* Later, when we predict, we’ll invert with **`np.expm1`**.

---

## 7) Remove the target from the feature tables to avoid leakage

Leaving `msrp` in the feature table is a classic leakage bug (the model “cheats”). Delete it **after** extracting `y`.

```python
for part in (df_train, df_val, df_test):
    del part['msrp']
```

From here on, `df_*` contain only **features**, while `y_*` contain the **log-transformed target**.

---

## 8) Sanity checks

Always verify sizes and alignment:

```python
assert len(df_train) == len(y_train) == n_train
assert len(df_val)   == len(y_val)   == n_val
assert len(df_test)  == len(y_test)  == n_test
```

If you see mismatches, re-check rounding and slicing boundaries.

---

## 9) (Optional) Notes on alternatives and robustness

* **Single-call split utilities**: Libraries (e.g., scikit-learn’s `train_test_split`) are convenient, but here we implemented the split manually to emphasize the mechanics and reproducibility.
* **Stratification in regression**: There’s no native “stratify” for continuous targets, but you can **bin** the target (e.g., quantiles of `msrp`) and stratify on those bins to balance ranges across splits. This is optional and situation-dependent.
* **Temporal data**: If the data has time order and you plan to forecast, use **time-based splits** rather than random shuffles. For our static car listings, random splits are fine.

---

## 10) What we have now—and what’s next

We now have:

* `df_train`, `df_val`, `df_test` — **feature** tables
* `y_train`, `y_val`, `y_test` — **log-transformed** targets
* A **reproducible** 60/20/20 split with a **fixed seed**
* No target leakage in features

**Next lesson:** we’ll implement **linear regression** on `df_train → y_train`, evaluate with **RMSE** on `df_val`, and establish a clear **baseline** before adding feature engineering or regularization.
