---
title: "08. Linear Algebra"
parent: "Module 01: Intro"
nav_order: 8
---

# Linear Algebra Refresher

> These notes are based on the video [ML Zoomcamp 1.8 - Linear Algebra Refresher](https://youtu.be/zZyKUeOR4Gg?si=4sy0F77OZCvTq7nc)

<iframe width="560" height="315" src="https://www.youtube.com/embed/zZyKUeOR4Gg?si=4sy0F77OZCvTq7nc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

This lesson covers fundamental linear algebra operations that are essential for understanding machine learning algorithms. We'll explore vector operations, matrix-vector multiplication, matrix-matrix multiplication, and special matrices.

## Vector Operations

### Vector Notation
In linear algebra, vectors are typically represented as columns, unlike NumPy where they're represented as rows by default. This is just a convention in mathematical notation.

### Vector Multiplication by Scalar
When multiplying a vector by a scalar (a number), each element of the vector is multiplied by that scalar:

If we multiply vector [2, 4, 5, 6] by 2, we get [4, 8, 10, 12].

### Vector Addition
To add two vectors, we add their corresponding elements:

Vector u: [2, 4, 5, 6]  
Vector v: [1, 0, 0, 2]  
u + v = [3, 4, 5, 8]

## Vector-Vector Multiplication (Dot Product)

The dot product (also called inner product) between two vectors produces a single number. It's calculated by:
1. Multiplying corresponding elements of the two vectors
2. Summing all these products

For vectors u = [2, 4, 5, 6] and v = [1, 0, 0, 2]:
- u · v = (2×1) + (4×0) + (5×0) + (6×2) = 2 + 0 + 0 + 12 = 14

The formula for dot product is:
u · v = Σ(u_i × v_i) from i=1 to n

In linear algebra notation, this is written as u^T v (where u^T is the transpose of u, turning a column vector into a row vector).

In NumPy, we can calculate the dot product using the `np.dot()` function:
```python
np.dot(u, v)  # Returns 14
```

## Matrix-Vector Multiplication

To multiply a matrix U by a vector v:
1. Take each row of the matrix
2. Calculate the dot product of that row with the vector
3. The results form a new vector

For example, if U is a 3×4 matrix and v is a vector with 4 elements:
- The result will be a vector with 3 elements
- Each element is the dot product of a row from U with vector v

In code:
```python
def matrix_vector_multiplication(U, v):
    # Check dimensions match
    assert U.shape[1] == v.shape[0]
    
    num_rows = U.shape[0]
    result = np.zeros(num_rows)
    
    for i in range(num_rows):
        result[i] = np.dot(U[i], v)
    
    return result
```

In NumPy, we can simply use:
```python
np.dot(U, v)
```

## Matrix-Matrix Multiplication

Matrix-matrix multiplication can be viewed as a series of matrix-vector multiplications:
1. Break the second matrix V into columns
2. Multiply the first matrix U by each column of V
3. The results form the columns of the new matrix

For matrices U and V, the result will have:
- Number of rows from U
- Number of columns from V

In code:
```python
def matrix_matrix_multiplication(U, V):
    # Check dimensions match
    assert U.shape[1] == V.shape[0]
    
    result = np.zeros((U.shape[0], V.shape[1]))
    
    for i in range(V.shape[1]):
        result[:, i] = np.dot(U, V[:, i])
    
    return result
```

In NumPy, we can simply use:
```python
np.dot(U, V)
```

## Special Matrices

### Identity Matrix

The identity matrix (I) is a square matrix with:
- 1's on the diagonal
- 0's everywhere else

It has a special property: for any matrix U, U × I = I × U = U

It works like the number 1 in scalar multiplication.

In NumPy, we can create an identity matrix using:
```python
np.eye(3)  # Creates a 3×3 identity matrix
```

### Matrix Inverse

For a square matrix A, its inverse (A⁻¹) is a matrix such that:
A × A⁻¹ = A⁻¹ × A = I

Not all matrices have inverses. Only square matrices can have inverses, and even then, some don't.

In NumPy, we can compute the inverse using:
```python
import numpy.linalg as LA
A_inverse = LA.inv(A)
```

Matrix inverses are particularly useful in linear regression, which we'll explore in future lessons.

## Summary

These linear algebra operations form the foundation for many machine learning algorithms:
- Vector operations (scalar multiplication, addition)
- Dot products
- Matrix-vector multiplication
- Matrix-matrix multiplication
- Identity matrices and matrix inverses

In the next lesson, we'll explore Pandas, a library for manipulating tabular data in Python.
