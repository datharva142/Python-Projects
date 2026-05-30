import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

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
# Step 4 : Create Gradient Boosting Model
#------------------------------------------------------------------------------------

def create_model(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42):
    model = GradientBoostingRegressor(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        max_depth=max_depth,
        random_state=random_state
    )
    print(f"Model Created : GradientBoostingRegressor(n_estimators={n_estimators}, learning_rate={learning_rate}, max_depth={max_depth})")
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
    mse  = mean_squared_error(Y_test, Y_pred)
    rmse = np.sqrt(mse)
    r2   = r2_score(Y_test, Y_pred)

    print("Mean Squared Error   : ", mse)
    print("Root Mean Sq. Error  : ", rmse)
    print("R2 Score             : ", r2)

    return mse, rmse, r2

#------------------------------------------------------------------------------------
# Step 8 : Plot Actual vs Predicted
#------------------------------------------------------------------------------------

def plot_actual_vs_predicted(Y_test, Y_pred, save_path="Screenshots/Actual_vs_Predicted.png"):
    plt.figure(figsize=(8, 5))
    plt.scatter(Y_test, Y_pred, alpha=0.5, color='steelblue')
    plt.plot([Y_test.min(), Y_test.max()],
             [Y_test.min(), Y_test.max()],
             color='red', linewidth=2, linestyle='--', label='Perfect Prediction')
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title("Actual vs Predicted Housing Prices — Gradient Boosting")
    plt.legend()
    plt.grid(True)
    plt.savefig(save_path)
    plt.show()

#------------------------------------------------------------------------------------
# Step 9 : Plot Feature Importance
#------------------------------------------------------------------------------------

def plot_feature_importance(model, feature_names, top_n=10, save_path="Screenshots/Feature_Importance.png"):
    importances  = model.feature_importances_
    indices      = np.argsort(importances)[::-1][:top_n]
    top_features = [feature_names[i] for i in indices]
    top_values   = importances[indices]

    plt.figure(figsize=(10, 6))
    plt.bar(top_features, top_values, color='steelblue')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Feature")
    plt.ylabel("Importance Score")
    plt.title(f"Top {top_n} Feature Importances — Gradient Boosting")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()

#------------------------------------------------------------------------------------
# Step 10 : Plot Learning Curve (n_estimators vs RMSE)
#------------------------------------------------------------------------------------

def plot_learning_curve(X_train, Y_train, X_test, Y_test, max_estimators=100, save_path="Screenshots/Learning_Curve.png"):
    train_errors = []
    test_errors  = []
    estimator_range = range(1, max_estimators + 1)

    model = GradientBoostingRegressor(
        n_estimators=max_estimators,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )
    model.fit(X_train, Y_train)

    # staged_predict gives prediction after each tree is added
    for Y_train_pred in model.staged_predict(X_train):
        train_errors.append(np.sqrt(mean_squared_error(Y_train, Y_train_pred)))

    for Y_test_pred in model.staged_predict(X_test):
        test_errors.append(np.sqrt(mean_squared_error(Y_test, Y_test_pred)))

    plt.figure(figsize=(10, 5))
    plt.plot(estimator_range, train_errors, label="Train RMSE", color='steelblue')
    plt.plot(estimator_range, test_errors,  label="Test RMSE",  color='tomato')
    plt.xlabel("Number of Estimators")
    plt.ylabel("RMSE")
    plt.title("Learning Curve — Gradient Boosting")
    plt.legend()
    plt.grid(True)
    plt.savefig(save_path)
    plt.show()

#------------------------------------------------------------------------------------
# Main Function
#------------------------------------------------------------------------------------

def main():

    # Load Dataset
    df = load_dataset("Dataset/California_Housing.csv")
    if df is None:
        return

    # Separate Features and Labels
    X, Y = separate_features_labels(df, target_column="target")

    # Split Data
    X_train, X_test, Y_train, Y_test = split_data(X, Y)

    # Create Model
    Boost_Model = create_model(n_estimators=100, learning_rate=0.1, max_depth=3)

    # Train Model
    Boost_Model = train_model(Boost_Model, X_train, Y_train)

    # Predict
    Y_pred = predict(Boost_Model, X_test)

    # Evaluate
    mse, rmse, r2 = evaluate_model(Y_test, Y_pred)

    # Plot Actual vs Predicted
    plot_actual_vs_predicted(Y_test, Y_pred)

    # Plot Feature Importance
    plot_feature_importance(Boost_Model, list(X.columns))

    # Plot Learning Curve
    plot_learning_curve(X_train, Y_train, X_test, Y_test)


if __name__ == "__main__":
    main()