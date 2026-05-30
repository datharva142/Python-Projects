import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-" * 80

#------------------------------------------------------------------------------------
# Step 1 : Load Dataset
#------------------------------------------------------------------------------------
print(Border)
print("                            Step 1 load the Dataset.                         ")
print(Border)

DataserPath = "Iris.csv"

df = pd.read_csv(DataserPath)

print("Dataset loaded successfully.")
print("Initial Entries form Dataset:")
print(df.head())


#--------------------------------------------------------------------------------
# Step 2: data Analysis
#--------------------------------------------------------------------------------

print(Border)
print("                            Step 2 Data Analysis.                         ")
print(Border)

print("Shape of Dataset: ", df.shape)
print("Colum Names: ", list(df.columns))

print("Missing vales (Per column): ")
print(df.isnull().sum())

print("Class distribution(species count): ")
print(df['species'].value_counts())

print("Statical Report of Dataset: ")
print(df.describe())


#--------------------------------------------------------------------------------
# Step 3: Deside Independent and dependent variables
#--------------------------------------------------------------------------------
print(Border)
print("            Step 3: Deside Independent and dependent variables            ")
print(Border)

# X : Independent Variables / Features
# Y : Dependent Variables / Labels

feature_cols =[
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[feature_cols]
Y = df["species"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)


#--------------------------------------------------------------------------------
# Step 4: Visualization of dataset
#--------------------------------------------------------------------------------
print(Border)
print("                   Step 4: Visualization of data set                   ")
print(Border)

# Scatter plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label = sp)

plt.title("Iris : Petal length vs Petal width")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid(True)
plt.show()


#--------------------------------------------------------------------------------
# Step 5: Split the Data set for training and testing
#--------------------------------------------------------------------------------
print(Border)
print("                 Step 5: Split the Data set for training and testing                ")
print(Border)

#Tesst size = 20%
#Train size = 80%

X_Train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42
)

print("Data Splitting activity done :")

print("X - Idependent : ",X.shape)
print("Y - Dependent : ",Y.shape)

print("X_train : ",X_Train.shape)
print("X_test : ",X_test.shape)

print("Y_train : ",Y_train.shape)
print("Y_test : ",Y_test.shape)


#--------------------------------------------------------------------------------
# Step 6: Built the model
#--------------------------------------------------------------------------------
print(Border)
print("                         Step 6: Build the model                              ")
print(Border)

print("We are Going to use DisionTreClassifier")

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

print("Model Succesfully Created : ",model)


#--------------------------------------------------------------------------------
# Step 7: Train the Model
#--------------------------------------------------------------------------------
print(Border)
print("                         Step 7: Train the model                              ")
print(Border)

model.fit(X_Train,Y_train)

print("Model training Completed")


#--------------------------------------------------------------------------------
# Step 8: Test the Model
#--------------------------------------------------------------------------------
print(Border)
print("                         Step 8 : Evaluate the model                              ")
print(Border)

Y_pred = model.predict(X_test)

print("Model evaluation(testing) Complete")

print(Y_pred.shape)

print("Expected answers : ")
print(Y_test)

print("Predicted answers : ")
print(Y_pred)


#--------------------------------------------------------------------------------
# Step 9: Evaluation of the model Preformance
#--------------------------------------------------------------------------------
print(Border)
print("                 Step 9 : Evaluate the model performance                              ")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of model is : ",accuracy*100)

cm = confusion_matrix(Y_test, Y_pred)
print("Confusion Matrix : ")
print(cm)

print("classification Report")
print(classification_report(Y_test,Y_pred))


#--------------------------------------------------------------------------------
# Step 10: Plot Confusion Matrix
#--------------------------------------------------------------------------------
print(Border)
print("                 Step 10 : Plot Confusion Matrix                              ")
print(Border)

data = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)

data.plot()
plt.title("Confusion Matrix of Iris Dataset")
plt.show()

#--------------------------------------------------------------------------------
# Step 11: Plot Decision Tree
#--------------------------------------------------------------------------------
print(Border)
print("                 Step 11 : Plot Decision Tree                              ")
print(Border)

plt.figure(figsize=(12,8))

plot_tree(
    model,
    feature_names=feature_cols,
    class_names=model.classes_,
    filled=True
)

plt.title("Decision Tree Visualization")
plt.show()