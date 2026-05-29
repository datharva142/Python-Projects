import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def breast_cancer_classification(DataPath):

    Border = "-" * 60

    # ------------------------------------------------------------
    # Step 1 : Load Dataset
    # ------------------------------------------------------------

    print(Border)
    print("Step 1 : Load Dataset")
    print(Border)

    try:
        df = pd.read_csv(DataPath)

    except FileNotFoundError:

        print("Error : File not found")
        return

    print("Shape of Dataset :", df.shape)

    print("First Five Records :")
    print(df.head())

    # ------------------------------------------------------------
    # Step 2 : Separate Features and Labels
    # ------------------------------------------------------------

    print(Border)
    print("Step 2 : Separate Features and Labels")
    print(Border)

    X = df.drop("target", axis=1)
    Y = df["target"]

    print("Features Shape :", X.shape)
    print("Labels Shape :", Y.shape)

    # ------------------------------------------------------------
    # Step 3 : Split Dataset
    # ------------------------------------------------------------

    print(Border)
    print("Step 3 : Split Dataset")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("X_train :", X_train.shape)
    print("X_test :", X_test.shape)

    print("Y_train :", Y_train.shape)
    print("Y_test :", Y_test.shape)

    # ------------------------------------------------------------
    # Step 4 : Create Base Model
    # ------------------------------------------------------------

    print(Border)
    print("Step 4 : Create Base Model")
    print(Border)

    Base_Model = DecisionTreeClassifier(
        random_state=42
    )

    # ------------------------------------------------------------
    # Step 5 : Create Bagging Model
    # ------------------------------------------------------------

    print(Border)
    print("Step 5 : Create Bagging Model")
    print(Border)

    Bagging_Model = BaggingClassifier(
        estimator=Base_Model,
        n_estimators=10,
        random_state=42
    )

    # ------------------------------------------------------------
    # Step 6 : Train Model
    # ------------------------------------------------------------

    print(Border)
    print("Step 6 : Train Model")
    print(Border)

    Bagging_Model.fit(
        X_train,
        Y_train
    )

    # ------------------------------------------------------------
    # Step 7 : Predict Results
    # ------------------------------------------------------------

    print(Border)
    print("Step 7 : Predict Results")
    print(Border)

    Y_pred = Bagging_Model.predict(X_test)

    # ------------------------------------------------------------
    # Step 8 : Evaluate Model
    # ------------------------------------------------------------

    print(Border)
    print("Step 8 : Evaluate Model")
    print(Border)

    Accuracy = accuracy_score(
        Y_test,
        Y_pred
    )

    print("Bagging Accuracy :")
    print(Accuracy)

    print("\nClassification Report :")
    print(
        classification_report(
            Y_test,
            Y_pred
        )
    )

    print("\nConfusion Matrix :")
    print(
        confusion_matrix(
            Y_test,
            Y_pred
        )
    )

def main():

    breast_cancer_classification(
        "Dataset/breast_cancer.csv"
    )

if __name__ == "__main__":
    main()