import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error, r2_score

#------------------------------------------------------------------------------------
# Step 1 : Load Dataset
#------------------------------------------------------------------------------------

def load_dataset(path):
    try:
        df = pd.read_csv(path)
        print("Shape of Dataset : ", df.shape)
        print("First five Records : \n", df.head())
        return df
    except Exception as e:
        print("Error in loading dataset : ", e)
        return None

#------------------------------------------------------------------------------------
# Step 2 : Separate Features and Labels
#------------------------------------------------------------------------------------

def separate_features_labels(df, target_column):
    X = df.drop(target_column, axis=1)
    Y = df[target_column]
    return X, Y

#------------------------------------------------------------------------------------
# Step 3 : Split Data for Training
#------------------------------------------------------------------------------------

def split_data(X, Y, test_size=0.2, random_state=42):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=random_state)
    return X_train, X_test, Y_train, Y_test

#------------------------------------------------------------------------------------
# Step 4 : Create Base Model
#------------------------------------------------------------------------------------

def create_base_model(random_state=42):
    return DecisionTreeRegressor(random_state=random_state)

#------------------------------------------------------------------------------------
# Step 5 : Create Bagging Model
#------------------------------------------------------------------------------------

def create_bagging_model(base_model, n_estimators=10, random_state=42):
    return BaggingRegressor(
        estimator=base_model,
        n_estimators=n_estimators,
        random_state=random_state
    )

#------------------------------------------------------------------------------------
# Step 6 : Train Model
#------------------------------------------------------------------------------------

def train_model(model, X_train, Y_train):
    model.fit(X_train, Y_train)
    return model

#------------------------------------------------------------------------------------
# Step 7 : Test / Predict
#------------------------------------------------------------------------------------

def predict(model, X_test):
    return model.predict(X_test)

#------------------------------------------------------------------------------------
# Step 8 : Evaluate Model
#------------------------------------------------------------------------------------

def evaluate_model(Y_test, Y_pred):
    mse  = mean_squared_error(Y_test, Y_pred)
    rmse = np.sqrt(mse)
    r2   = r2_score(Y_test, Y_pred)
    print("Mean Squared Error   : ", mse)
    print("R2 Score             : ", r2)
    print("Root Mean Sq. Error  : ", rmse)
    return mse, rmse, r2

#------------------------------------------------------------------------------------
# Step 9 : Plot Base Model vs Bagging Model
#------------------------------------------------------------------------------------

def plot_model_comparison(base_rmse, bagging_rmse,):
    plt.figure(figsize=(6, 5))
    plt.bar(["Decision Tree", "Bagging Regressor"], [base_rmse, bagging_rmse],
            color=['tomato', 'steelblue'])
    plt.ylabel("RMSE")
    plt.title("Base Model vs Bagging Model RMSE")
    plt.grid(axis='y')
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

    # Create and Train Base Model (standalone, for comparison)
    Base_Model    = create_base_model()
    Base_Model     = train_model(Base_Model, X_train, Y_train)
    base_pred      = predict(Base_Model, X_test)
    _, base_rmse, _ = evaluate_model(Y_test, base_pred)

    # Create and Train Bagging Model
    Bagging_Model     = create_bagging_model(create_base_model())
    Bagging_Model      = train_model(Bagging_Model, X_train, Y_train)
    Y_pred             = predict(Bagging_Model, X_test)
    _, bagging_rmse, _ = evaluate_model(Y_test, Y_pred)

    # Plot Comparison
    plot_model_comparison(base_rmse, bagging_rmse)


if __name__ == "__main__":
    main()