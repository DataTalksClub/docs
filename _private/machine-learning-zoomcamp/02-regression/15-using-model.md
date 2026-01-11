---
title: "15. Using Model"
parent: "Module 2: Machine Learning for Regression"
nav_order: 15
---

# Train the final model and use it to price a single car

<iframe width="560" height="315" src="https://www.youtube.com/embed/KT--uIJozes" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


Alright, we picked our best regularization strength (λ) on the validation set. Now we’ll (1) retrain **once** on all the data we’re allowed to learn from (train + validation), (2) evaluate on the **held-out test** set, and (3) show how to price an individual car from a plain Python dict.

---

## 1) Why retrain on **train + validation**?

During tuning we only fit on the train split to keep validation “clean” for selection. Once λ is chosen, we can safely fold validation back in to squeeze a bit more signal out of the data. The test set stays untouched until the very end for a single, honest report.

---

## 2) Build the full training set

* **Concatenate** train and validation dataframes:

  ```python
  df_full_train = pd.concat([df_train, df_val], axis=0).reset_index(drop=True)
  ```
* **Targets**: If you already have `y_train` and `y_val` as `np.log1p(msrp)`, just concatenate:

  ```python
  y_full_train = np.concatenate([y_train, y_val])
  ```

> Tip: keep the **same feature prep pipeline** you used before. Don’t silently change anything between splits.

---

## 3) Prepare features with the *same vocabulary*

Your `prepare_x(df)` should do exactly what it did during tuning:

* numeric features (+ the **car age** feature),
* chosen categorical one-hots (e.g., top-K per category),
* fill NA (you used zeros earlier),
* keep **column order** consistent.

If your `prepare_x` currently *discovers* top-K categories from whatever df you pass, freeze that list **from training data** and reuse it for validation/test:

```python
# One-time, from df_full_train
categories = build_category_vocab(df_full_train, k=5)  # dict: feature -> list of top values

X_full = prepare_x(df_full_train, categories)  # uses the frozen vocab
```

Prepare the test matrix with the same vocab:

```python
X_test = prepare_x(df_test, categories)
```

> If a test value isn’t in the top-K, all its one-hots will be 0 for that feature group (or map to an explicit “other” flag if you added one).

---

## 4) Train Ridge (regularized linear regression) with the chosen λ

We’ll use the normal equation with diagonal shrinkage (Ridge) and **no penalty on the intercept** (i.e., the first diagonal element is 0, others are 1):

```python
w0, w = train_linear_regression_reg(X_full, y_full_train, r=best_lambda)
```

Where `train_linear_regression_reg` implements:

$$
w = \big(X^\top X + \lambda D\big)^{-1} X^\top y
$$

with $D=\text{diag}(0,1,1,\dots,1)$.

---

## 5) Final evaluation on the **test** set

Predict on X\_test, compute RMSE in log space (same as you tuned):

```python
y_pred_val = X_test.dot(w) + w0
rmse_log = rmse(y_test, y_pred_val)
```

Optionally also report RMSE in **dollars** (invert the log1p):

```python
rmse_dollars = np.sqrt(np.mean((np.expm1(y_test) - np.expm1(y_pred_val))**2))
```

You should see test RMSE close to your validation RMSE (small drift is normal). If it’s much worse, suspect data leakage or a mismatch in feature prep.

---

## 6) Use the model to price a **single** car

Imagine your app posts a JSON payload; you’ll get a plain dict like:

```python
car = {
  "make": "toyota",
  "model": "sienna",
  "year": 2016,
  "engine_hp": 266,
  "engine_cylinders": 6,
  "transmission_type": "automatic",
  "driven_wheels": "front_wheel_drive",
  "number_of_doors": 4,
  "market_category": "minivan,performance",
  "vehicle_size": "midsize",
  "vehicle_style": "van",
  "highway_mpg": 25,
  "city_mpg": 18,
  "popularity": 2031
}
```

Turn it into a 1-row dataframe, prepare features, predict log-price, and convert back:

```python
df_one = pd.DataFrame([car])
X_one  = prepare_x(df_one, categories)          # same vocab!
y_log  = X_one.dot(w) + w0
price  = float(np.expm1(y_log))                 # dollars

# Optional: nice formatting
price_rounded = int(np.round(price, -2))        # e.g., nearest $100
```

To sanity-check, compare against the true MSRP for that row in your test set; being off by a few thousand dollars is typical for a simple linear baseline.

---

## 7) Save everything you need to **serve** the model

When you deploy, you must recreate the exact feature vector:

* `w0` (intercept) and `w` (weights)
* the **feature order** your model expects
* the **category vocabulary** (`categories` dict)
* any constants used in feature engineering (e.g., the **reference year** `2017` for `age`)
* NA fill rules (you used zeros)

A simple way:

```python
np.savez("car_price_model.npz", w0=w0, w=w)
with open("car_price_features.json", "w") as f:
    json.dump({"categories": categories,
               "numeric_features": base_numeric_feature_list,
               "reference_year": 2017}, f)
```

At inference time, load artifacts, run `prepare_x` with the frozen vocab, then `price = expm1(X.dot(w)+w0)`.

---

## 8) Quick diagnostics (nice to do once)

* **Histogram** of `y_pred` vs `y_test` (in log space) — shapes should be similar.
* **Residuals vs. prediction** — look for patterns (curvature hints at missing nonlinearity).
* **Segmented error** — e.g., RMSE by vehicle size or age decile to spot pockets of weakness.

---

## What “good” looks like here

* Test RMSE close to validation RMSE → **generalization** looks healthy.
* Individual prediction within a few thousand dollars → solid for a linear baseline.
* Clean, reproducible pipeline → easy to iterate (add features, try different K for top categories, etc.).

That’s it: you’ve trained the **final** Ridge model on full train data, verified it on test, and wired it to predict a single car’s price. Next natural steps would be feature upgrades (e.g., richer categorical coverage, interaction terms) or trying tree-based models to capture nonlinearity.
