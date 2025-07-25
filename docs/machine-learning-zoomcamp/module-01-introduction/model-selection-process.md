---
title: "Model Selection Process"
parent: "Module 1: Introduction to Machine Learning"
nav_order: 5
---

# Model Selection Process

> These notes are based on the video [ML Zoomcamp 1.5 - Model Selection Process](https://youtu.be/OH_R0Sl9neM?si=iPIPjPlkaqiahKpP)

<iframe width="560" height="315" src="https://www.youtube.com/embed/OH_R0Sl9neM?si=iPIPjPlkaqiahKpP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Model selection is a crucial step in the machine learning workflow where we evaluate different models to determine which one performs best for our specific problem. This process follows the data preparation step, where we've already extracted features from our raw data.

During the model selection phase, we:
- Try different model types (logistic regression, decision trees, neural networks, etc.)
- Evaluate their performance systematically
- Select the best performing model for deployment

## Simulating Real-World Performance

### The Challenge of Evaluation

When deploying a model in production, it will encounter new data it hasn't seen during training. For example:
- If we train a model in July using historical data
- And deploy it in August to classify new emails as spam or not spam
- We need to know how well it will perform on this unseen August data

### The Holdout Method

To simulate this real-world scenario, we use the holdout method:
1. Take our complete dataset
2. Set aside a portion (e.g., 20%) and "hide" it
3. Train our model only on the remaining data (e.g., 80%)
4. Evaluate the model on the hidden portion

This hidden portion is called the **validation dataset**, and it helps us estimate how well our model will perform on new, unseen data.

## Making and Evaluating Predictions

### The Prediction Process

1. From the training data, we extract:
   - Feature matrix X
   - Target variable y
   - Train our model g using X and y

2. From the validation data, we extract:
   - Feature matrix X_validation
   - Target variable y_validation (ground truth)

3. Apply our trained model g to X_validation to get predictions (y_hat)

4. Compare predictions (y_hat) with actual values (y_validation)

### Example: Spam Detection Evaluation

For a spam detection model that outputs probabilities:
- Predictions might be: 0.8, 0.7, 0.6, 0.1, 0.9, 0.6
- Actual values might be: 1, 0, 1, 0, 1, 0 (where 1=spam, 0=not spam)
- Using a threshold of 0.5, our predictions become: 1, 1, 1, 0, 1, 1
- Comparing with actual values: correct, incorrect, correct, correct, correct, incorrect
- Accuracy: 4 out of 6 = 66.7%

## Comparing Multiple Models

We can repeat this process for different model types:
- Logistic Regression: 66% accuracy
- Decision Tree: 60% accuracy
- Random Forest: 67% accuracy
- Neural Network: 80% accuracy

Based on these results, we would select the Neural Network as our best model.

## The Multiple Comparisons Problem

### A Cautionary Example

Consider a scenario where we use random coin flips to "predict" spam:
- Euro coin: 20% accuracy
- Dollar coin: 40% accuracy
- Polish zloty: 20% accuracy
- Russian ruble: 20% accuracy
- Ukrainian hryvnia: 100% accuracy

The Ukrainian hryvnia appears to be perfect, but this is purely by chance. It just happened to produce the exact sequence that matched our validation data.

This illustrates the **multiple comparisons problem**: when evaluating many models against the same validation dataset, one model might appear superior just by random chance, not because it truly captures the underlying patterns.

## The Train-Validation-Test Split

To guard against the multiple comparisons problem, we use a three-way data split:

1. **Training data** (60%): Used to train models
2. **Validation data** (20%): Used to compare different models
3. **Test data** (20%): Used only once to evaluate the final selected model

The process works as follows:
1. Split the dataset into three non-overlapping subsets
2. Hide the test data completely until the final step
3. Train models on the training data
4. Evaluate and compare models on the validation data
5. Select the best performing model
6. Evaluate the selected model on the test data to get an unbiased estimate of its performance

In our example:
- Neural network achieved 80% accuracy on validation data
- When applied to the test data, it achieved 79% accuracy
- This confirms the model is genuinely performing well, not just getting lucky on the validation set

## The Complete Model Selection Process

The model selection process can be summarized in six steps:

1. Split the dataset into training, validation, and test sets
2. Train different models on the training data
3. Validate models using the validation dataset
4. Repeat steps 2-3 for various model types
5. Select the best performing model based on validation results
6. Evaluate the best model on the test data for final performance assessment

## Optimizing the Final Model

After selecting the best model type, we can improve its performance by:
1. Combining the training and validation datasets (80% of original data)
2. Training a new model of the selected type on this combined dataset
3. Evaluating this final model on the test dataset

This approach allows us to use more data for the final model training while still maintaining an unbiased evaluation through the test set.
