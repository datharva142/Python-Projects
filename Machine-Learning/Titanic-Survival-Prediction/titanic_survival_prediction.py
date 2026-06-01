import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

#-------------------------------------------------------------------
#   Function Name : DisplayInfo
#   Description : Displays a formatted section title
#   Parameters : title (str)
#   Return  : None
#   Date : 14/03/2026
#   Author : Atharva Deshmukh
#-------------------------------------------------------------------

def DisplayInfo(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

#-------------------------------------------------------------------
#   Function Name : ShowData
#   Description : Shows basic information about the Dataset
#   Parameters : df     --> Pandas DataFrame object
#                message --> Heading text to display
#   Return  : None
#   Date : 14/03/2026
#   Author : Atharva Deshmukh
#-------------------------------------------------------------------

def ShowData(df, message):
    DisplayInfo(message)

    print("First Five Rows of Dataset : ")
    print(df.head())

    print("\nShape of Dataset : ")
    print(df.shape)

    print("\nColumn Names : ")
    print(df.columns.tolist())

    print("\nMissing Values in Each Column : ")
    print(df.isnull().sum())

#-------------------------------------------------------------------
#   Function Name : CleanTitanicData
#   Description : Performs full preprocessing pipeline
#                 - Removes unnecessary columns
#                 - Handles missing values
#                 - Converts categorical columns
#                 - Encodes Embarked column
#   Parameters : df --> Pandas DataFrame
#   Return  : df --> Cleaned DataFrame
#   Date : 14/03/2026
#   Author : Atharva Deshmukh
#-------------------------------------------------------------------

def CleanTitanicData(df):

    # ── Remove unnecessary columns ──────────────────────────────
    DisplayInfo("Step 2 : Original Data")
    print(df.head())
    print(df["Sex"].unique())

    drop_columns    = ["Passengerid", "zero", "Name", "Cabin"]
    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\nColumns to be Dropped : ")
    print(existing_columns)

    df = df.drop(columns=existing_columns)

    DisplayInfo("Step 2 : Data After Removal")
    print(df.head())

    # ── Handle Age column ────────────────────────────────────────
    if "Age" in df.columns:
        print("\nAge Column Before Preprocessing : ")
        print(df["Age"].head(10))

        df["Age"]  = pd.to_numeric(df["Age"], errors="coerce")
        age_median = df["Age"].median()
        df["Age"]  = df["Age"].fillna(age_median)

        print("\nAge Column After Preprocessing : ")
        print(df["Age"].head(10))

    # ── Handle Fare column ───────────────────────────────────────
    if "Fare" in df.columns:
        print("\nFare Column Before Preprocessing : ")
        print(df["Fare"].head(10))

        df["Fare"]  = pd.to_numeric(df["Fare"], errors="coerce")
        fare_median = df["Fare"].median()
        print("Median of Fare Column : ", fare_median)
        df["Fare"]  = df["Fare"].fillna(fare_median)

        print("\nFare Column After Preprocessing : ")
        print(df["Fare"].head(10))

    # ── Handle Sex column ────────────────────────────────────────
    if "Sex" in df.columns:
        print("\nSex Column Before Preprocessing : ")
        print(df["Sex"].head(10))

        df["Sex"] = pd.to_numeric(df["Sex"], errors="coerce")

        print("\nSex Column After Preprocessing : ")
        print(df["Sex"].head(10))

    DisplayInfo("Data After Preprocessing")
    print(df.head())
    print("\nMissing Values After Preprocessing : ")
    print(df.isnull().sum())

    # ── Handle Embarked column ───────────────────────────────────
    if "Embarked" in df.columns:
        print("\nEmbarked Column Before Preprocessing : ")
        print(df["Embarked"].head(10))

        df["Embarked"] = df["Embarked"].astype(str).str.strip()
        df["Embarked"] = df["Embarked"].replace(['nan', 'None', ''], np.nan)

        embarked_mode  = df["Embarked"].mode()[0]
        print("Mode of Embarked Column : ", embarked_mode)

        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("\nEmbarked Column After Preprocessing : ")
        print(df["Embarked"].head(10))

        df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

        # Convert boolean columns to integer
        for col in df.columns:
            if df[col].dtype == bool:
                df[col] = df[col].astype(int)

    DisplayInfo("Data After Encoding")
    print(df.head())
    print("Shape of Dataset : ", df.shape)

    return df

#-------------------------------------------------------------------
#   Function Name : PreserveModel
#   Description : Saves trained model to disk using joblib
#   Parameters : model    --> Trained ML model
#                filename --> Name of the output .pkl file
#   Return  : None
#   Date : 14/03/2026
#   Author : Atharva Deshmukh
#-------------------------------------------------------------------

def PreserveModel(model, filename):
    joblib.dump(model, filename)
    print(f"Model successfully preserved as : {filename}")

#-------------------------------------------------------------------
#   Function Name : LoadPreservedModel
#   Description : Loads a previously saved model from disk
#   Parameters : filename --> Path to the .pkl file
#   Return  : loaded_model --> Loaded ML model
#   Date : 14/03/2026
#   Author : Atharva Deshmukh
#-------------------------------------------------------------------

def LoadPreservedModel(filename):
    loaded_model = joblib.load(filename)
    print(f"Model successfully loaded from : {filename}")
    return loaded_model

#-------------------------------------------------------------------
#   Function Name : TrainTitanicModel
#   Description : Splits data, trains Logistic Regression model,
#                 preserves it, reloads it, and evaluates it
#   Parameters : df --> Cleaned Pandas DataFrame
#   Return  : None
#   Date : 14/03/2026
#   Author : Atharva Deshmukh
#-------------------------------------------------------------------

def TrainTitanicModel(df):

    # ── Separate Features and Labels ─────────────────────────────
    DisplayInfo("Step 3 : Separate Features and Labels")
    X = df.drop("Survived", axis=1)
    Y = df["Survived"]

    print("Features (X) : ")
    print(X.head())
    print("\nLabels (Y) : ")
    print(Y.head())
    print("\nShape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    # ── Train-Test Split ─────────────────────────────────────────
    DisplayInfo("Step 4 : Train-Test Split")
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )
    print("X_train Shape : ", X_train.shape)
    print("X_test  Shape : ", X_test.shape)
    print("Y_train Shape : ", Y_train.shape)
    print("Y_test  Shape : ", Y_test.shape)

    # ── Train Model ──────────────────────────────────────────────
    DisplayInfo("Step 5 : Train Logistic Regression Model")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)
    print("Model Trained Successfully")

    print("\nIntercept of Model : ")
    print(model.intercept_)

    print("\nCoefficients of Model : ")
    for feature, coefficient in zip(X.columns, model.coef_[0]):
        print(f"  {feature:30s} : {coefficient:.6f}")

    # ── Preserve Model ───────────────────────────────────────────
    DisplayInfo("Step 6 : Preserve Model")
    PreserveModel(model, "Titanic.pkl")

    # ── Load Preserved Model ─────────────────────────────────────
    DisplayInfo("Step 7 : Load Preserved Model")
    loaded_model = LoadPreservedModel("Titanic.pkl")

    # ── Predict & Evaluate ───────────────────────────────────────
    DisplayInfo("Step 8 : Predict and Evaluate")
    Y_pred   = loaded_model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    cm       = confusion_matrix(Y_test, Y_pred)

    print("Accuracy : ", accuracy)
    print("\nConfusion Matrix : ")
    print(cm)

#-------------------------------------------------------------------
#   Function Name : TitanicLogistic
#   Description : Main pipeline controller — loads, cleans,
#                 and trains the Titanic survival model
#   Parameters : Datapath --> Path to the CSV dataset file
#   Return  : None
#   Date : 14/03/2026
#   Author : Atharva Deshmukh
#-------------------------------------------------------------------

def TitanicLogistic(Datapath):
    DisplayInfo("Step 1 : Loading the Dataset")
    df = pd.read_csv(Datapath)

    ShowData(df, "Initial Dataset")

    df = CleanTitanicData(df)

    TrainTitanicModel(df)

#-------------------------------------------------------------------
#   Function Name : main
#   Description : Entry point of the application
#   Parameters : None
#   Return  : None
#   Date : 14/03/2026
#   Author : Atharva Deshmukh
#-------------------------------------------------------------------

def main():
    TitanicLogistic("Dataset/TitanicDataset.csv")

if __name__ == "__main__":
    main()