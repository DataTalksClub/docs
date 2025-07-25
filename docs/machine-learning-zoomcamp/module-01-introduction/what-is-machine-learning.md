---
title: What is Machine Learning?
parent: "Module 1: Introduction to Machine Learning"
nav_order: 1
---

# What is Machine Learning?

> These notes are based on the video [ML Zoomcamp 1.1 - Introduction to Machine Learning](https://youtu.be/Crm_5n4mvmg?si=Nzk3bCedKOiwudCG)

<iframe width="560" height="315" src="https://www.youtube.com/embed/Crm_5n4mvmg?si=ScfgiUraIwp-qVSN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Machine learning is a process of identifying patterns in data through statistical and computational methods. This concept can be illustrated through a real-world problem that online platforms commonly encounter.

1-car-classifields.png

Imagine a user wants to sell their car on a classifieds website:
1. They upload pictures and details about their car
2. They reach the price field and pause - what should they charge?
3. Setting the right price creates a dilemma:
   - **Too high**: The car won't attract buyers
   - **Too low**: The seller loses potential profit

Currently, users solve this problem by manually researching similar listings - a tedious and time-consuming process that often leads to suboptimal pricing decisions.

2-user-price.png

## How Machine Learning Transforms This Process

As website owners, we can leverage machine learning to automate and improve this pricing decision. But how exactly does this work?

Every car in our database contains valuable information that influences its market value:

- **Age/Year of manufacture**: Newer cars generally command higher prices
- **Manufacturer**: Luxury brands (BMW, Mercedes) versus economy brands (Toyota, Honda)
- **Mileage**: Lower mileage typically means higher value
- **Model**: Popular or rare models affect pricing
- **Number of doors**: Practical considerations that buyers value
- **Additional specifications**: Engine size, features, condition, etc.

These characteristics are called **features** in machine learning terminology, they're the inputs our system will use to make predictions.

3-what-do-we-know-about-cars.png

### The Expert Knowledge

Car dealerships employ experts who can look at these features and estimate a fair market price. How? Through years of experience examining cars and their prices, they've:

1. Observed thousands of cars and their selling prices
2. Recognized patterns (older cars sell for less, luxury brands command premiums)
3. Internalized these relationships to make accurate estimates

If human experts can learn these patterns from data, so can computers - often more efficiently and consistently.

4-expert-model.png

## Machine Learning Models to Capture the Expert Knowledge

A machine learning model serves as our "digital expert" that can learn the same patterns from data, but at scale and with mathematical precision.

### The Core Components of a Machine Learning Model

1. **Features** (Inputs): All measurable car characteristics (age, manufacturer, mileage, etc.)
2. **Target** (Output): What we want to predict - the car's price
3. **Training Data**: Historical records of cars with known features AND prices

### Model Training Process

5-model-training.png

The model training process mimics how humans learn, but follows a more structured approach:

1. **Data Collection**: Gather information about thousands of cars that have already sold
2. **Data Organization**: Structure this information into a table where:
   - Each row represents a specific car
   - Each column represents either a feature or the target price
3. **Pattern Recognition**: Apply mathematical algorithms that identify relationships between features and prices
4. **Model Creation**: Encode these relationships into a mathematical model

This process transforms raw data into a model that can predict prices for new cars.

### From Model to Predictions

Once trained, our model becomes a powerful prediction tool:

1. A user enters their car's information (age, make, mileage, etc.)
2. These features are processed through the mathematical relationships our model learned
3. The model calculates an estimated price based on patterns in similar cars

While the prediction won't be perfect for every individual car (some cars have unique characteristics or market conditions), it provides a statistically sound starting point that's accurate on average for cars with similar features.

## The Complete Machine Learning Solution

Let's see how this transforms the user experience on our car classifieds website:

1. A user begins listing their car for sale
2. They enter all details about their vehicle (year, make, model, mileage, etc.)
3. Before they reach the "price" field, our system:
   - Extracts these details as features
   - Passes them to our trained model
   - Calculates an optimal suggested price
4. The user sees this suggested price when they reach the pricing step
5. They can accept this data-driven suggestion or adjust it based on their knowledge of the car's specific condition

This creates a win-win situation:
- Users save time and gain confidence in their pricing decisions
- The platform facilitates more successful transactions with fair market prices
- Buyers find reasonably priced vehicles

## Machine Learning: The Bigger Picture

What we've explored with car pricing illustrates the fundamental principles of machine learning that apply across countless applications:

### The Universal Machine Learning Framework

1. **Data Collection**: Gather examples with known outcomes (cars with known prices)
2. **Feature Engineering**: Identify and prepare the relevant information (car characteristics)
3. **Model Training**: Allow algorithms to discover patterns in the data
4. **Prediction**: Apply the model to new cases where the outcome is unknown

### The Power of Machine Learning

Machine learning excels because it:
- **Scales**: Can process millions of examples to find subtle patterns
- **Adapts**: Can be updated with new data as market conditions change
- **Generalizes**: Can make reasonable predictions for cases it hasn't seen before
- **Automates**: Reduces the need for manual analysis and expert intervention

## Next Steps

In the next lesson, we'll contrast machine learning with traditional rule-based systems through a spam detection example. This comparison will further illustrate why machine learning has become the preferred approach for many complex prediction problems in today's data-rich world.

## Glossary
- Features: All the known characteristics or pieces of information about an object that are used as input to a machine learning model to make a prediction. (e.g., car's age, manufacturer, mileage).
- Target: The specific variable or value that a machine learning model aims to predict. (e.g., the price of a car).
- Model: The output of the machine learning training process; it's an algorithm or system that has learned patterns from data and can be used to make predictions on new, unseen data.
- Prediction: The output generated by a trained machine learning model when it is given new input features, representing the model's estimate for the target variable.
- Machine Learning (ML): A process of extracting patterns and insights from data, allowing a system to learn and make predictions or decisions without being explicitly programmed for every specific outcome.
- Data: Raw facts, figures, or information collected for analysis. In machine learning, it refers to the collection of features and targets used for training and testing models.
- Patterns: Regular and discernible relationships or structures within data that machine learning algorithms identify and learn from.
- Rule-based Systems: Traditional programming approaches where a system makes decisions based on a predefined set of explicit rules, often contrasting with the pattern-learning approach of machine learning.
- Training: The process of feeding data (features and corresponding targets) to a machine learning algorithm so that it can learn the underlying patterns and create a model.

## Quiz

<details>
<summary>1. What is the fundamental concept of Machine Learning (ML)?</summary>
Machine Learning is essentially the process of extracting patterns from data. Instead of explicitly programming a computer with rules, you provide it with a dataset, and an ML model learns to identify relationships and trends within that data. This allows the model to make predictions or decisions on new, unseen data, replicating the kind of insights an expert might derive from the same information.
</details>

<details>
<summary>2. How can Machine Learning be applied in a practical scenario, such as predicting car prices?</summary>
In a car classifieds website scenario, ML can help users determine a fair selling price for their car. Instead of manually researching similar ads, a user can input various details about their car (features like age, manufacturer, mileage, model, number of doors). An ML model, trained on a large dataset of past car sales (with their corresponding features and prices), can then predict a suitable price. This automates a complex task and ensures the user doesn't price their car too high (leading to no sales) or too low (leaving money on the table).
</details>

<details>
<summary>3. What are "features" and "targets" in the context of Machine Learning?</summary>
In ML, "features" refer to all the input information or characteristics known about an object. For example, when predicting car prices, features would include the car's age, manufacturer, mileage, and model. The "target" is the specific outcome or value that the machine learning model aims to predict. In the car price prediction example, the target is the price of the car. The model learns the relationship between the features and the target from the training data.
</details>

<details>
<summary>4. How does a Machine Learning model learn from data?</summary>
A machine learning model learns by analyzing a dataset that contains both features and their corresponding target values. It identifies patterns, correlations, and relationships within this data. For instance, in car price prediction, the model learns that older cars with higher mileage tend to be cheaper, while certain manufacturers might command higher prices. This "learning" process allows the model to encapsulate these patterns, enabling it to make predictions on new data where only the features are known.
</details>

<details>
<summary>5. What is the output of a Machine Learning process?</summary>
The output of a machine learning process is a "model." This model is essentially a trained entity that has learned and stored the patterns extracted from the data. Once trained, this model can be used to make predictions on new, unseen data. In the car price example, the trained model would take new car features as input and output a predicted price.
</details>

<details>
<summary>6. How accurate are Machine Learning predictions?</summary>
Machine learning models, while powerful, may not always predict the exact value for a specific instance. However, their predictions are generally correct "on average." This means that for a car of a certain year, manufacturer, and mileage, the model's predicted price will be close to the typical cost of such a car. While a specific prediction might be slightly higher or lower, the overall accuracy tends to be reliable for practical applications.
</details>

<details>
<summary>7. Can you illustrate the complete workflow of using an ML model for car price prediction?</summary>
The workflow for car price prediction using ML involves several steps. First, historical data with car features (age, manufacturer, mileage, etc.) and their corresponding prices (the target) is collected. This data is then used to train an ML model. Once the model is trained, a user wanting to sell their car inputs their car's features into an application. These features are then fed into the trained ML model, which processes them and outputs a predicted price. This predicted price is then presented to the user, assisting them in setting an optimal selling price.
</details>

<details>
<summary>8. What is the distinction between a machine learning model and an expert's knowledge?</summary>
While an expert can determine a car's price based on their accumulated knowledge and experience from looking at many similar car sales, they fundamentally learn these patterns from data, much like a machine learning model. The key difference is that an expert learns implicitly over time, extracting patterns mentally, whereas a machine learning model explicitly takes a dataset and an algorithm to systematically extract these patterns. If an expert can do it, given sufficient data, a machine learning model can replicate that expertise by learning the same underlying patterns.
</details>


