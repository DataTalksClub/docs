---
title: "03. Exploratory Data Analysis"
parent: "Module 02: Regression"
nav_order: 3
---


# Exploratory Data Analysis for Car Price Prediction
<iframe width="560" height="315" src="https://www.youtube.com/embed/k6k8sQ0GhPM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

In this lesson, we’ll **explore the dataset** to understand its columns, inspect value ranges and categories, **visualize the target (`msrp`)**, and handle common issues like **long-tail distributions** and **missing values**. The goal is to form a clear mental model of the data before we build any models.

---

## What we’ll do

1. **Audit columns**: types, examples, and cardinality.
2. **Visualize the target** (`msrp`) to understand its distribution.
3. **Tame the long tail** using a log transform and discuss why it helps.
4. **Quantify missingness** and outline options to handle it.
5. **Set up next steps** for validation and modeling.

---

## 1) Quick column audit

We’ll iterate through columns and print basic info: first values, a sample of **unique values**, and **number of unique values** (cardinality). This is useful for spotting obvious data cleaning needs and understanding feature types.

```python
import pandas as pd

# Assume df is already loaded and cleaned for names/strings as in the previous lesson
df.dtypes

for col in df.columns:
    s = df[col]
    print(f"\n=== {col} ===")
    print("dtype:", s.dtype)
    # Show a few example values safely
    print("head:", s.head().tolist())
    # Unique count
    try:
        nun = s.nunique(dropna=True)
        print("n_unique:", nun)
        # Peek at a few unique values (only sensible for categoricals / low-cardinality)
        if s.dtype == "object" or nun < 30:
            print("sample unique:", list(s.dropna().unique())[:5])
    except Exception as e:
        print("unique check skipped:", e)
```

Typical observations you’ll see:

* **Categoricals**: `make`, `model`, `engine_fuel_type`, `transmission_type`, `driven_wheels`, `market_category` (often messy and mixed-case in raw data).
* **Numericals**: `year`, `engine_hp`, `engine_cylinders`, `highway_mpg`, `city_mpg`, `popularity`, and the target **`msrp`**.
* `popularity` is usually a derived indicator (e.g., based on mentions), so treat it as a numeric feature but keep in mind its definition.

High cardinality in `model` is expected (many distinct models per manufacturer). This matters for encoding choices later.

---

## 2) Visualize the target distribution (`msrp`)

A histogram provides a fast view of the shape and scale of prices.

```python
import matplotlib.pyplot as plt

ax = df['msrp'].plot(kind='hist', bins=50)
ax.set_title('MSRP Distribution')
ax.set_xlabel('msrp')
plt.show()
```

What you’ll likely see:

* A **heavy concentration** of relatively affordable prices.
* A **long right tail**: a small number of very expensive cars (e.g., high-end or exotic models).
* Scientific notation on the axis (e.g., `1e6` = 1,000,000) when values are large.

If the long tail hides structure in the bulk of the data, zoom into a more “typical” price range:

```python
df.loc[df['msrp'] <= 100_000, 'msrp'].plot(kind='hist', bins=50)
plt.title('MSRP (≤ 100k)'); plt.xlabel('msrp'); plt.show()
```

This helps visualize the body of the distribution without the extreme outliers dominating the plot. You may also notice artifacts (e.g., a spike at 1,000) from platform-imposed minimum listing prices.

> **Tip:** The number of bins changes interpretability. You can try heuristics like Sturges or Freedman–Diaconis, but starting with 30–50 is usually fine for a first pass.

---

## 3) Handling long tails with a log transform

Long right tails often **confuse regression models** by forcing them to trade off between fitting the bulk of common prices and rare but extreme values. A standard remedy is to **log-transform** the target:

* Log compresses large values, making the distribution **more symmetric**.
* Many loss functions behave more stably on log-scaled targets.
* Errors become **multiplicative** in the original space (i.e., closer to relative error).

We’ll use `np.log1p` (log of 1 + x). It is numerically stable and avoids issues with zero values:

```python
import numpy as np

y = df['msrp'].values
y_log = np.log1p(y)  # log(1 + msrp)

pd.Series(y_log).plot(kind='hist', bins=50)
plt.title('log1p(msrp) Distribution'); plt.xlabel('log1p(msrp)'); plt.show()
```

What changes:

* The right tail collapses, and the histogram looks **more bell-shaped** (closer to normal).
* This typically makes linear models happier and reduces sensitivity to outliers.

**Training & inference notes:**

* If you train on `log1p(msrp)`, remember to **invert** predictions with `np.expm1`:

  ```python
  y_pred_log = model.predict(X_val)
  y_pred = np.expm1(y_pred_log)
  ```
* Metrics: decide whether you’ll evaluate error in **log space** (easier for model comparisons) or convert back to the original scale and compute **RMSE in dollars** (often more interpretable for stakeholders). Be explicit and consistent.

---

## 4) Missing values: audit and plan

Before modeling, quantify missingness so you can plan imputations or drops.

```python
missing_counts = df.isna().sum().sort_values(ascending=False)
missing_ratio = (df.isna().mean().sort_values(ascending=False) * 100).round(2)

print(missing_counts.head(12))
print(missing_ratio.head(12), '%')
```

Typical findings:

* Gaps in **`market_category`**, **`engine_hp`**, **`engine_cylinders`**, occasionally **`fuel_type`** or **`num_of_doors`**.
* Missingness can be **informative** (e.g., specific trims or model years lacking certain fields).

**Options to handle missingness (later in the pipeline):**

* **Numerical**: median/mean imputation, model-based imputation, or flag missingness with an extra indicator column.
* **Categorical**: introduce an explicit `"missing"` category (common with one-hot encoding).
* **Row drops**: acceptable if the fraction is tiny and the rows aren’t systematically different.
* **Advanced**: iterative imputation (e.g., `IterativeImputer`) when the signal lost is material.

> Keep the imputation decisions inside a **reproducible pipeline** (e.g., scikit-learn `ColumnTransformer` + `Pipeline`) so training and validation treat data identically.

---

## 5) Summary & next steps

* We **audited columns** and cardinality to understand feature types.
* We **visualized `msrp`**, identified a **long-tail** pattern, and **log-transformed** the target with `np.log1p` to stabilize modeling.
* We **quantified missing values** and outlined practical imputation strategies to use in the modeling pipeline.

**Next lesson:** we’ll set up the **validation framework**—define a split strategy, lock down evaluation metrics (e.g., RMSE), and build a baseline linear regression (trained on `log1p(msrp)`), so we have a clear benchmark before feature engineering.
