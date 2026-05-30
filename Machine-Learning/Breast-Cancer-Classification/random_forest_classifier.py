import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#------------------------------------------------------------------------------------
# Step 1 : Load Dataset
#------------------------------------------------------------------------------------

def load_dataset(path):
    try:
        df = pd.read_csv(path)
        print("Shape of Dataset : ", df.shape)
        print("First Five Records : \n", df.head())
        return df
    except FileNotFoundError:
        print(f"Error : File not found at {path}")
        return None

#------------------------------------------------------------------------------------
# Step 2 : Separate Features and Labels
#------------------------------------------------------------------------------------

def separate_features_labels(df, target_column):
    X = df.drop(target_column, axis=1)
    Y = df[target_column]
    print("Shape of Features (X) : ", X.shape)
    print("Shape of Labels   (Y) : ", Y.shape)
    return X, Y

#------------------------------------------------------------------------------------
# Step 3 : Split Data for Training and Testing
#------------------------------------------------------------------------------------

def split_data(X, Y, test_size=0.2, random_state=42):
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=test_size, random_state=random_state
    )
    print("X_train shape : ", X_train.shape)
    print("X_test  shape : ", X_test.shape)
    print("Y_train shape : ", Y_train.shape)
    print("Y_test  shape : ", Y_test.shape)
    return X_train, X_test, Y_train, Y_test

#------------------------------------------------------------------------------------
# Step 4 : Create Random Forest Model
#------------------------------------------------------------------------------------

def create_model(n_estimators=200, max_depth=10, random_state=42):
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state
    )
    print(f"Model Created : RandomForestClassifier(n_estimators={n_estimators}, max_depth={max_depth})")
    return model

#------------------------------------------------------------------------------------
# Step 5 : Train Model
#------------------------------------------------------------------------------------

def train_model(model, X_train, Y_train):
    model.fit(X_train, Y_train)
    print("Model Training Complete.")
    return model

#------------------------------------------------------------------------------------
# Step 6 : Predict
#------------------------------------------------------------------------------------

def predict(model, X_test):
    Y_pred = model.predict(X_test)
    return Y_pred

#------------------------------------------------------------------------------------
# Step 7 : Evaluate Model
#------------------------------------------------------------------------------------

def evaluate_model(Y_test, Y_pred):
    accuracy = accuracy_score(Y_test, Y_pred)
    report   = classification_report(Y_test, Y_pred)
    matrix   = confusion_matrix(Y_test, Y_pred)

    print("Random Forest Accuracy   : ", accuracy)
    print("\nClassification Report  : \n", report)
    print("Confusion Matrix         : \n", matrix)

    return accuracy, report, matrix

#------------------------------------------------------------------------------------
# Step 8 : Plot Confusion Matrix
#------------------------------------------------------------------------------------

def plot_confusion_matrix(matrix, save_path="Screenshots/Confusion_Matrix_Random_Forest.png"):
    plt.figure(figsize=(6, 5))
    sns.heatmap(matrix, annot=True, fmt='d', cmap='Blues',
                xticklabels=["Benign", "Malignant"],
                yticklabels=["Benign", "Malignant"])
    plt.xlabel("Predicted Label")
    plt.ylabel("Actual Label")
    plt.title("Confusion Matrix — Random Forest")
    plt.tight_layout()
    plt.show()

#------------------------------------------------------------------------------------
# Step 9 : Plot Feature Importance
#------------------------------------------------------------------------------------

def plot_feature_importance(model, feature_names, top_n=10,):
    importances  = model.feature_importances_
    indices      = np.argsort(importances)[::-1][:top_n]
    top_features = [feature_names[i] for i in indices]
    top_values   = importances[indices]

    plt.figure(figsize=(10, 6))
    plt.bar(top_features, top_values, color='steelblue')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Feature")
    plt.ylabel("Importance Score")
    plt.title(f"Top {top_n} Feature Importances — Random Forest")
    plt.tight_layout()
    plt.show()

#------------------------------------------------------------------------------------
# Main Function
#------------------------------------------------------------------------------------

def main():

    # Load Dataset
    df = load_dataset("Dataset/breast_cancer.csv")
    if df is None:
        return

    # Separate Features and Labels
    X, Y = separate_features_labels(df, target_column="target")

    # Split Data
    X_train, X_test, Y_train, Y_test = split_data(X, Y)

    # Create Model
    RF_Model = create_model(n_estimators=200, max_depth=10)

    # Train Model
    RF_Model = train_model(RF_Model, X_train, Y_train)

    # Predict
    Y_pred = predict(RF_Model, X_test)

    # Evaluate
    accuracy, report, matrix = evaluate_model(Y_test, Y_pred)

    # Plot Confusion Matrix
    plot_confusion_matrix(matrix)

    # Plot Feature Importance
    plot_feature_importance(RF_Model, list(X.columns))


if __name__ == "__main__":
    main()