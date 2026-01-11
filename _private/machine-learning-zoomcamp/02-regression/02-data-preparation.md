---
title: "2. Data Preparation"
parent: "Module 2: Machine Learning for Regression"
nav_order: 2
---


# Preparing the Dataset for the Car Price Prediction Project

<iframe width="560" height="315" src="https://www.youtube.com/embed/Kd74oR4QWGM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


In this lesson, we get practical: we’ll **locate the dataset**, **download it**, **load it into Pandas**, and **normalize names and text values** so everything is easy to work with in the next steps of the project.

---

## 1) Where the data lives and how to download it

We’ll use the copy of the dataset stored in the course GitHub repository (the folder for the “car price” chapter). Inside you’ll find two things we care about:

* A **Jupyter notebook** with the lesson’s code
* A **CSV file** with the data

Download the CSV via either:

* Your browser (“Save as…” from the raw file view), or
* The terminal with `wget <direct-file-url>`

> If you already have the file locally, you’ll see the usual OS behavior (e.g., appending `(1)` to avoid overwriting). That’s fine.

---

## 2) Load the dataset into Pandas

We’ll load the CSV and immediately peek at the first rows to sanity-check what we got:

```python
import pandas as pd

df = pd.read_csv("path/to/your.csv")  # use the actual filename from the repo
df.head()
```

You should see columns like **make**, **model**, **year**, engine and fuel characteristics, transmission information, etc. The target we want to predict is **`MSRP`** — *Manufacturer’s Suggested Retail Price*.

---

## 3) Why we normalize names (and what “Index” has to do with it)

You’ll notice some **inconsistencies** in column names:

* A mix of **upper** and **lower** case
* **Spaces** in some names (e.g., `"Transmission Type"`)
* Occasional **underscores** elsewhere

This matters because:

* Dot notation (`df.Transmission Type`) **doesn’t work** with spaces.
* Inconsistent casing and separators make code brittle and harder to search/grep.

In Pandas, `df.columns` is an **Index** (a label container similar to a `Series`) that supports vectorized string ops through `.str`. We’ll use that to apply the same cleanup everywhere at once.

**Normalize column names**:

```python
df.columns = (
    df.columns
      .str.lower()
      .str.replace(' ', '_', regex=False)
)
```

Now all column names are **lowercase\_with\_underscores**, which is predictable and safe to use in code.

---

## 4) Normalize text values (categorical columns)

The same inconsistency often appears in **values** inside string/categorical columns:

* Some makes may be `"BMW"` while others are `"Bmw"` or `"bmw"`.
* Spaces vs underscores, etc.

First, identify which columns are text. When CSVs are read, text columns usually appear with dtype **`object`**.

```python
df.dtypes  # quick scan of types
```

Extract just the string columns. Two equivalent approaches:

**A. With `select_dtypes` (cleanest):**

```python
string_cols = df.select_dtypes(include=['object']).columns.tolist()
```

**B. With a dtype comparison (matches the source’s approach):**

```python
string_cols = df.dtypes[df.dtypes == 'object'].index.tolist()
```

Now apply a consistent transformation to **every** string column:

```python
for col in string_cols:
    df[col] = (
        df[col]
          .str.lower()
          .str.replace(' ', '_', regex=False)
    )
```

At this point:

* All **column names** are lowercase\_with\_underscores.
* All **string values** are normalized the same way.

This makes downstream encoding, grouping, and analysis much less error-prone.

---

## 5) Quick verification

It’s worth re-checking the top rows and a couple of columns after cleaning:

```python
df.head()
df[string_cols].nunique().sort_values(ascending=False).head(10)
```

* `head()` confirms the text normalization looks right.
* `nunique()` helps spot **suspicious duplicates** caused by casing/spacing before cleaning (e.g., `"front_wheel_drive"` vs `"Front Wheel Drive"` now unified).

---

## 6) Notes and common pitfalls

* **Dot vs bracket access**: After normalization you *can* use `df.transmission_type`, but **prefer** `df['transmission_type']` in production notebooks to avoid clashes with DataFrame attributes.
* **Non-string objects**: `object` columns can sometimes hold non-string values (e.g., mixed types or `NaN`). If you hit errors like “Can only use .str accessor with string values”, ensure you have strings:

  ```python
  df[col] = df[col].astype('string').str.lower().str.replace(' ', '_', regex=False)
  ```
* **Underscore collisions**: Replacing spaces with underscores can produce identical labels if the raw data had near-duplicates. Use `nunique()` and `value_counts()` to audit high-cardinality columns.

---

## 7) What’s next

With a **clean, consistent** DataFrame, we’re set up for the next steps:

1. **Exploratory Data Analysis (EDA)**

   * Inspect distributions (e.g., MSRP, horsepower, engine size)
   * Check missing values and outliers
   * Understand relationships between features and price

2. **Train a baseline model (Linear Regression)**

   * Split into train/validation sets
   * Fit the model and compute **RMSE**
   * Establish a benchmark for later improvements

3. **Feature engineering**

   * Derive useful features (e.g., car age from year)
   * Consolidate rare categories

We’ll start with EDA and a careful train/validation split in the next lesson.
