# Breast Cancer Classification using Bagging Classifier

## Overview

This project focuses on classifying breast cancer tumors as benign or malignant using Machine Learning techniques.

A Bagging Classifier ensemble model is built using Decision Trees as the base estimator to improve prediction stability and classification performance.

The goal of this project is to demonstrate how Machine Learning can be applied to medical classification problems using diagnostic features.

---

## Problem Statement

Early detection of breast cancer plays an important role in improving treatment outcomes.

Healthcare datasets often contain multiple diagnostic measurements. Machine Learning models can analyze these measurements and classify whether a tumor is benign or malignant.

This project aims to answer the following question:

**Can breast cancer tumors be classified using machine learning techniques?**

---

## Dataset Information

The dataset contains diagnostic measurements collected from breast cancer cases.

### Target Variable

| Value | Meaning |
|---|---|
| 0 | Malignant |
| 1 | Benign |

### Features

The dataset contains multiple numerical medical measurements used for classification.

---

## Dataset Preview

![Dataset Preview](Screenshots/Dataset_Preview.png)

---

## Project Workflow

1. Data Loading
   - Load dataset using Pandas
   - Verify dataset integrity

2. Feature and Label Separation
   - Extract independent variables
   - Extract target variable

3. Train-Test Split
   - 80% Training Data
   - 20% Testing Data

4. Base Model Creation
   - Decision Tree Classifier

5. Ensemble Model Creation
   - Bagging Classifier
   - 10 Decision Tree estimators

6. Model Training
   - Train ensemble model using training dataset

7. Prediction
   - Predict tumor classification on unseen test data

8. Model Evaluation
   - Accuracy Score
   - Classification Report
   - Confusion Matrix

---

## Machine Learning Algorithms Used

### Decision Tree Classifier

A Decision Tree is used as the base learner for classification.

### Bagging Classifier

Bagging, also known as Bootstrap Aggregating, combines multiple Decision Trees trained on different subsets of data to improve model robustness and reduce overfitting.

---

## Technologies Used

- Python
- Pandas
- Scikit-Learn

---

## Project Structure

```text
Breast-Cancer-Classification/
│
├── Dataset/
│   └── breast_cancer.csv
│
├── Screenshots/
│   └── Dataset_Preview.png
│
├── breast_cancer_classification.py
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move to the project directory:

```bash
cd Breast-Cancer-Classification
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute the project using:

```bash
python3 breast_cancer_classification.py
```

---

## Model Performance

The Bagging Classifier achieved an accuracy of:

**95.61%**

This means the model correctly classified approximately 95.61% of the test data.

---

## Model Performance Screenshot

![Model Performance](Screenshots/Model_Performance.png)

---

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.95      0.93      0.94        43
           1       0.96      0.97      0.97        71

    accuracy                           0.96       114
   macro avg       0.96      0.95      0.95       114
weighted avg       0.96      0.96      0.96       114
```

---

## Confusion Matrix

```text
[[40  3]
 [ 2 69]]
```

### Confusion Matrix Interpretation

- 40 malignant cases were correctly classified as malignant
- 69 benign cases were correctly classified as benign
- 3 malignant cases were incorrectly classified as benign
- 2 benign cases were incorrectly classified as malignant

---

## Output Summary

The project generates:

- Dataset shape
- First five dataset records
- Bagging Classifier accuracy
- Classification report
- Confusion matrix

---

## Key Learning Outcomes

Through this project, I gained practical experience in:

- Classification Problems
- Ensemble Learning Techniques
- Decision Tree Classifier
- Bagging Classifier
- Train-Test Splitting
- Model Evaluation
- Confusion Matrix Analysis
- Healthcare Data Classification

---

## Future Improvements

- Random Forest Classifier
- Gradient Boosting
- XGBoost Classifier
- Hyperparameter Tuning
- Model Comparison Studies
- Web Deployment using Flask

---

## Author

**Atharva Deshmukh**

Python Developer | Machine Learning Enthusiast | Automation & AI Projects