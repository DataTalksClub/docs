---
title: "9. Introduction to Pandas"
parent: "Module 1: Introduction to Machine Learning"
nav_order: 9
---
# Introduction to Pandas

> These notes are based on the video [ML Zoomcamp 1.9 - Introduction to Pandas](https://youtu.be/0j3XK5PsnxA?si=cIOKp_VevAvqGMrQ)

<iframe width="560" height="315" src="https://www.youtube.com/embed/0j3XK5PsnxA?si=cIOKp_VevAvqGMrQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Pandas is a Python library for manipulating tabular data. It provides powerful data structures and operations for working with structured data efficiently.

## Importing Pandas

```python
import pandas as pd  # Standard convention is to use 'pd' as the alias
```

## DataFrames

The main data structure in pandas is the DataFrame, which represents tabular data (similar to a spreadsheet or SQL table).

### Creating DataFrames

There are multiple ways to create a DataFrame:

1. **From a list of lists (rows)**:
```python
data = [
    ['Toyota', 'Corolla', 2015, 130, 4, 'manual', 'sedan', 18000],
    ['Ford', 'Focus', 2018, 140, 4, 'automatic', 'sedan', 23000],
    ['Nissan', 'Sentra', 2020, 149, 4, 'manual', 'sedan', 22000],
    ['Nissan', 'Altima', 2014, None, 6, 'automatic', 'coupe', 16000],
    ['Toyota', 'Camry', 2019, 160, 4, 'automatic', 'sedan', 25000]
]
columns = ['make', 'model', 'year', 'engine_hp', 'engine_cylinders', 
           'transmission_type', 'vehicle_style', 'msrp']

df = pd.DataFrame(data, columns=columns)
```

2. **From a list of dictionaries**:
```python
data_dict = [
    {'make': 'Toyota', 'model': 'Corolla', 'year': 2015, 'msrp': 18000},
    {'make': 'Ford', 'model': 'Focus', 'year': 2018, 'msrp': 23000},
    # ... more dictionaries for each row
]

df = pd.DataFrame(data_dict)
```

### Inspecting DataFrames

After creating or loading a DataFrame, it's common to inspect the first few rows:

```python
df.head()       # Returns first 5 rows by default
df.head(2)      # Returns first 2 rows
```

## Series

Each column in a DataFrame is a Series object. A Series is a one-dimensional labeled array.

### Accessing Series (Columns)

There are two ways to access columns:

1. **Dot notation** (only works for column names without spaces or special characters):
```python
df.make          # Returns the 'make' column as a Series
```

2. **Bracket notation** (works for all column names):
```python
df['make']       # Returns the 'make' column as a Series
df['vehicle_style']  # For column names with spaces, must use brackets
```

### Accessing Multiple Columns

To get a subset of columns:
```python
df[['make', 'model', 'msrp']]  # Returns a DataFrame with only these columns
```

### Adding and Modifying Columns

```python
# Add a new column
df['id'] = [1, 2, 3, 4, 5]

# Modify an existing column
df['id'] = [10, 20, 30, 40, 50]

# Delete a column
del df['id']
```

## Indexing

DataFrames have an index that labels each row. By default, it's a sequential range starting from 0.

```python
df.index  # View the current index
```

### Accessing Rows by Index

1. **Using `loc` - label-based indexing**:
```python
df.loc[1]        # Returns row with index 1
df.loc[[1, 2]]   # Returns rows with indices 1 and 2
```

2. **Using `iloc` - position-based indexing**:
```python
df.iloc[1]       # Returns row at position 1 (second row)
df.iloc[[1, 2]]  # Returns rows at positions 1 and 2
```

### Changing the Index

```python
# Set a custom index
df.index = ['a', 'b', 'c', 'd', 'e']

# Reset the index to default sequential numbers
df = df.reset_index()  # Keeps old index as a column
df = df.reset_index(drop=True)  # Discards old index
```

## Element-wise Operations

Like NumPy arrays, pandas Series support element-wise operations:

```python
# Divide all values in a column by 100
df['engine_hp'] / 100

# Multiply by 2
df['engine_hp'] * 2
```

## Filtering

You can filter rows based on conditions:

```python
# Filter cars made after 2015
df[df['year'] > 2015]

# Filter Nissan cars
df[df['make'] == 'Nissan']

# Combine conditions (AND)
df[(df['make'] == 'Nissan') & (df['year'] > 2015)]
```

## String Operations

Pandas provides string methods through the `.str` accessor:

```python
# Convert to lowercase
df['vehicle_style'].str.lower()

# Replace spaces with underscores
df['vehicle_style'].str.replace(' ', '_')

# Chain string operations
df['vehicle_style'] = df['vehicle_style'].str.replace(' ', '_').str.lower()
```

## Summarizing Operations

Pandas offers various methods to summarize data:

```python
# Basic statistics for a column
df['msrp'].mean()
df['msrp'].max()
df['msrp'].min()

# Comprehensive summary statistics
df['msrp'].describe()

# Summary statistics for all numeric columns
df.describe()
df.describe().round(2)  # Round to 2 decimal places for readability
```

For categorical (string) columns:

```python
# Count unique values
df['make'].nunique()  # Returns number of unique makes

# Count unique values for all columns
df.nunique()
```

## Handling Missing Values

Pandas represents missing values as `NaN` (Not a Number):

```python
# Identify missing values (returns boolean DataFrame)
df.isnull()

# Count missing values per column
df.isnull().sum()
```

## Grouping

Similar to SQL's GROUP BY, pandas allows grouping and aggregation:

```python
# Group by transmission type and calculate mean price
df.groupby('transmission_type')['msrp'].mean()

# Calculate min and max prices by transmission type
df.groupby('transmission_type')['msrp'].min()
df.groupby('transmission_type')['msrp'].max()
```

## Converting Between Pandas and NumPy/Python

```python
# Get underlying NumPy array from a Series
numpy_array = df['msrp'].values

# Convert DataFrame to list of dictionaries
records = df.to_dict(orient='records')
```

This format is useful for saving data or passing it to other systems that expect Python dictionaries.
