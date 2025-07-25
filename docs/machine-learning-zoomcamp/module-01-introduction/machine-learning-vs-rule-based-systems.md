---
title: "Machine Learning vs Rule-Based Systems: What is the Difference?"
parent: "Module 1: Introduction to Machine Learning"
nav_order: 2
---

# Machine Learning vs Rule-Based Systems: What is the Difference?

> These notes are based on the video [ML Zoomcamp 1.2 - ML vs Rule-Based Systems](https://youtu.be/CeukwyUdaz8?si=Hd70BRJsMabLZM6F)

<iframe width="560" height="315" src="https://www.youtube.com/embed/CeukwyUdaz8?si=Hd70BRJsMabLZM6F" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Spam Detection Example

To understand the fundamental differences between rule-based systems and machine learning approaches, let's explore a practical example: email spam detection.

### The Problem

Imagine you're running an email service like Gmail or Outlook. Your users are increasingly complaining about receiving:
- Unsolicited promotional emails
- Fraudulent messages attempting to scam them

Your goal is to develop a system that can automatically identify these unwanted messages and filter them into a spam folder, keeping users' inboxes clean and safe.

### Rule-Based Systems Approach

A rule-based approach tackles this problem by encoding explicit patterns that human experts identify in spam messages.

#### How Rule-Based Systems Work:

1. **Pattern Identification**: Analyze existing spam messages to find common characteristics
   - Example patterns:
     - Emails from specific senders (e.g., "promotions@online.com")
     - Subject lines containing suspicious phrases (e.g., "tax review")
     - Emails from certain domains (e.g., "online.com")

2. **Rule Creation**: Convert these patterns into explicit rules
   - Rule 1: `IF sender = "promotions@online.com" THEN mark_as_spam()`
   - Rule 2: `IF subject_contains("tax review") AND sender_domain = "online.com" THEN mark_as_spam()`

3. **Implementation**: Write code that applies these rules to incoming emails
   ```python
   def is_spam(email):
       if email.sender == "promotions@online.com":
           return True
       if "tax review" in email.subject and email.sender_domain == "online.com":
           return True
       return False
   ```

4. **Deployment**: Apply these rules to filter incoming emails

#### The Evolution Problem

Initially, this system works well. But soon:

1. **New Spam Patterns Emerge**: Spammers adapt their tactics
   - Example: New fraudulent emails about "deposits" and money transfers appear

2. **Rule Updates**: You analyze these new spam messages and add another rule
   ```python
   def is_spam(email):
       # Previous rules remain
       if "deposit" in email.body:
           return True
       return False
   ```

3. **False Positives**: A legitimate email containing "deposit" (e.g., "I paid the deposit for the apartment") gets incorrectly marked as spam

4. **Rule Refinement**: You need to make the rule more specific
   ```python
   def is_spam(email):
       # Previous rules remain
       if "deposit" in email.body and ("transfer" in email.body or "fee" in email.body):
           return True
       return False
   ```

#### The Maintenance Nightmare

Over time, this approach becomes increasingly problematic:

1. **Endless Updates**: Spam tactics constantly evolve, requiring continuous rule updates
2. **Growing Complexity**: Rules need more exceptions and conditions
3. **Code Bloat**: The system becomes a tangled web of if-else statements
4. **Maintenance Burden**: Changing one rule might break others
5. **Diminishing Returns**: Despite more rules, effectiveness plateaus or declines

### Machine Learning Approach

Machine learning offers a fundamentally different approach to the same problem.

#### How Machine Learning Systems Work:

1. **Data Collection**: Instead of manually identifying patterns, gather examples
   - Collect thousands of emails that users have already marked as "spam" or "not spam"
   - This labeled dataset becomes your training material

2. **Feature Extraction**: Convert emails into measurable characteristics (features)
   - **Text-based features**:
     - Email length (title, body)
     - Presence of specific words ("deposit", "urgent", "money")
     - Ratio of uppercase letters
     - Number of exclamation marks
   - **Metadata features**:
     - Sender information
     - Time of day sent
     - Whether sender is in contacts

3. **Feature Representation**: Transform each email into a numerical format
   
   For example, a simple binary feature set might look like:
   
   | Feature | Description | Value (1=Yes, 0=No) |
   |---------|-------------|---------------------|
   | F1 | Title length > 10 characters | 1 |
   | F2 | Body length > 1000 characters | 1 |
   | F3 | Sender is "promotions@online.com" | 0 |
   | F4 | Sender domain is "online.com" | 1 |
   | F5 | Body contains "deposit" | 1 |
   | F6 | Contains multiple exclamation marks | 0 |
   
   Each email is now represented as a vector: [1, 1, 0, 1, 1, 0]

4. **Model Training**: Feed these feature vectors and their corresponding labels (spam=1, not spam=0) into a machine learning algorithm
   - The algorithm analyzes thousands of examples
   - It automatically discovers patterns that distinguish spam from legitimate emails
   - It creates a mathematical model that captures these patterns

5. **Model Output**: Instead of binary yes/no decisions, the model produces probability scores
   - Example: Email A has 80% probability of being spam
   - Example: Email B has 10% probability of being spam

6. **Decision Making**: Apply a threshold to convert probabilities to decisions
   - Common threshold: If probability ≥ 50%, classify as spam
   - This threshold can be adjusted based on tolerance for false positives

### Key Differences: Rule-Based vs. Machine Learning

This example highlights fundamental differences in how these approaches work:

#### 1. Knowledge Representation

- **Rule-Based**: Knowledge is explicitly encoded by humans in IF-THEN rules
- **Machine Learning**: Knowledge is implicitly encoded in model parameters learned from data

#### 2. System Development

- **Rule-Based**: 
  - Start with empty ruleset
  - Human experts identify patterns
  - Engineers code these patterns as rules
  - System applies rules to make decisions

- **Machine Learning**:
  - Start with labeled examples (data)
  - Algorithm discovers patterns automatically
  - System learns a mathematical model
  - Model applies learned patterns to make predictions

#### 3. Input/Output Flow

- **Rule-Based**:
  - Input: Rules (code) + New data
  - Output: Decisions (spam/not spam)

- **Machine Learning**:
  - Training phase:
    - Input: Historical data + Labels
    - Output: Trained model
  - Prediction phase:
    - Input: Model + New data
    - Output: Predictions (probabilities)

#### 4. Adaptability

- **Rule-Based**: Must be manually updated when new patterns emerge
- **Machine Learning**: Can be retrained on new data to adapt automatically

#### 5. Explainability

- **Rule-Based**: Rules are explicit and easy to understand
- **Machine Learning**: Decision process may be complex and less transparent

### Advantages of Machine Learning for Spam Detection

1. **Scalability**: Can process millions of emails and thousands of features
2. **Adaptability**: Can learn new spam patterns without explicit reprogramming
3. **Nuance**: Can identify subtle patterns humans might miss
4. **Probabilistic output**: Provides confidence levels, not just binary decisions
5. **Maintenance**: Easier to update (retrain) than rewriting complex rule systems

### Practical Implementation

In practice, modern spam filters often use a hybrid approach:
- Some explicit rules for obvious cases (known malicious senders)
- Machine learning for the majority of classification decisions
- User feedback to continuously improve the system

## Next Steps

In the next lesson, we'll explore supervised learning in more detail, examining different types such as regression, classification, and ranking. The spam detection example we've just covered is a classic case of binary classification, one of the fundamental supervised learning tasks.

## Glossary

- Classifier: A system or algorithm that categorizes input into one of several classes (e.g., spam/not spam).
- Features: Measurable characteristics or attributes of the data used by the model (e.g., email length, sender domain).
- Target Variable: The variable that the model is trying to predict or classify (e.g., whether an email is spam or not).
- Training/Fitting: The process of feeding data to a machine learning algorithm so it can learn patterns and create a model.
- Model: The output of the training process; a learned representation that can make predictions on new data.
- Probability: The likelihood of an event occurring, often output by ML models before a final classification decision.
- Decision Threshold: A predefined value used to convert a model's probability output into a definitive classification (e.g., >0.5 means spam).
- Supervised Learning: A type of machine learning where the model learns from labeled data (inputs with known correct outputs). Spam detection and car price prediction are examples.

## Quiz
<details>
<summary>What is the fundamental difference between rule-based systems and machine learning systems for tasks like spam detection?</summary>
Rule-based systems involve manually defining a set of explicit rules (e.g., "if sender is promotions@online.com, then it's spam"). These rules are hard-coded into the software. In contrast, machine learning systems learn patterns from data. Instead of programmers writing rules, the system is fed data (emails labeled as spam or not spam), and a machine learning algorithm creates a "model" that can then predict whether new emails are spam.
</details>

<details>
<summary>Why do rule-based systems become difficult to maintain over time, especially for dynamic problems like spam detection?</summary>
Rule-based systems struggle with dynamic problems because the rules need constant updating as the nature of the problem changes (e.g., spammers evolve their tactics). Old rules may stop working, and new ones need to be added. This leads to an ever-growing, complex codebase that is difficult to maintain, prone to breakage when changes are made, and ultimately becomes a "nightmare" for developers.
</details>

<details>
<summary>What are "features" in the context of a machine learning system for spam detection, and how are they derived?</summary>
Features are characteristics or attributes extracted from the data that the machine learning model can use to make predictions. For spam detection, features could include: the length of the email title, the length of the body, the sender's domain, or the presence of specific keywords (like "deposit"). Often, these features are derived from the rules that were initially used in a rule-based system, as these rules often highlight relevant patterns.
</details>

<details>
<summary>How does a machine learning system "learn" to classify emails as spam or not spam?</summary>
A machine learning system learns by being trained on a dataset of examples. For spam detection, this involves collecting emails that have been explicitly labeled by users as "spam" or "not spam." From each email, relevant features are extracted and paired with its corresponding label. This "labeled data" (features + target variable) is then fed into a machine learning algorithm, which "fits" or "trains" a model. This trained model can then make predictions on new, unlabeled emails.
</details>

<details>
<summary>What is the role of "probabilities" in the output of a machine learning model for classification?</summary>
A machine learning model, particularly for classification tasks like spam detection, often outputs a probability rather than a definitive "yes" or "no." For example, it might predict an email has an 80% probability of being spam. This probability represents the model's confidence level. A threshold (e.g., 0.5 or 50%) is then typically applied to these probabilities to make a final decision: if the probability is above the threshold, it's classified as spam; otherwise, it's considered legitimate.
</details>

<details>
<summary>How does the workflow of creating a prediction system differ between a rule-based approach and a machine learning approach?</summary>
In a rule-based system, you typically have existing data and you manually derive and hard-code rules (code) to produce an outcome (predictions). So, it's Data + Code -> Predictions. In a machine learning system, the "outcome" itself (the labels like spam/not spam) is an input along with the data. You feed the data and known outcomes into a machine learning algorithm to produce a "model." This model then takes new, unlabeled data to make predictions. So, it's Data + Outcome -> Model, and then Data + Model -> Predictions.
</details>  

<details>
<summary>Why is it often recommended to start with a rule-based system before transitioning to machine learning?</summary>
Starting with a rule-based system can be a good initial step because it helps in understanding the problem and identifying key patterns. The rules developed during this phase can then be directly used as features for the machine learning system, providing a strong foundation and leveraging the initial analysis. This approach allows for a gradual transition and ensures that valuable insights gained from manual rule creation are not lost.
</details>

<details>
<summary>What is "supervised learning," and how do the car price prediction and spam detection examples fit into this category?</summary>
Supervised learning is a type of machine learning where the algorithm learns from "labeled" data, meaning the input data is paired with the correct output or "target variable." Both the car price prediction and spam detection examples are instances of supervised learning. In car price prediction, the input features (car characteristics) are paired with the actual car prices. In spam detection, email features are paired with labels indicating whether the email is spam or not. The system learns the relationship between the inputs and the known outputs to make future predictions.