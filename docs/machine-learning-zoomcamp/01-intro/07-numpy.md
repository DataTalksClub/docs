---
title: "07. Numpy"
parent: "Module 01: Intro"
nav_order: 7
---
# Introduction to NumPy

> These notes are based on the video [ML Zoomcamp 1.7 - Introduction to NumPy](https://youtu.be/Qa0-jYtRdbY?si=D7usABfuvCYqG7XD)

<iframe width="560" height="315" src="https://www.youtube.com/embed/Qa0-jYtRdbY?si=D7usABfuvCYqG7XD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

NumPy is a fundamental library for numerical computing in Python. This guide covers the essential NumPy operations you'll need throughout the machine learning course.

## Importing NumPy

The standard convention is to import NumPy with an alias:

```python
import numpy as np
```

This makes code more concise by allowing you to write `np` instead of `numpy`.

## Creating Arrays

### Basic Array Creation

NumPy provides several functions to create arrays:

- `np.zeros(10)`: Creates an array of 10 zeros
- `np.ones(10)`: Creates an array of 10 ones
- `np.full(10, 2.5)`: Creates an array of 10 elements, all with value 2.5

### From Python Lists

Convert a Python list to a NumPy array:

```python
a = np.array([1, 2, 3, 5, 7, 12])
```

### Accessing and Modifying Elements

Access elements using zero-based indexing:
```python
a[2]  # Returns the third element (3)
a[2] = 10  # Changes the third element to 10
```

### Range-Based Arrays

Create arrays with sequential values:
- `np.arange(10)`: Creates array with values 0 through 9
- `np.arange(3, 10)`: Creates array with values 3 through 9
- `np.linspace(0, 1, 11)`: Creates 11 evenly spaced values from 0 to 1 inclusive

## Multi-Dimensional Arrays

### Creating 2D Arrays

```python
# Create a 5×2 array of zeros
np.zeros((5, 2))

# Create from nested lists
n = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
```

### Accessing Elements in 2D Arrays

```python
n[0, 1]  # Access element at row 0, column 1 (value: 2)
n[0, 1] = 20  # Change this element to 20
```

### Accessing Rows and Columns

```python
n[0]  # Access the first row
n[2] = [1, 1, 1]  # Replace the last row with ones

n[:, 1]  # Access the second column (all rows, column 1)
n[:, 2] = [0, 1, 2]  # Replace the last column
```

## Randomly Generated Arrays

### Uniform Distribution

```python
# 5×2 array of random values between 0 and 1
np.random.random((5, 2))
```

### Setting Random Seed

Make random generation reproducible:

```python
np.random.seed(2)
np.random.random((5, 2))  # Will produce the same "random" values every time
```

### Normal Distribution

```python
# Random values from standard normal distribution
np.random.randn(5, 2)
```

### Random Integers

```python
# Random integers between 0 and 99
np.random.randint(0, 100, (5, 2))
```

## Element-Wise Operations

NumPy arrays support arithmetic operations that apply to each element:

```python
a = np.arange(5)  # [0, 1, 2, 3, 4]

a + 1  # [1, 2, 3, 4, 5]
a * 2  # [0, 2, 4, 6, 8]
a / 2  # [0, 0.5, 1, 1.5, 2]
```

Operations can be chained:
```python
a * 2 + 10  # [10, 12, 14, 16, 18]
(a * 2 + 10) ** 2  # [100, 144, 196, 256, 324]
```

### Operations Between Arrays

Element-wise operations work between arrays too:

```python
a = np.arange(5)  # [0, 1, 2, 3, 4]
b = np.array([10, 10, 10, 10, 10])

a + b  # [10, 11, 12, 13, 14]
a * b  # [0, 10, 20, 30, 40]
```

## Comparison Operations

Compare arrays element-wise:

```python
a >= 2  # [False, False, True, True, True]
a > b  # Element-wise comparison between arrays
```

Filter arrays using boolean masks:
```python
a[a > b]  # Returns elements of a where a > b is True
```

## Summarizing Operations

Reduce arrays to single values:

```python
np.min(a)  # Minimum value (0)
np.max(a)  # Maximum value (4)
np.sum(a)  # Sum of all elements (10)
np.mean(a)  # Mean value (2.0)
np.std(a)  # Standard deviation
```

These operations work on both 1D and 2D arrays.

NumPy offers many more functions for operations like finding minimums per row, sorting arrays, and matrix operations which will be covered in the linear algebra section.
