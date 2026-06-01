import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def Classifier(Datapath):
    Border = "-"*60
    
    #Step 1 : Load The Dataset from csv File
    
    print(Border)
    print("Step 1 : Load The Dataset from csv File")
    print(Border)
    
    try:
        df = pd.read_csv(Datapath)
    except FileNotFoundError:
        print("File not found")
        return

    print(Border)
    print("Some Entries from dataset")
    print(Border)
    print(df.head())
    
    #Step 2 : Clean the dataset by removing empty rows

    print(Border)
    print("Step 2 : Clean the dataset by removing empty rows")
    print(Border)

    df.dropna(inplace = True)
    print("Total Records : ",df.shape[0])
    print("Total Columns : ",df.shape[1])
    print(Border)

    #Step 3 : Seprate Dependent and Idependent Variables

    print(Border)
    print("Step 3 : Seprate Dependent and Idependent Variables")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Border)
    print("Input Columns : ", X.columns.to_list())
    print("Output Colum : Class")

    #Step 4 : Split The Dataset For Training and Testing

    print(Border)
    print("Step 4 : Split The Dataset For Training and Testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42, stratify=Y)

    print(Border)
    print("Information of training and Testing Data")
    print("X_train Shape : ",X_train.shape)
    print("X_test Shape : ",X_test.shape)
    print("Y_train Shape : ",Y_train.shape)
    print("Y_test Shape : ",Y_test.shape)
    print(Border)

    # Step 5 : Feature Scaling

    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)

    scaler = StandardScaler()
    #Independent variable scalling
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Feature Scaling is Done")

    # Step 6 : Explore the Multiple Values of k
    # Hyperparameter Tunning (K)

    print(Border)
    print("Step 6 : Explore the Multiple Values of k")
    print(Border)

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled, Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print(Border)
    print("Accuracy of all the K values from 1 to 20")
    for value in accuracy_scores:
        print(value)

    print(Border)

    # Step 7 : plot graph of K vs Accuracy
   
    print(Border)
    print("Step 7 : plot graph of K vs Accuracy")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values, accuracy_scores, marker = 'o')
    plt.title("K values vs Accuracy")
    plt.xlabel("Values of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()

    # Step 8 : Find Best value of K
   
    print(Border)
    print("Step 8 : Find Best value of K")
    print(Border)

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best value of k is : ",best_k)

    # Step 9 : Build final Model using best value of k
      
    print(Border)
    print("Step 9 : Build final Model using best value of k")
    print(Border)

    final_model = KNeighborsClassifier(n_neighbors= best_k)
    final_model.fit(X_train_scaled, Y_train)

    Y_pred = final_model.predict(X_test_scaled)

    # Step 10 : Calculate Final Accuracy 
      
    print(Border)
    print("Step 10 : Calculate Final Accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of model is : ",accuracy)

    # Step 11 : Display Confusion Matrix 
      
    print(Border)
    print("Step 11 : Display Confusion Matrix")
    print(Border)

    cm = confusion_matrix(Y_test,Y_pred)
    print(cm)

    # Step 12 : Display Classification Report
      
    print(Border)
    print("Step 12 : Display Classification Report")
    print(Border)

    print(classification_report(Y_test,Y_pred))

def main():
    Border = "-"*60
    print(Border)
    print("Wine Classidier using KNN")
    print(Border)

    Classifier('Dataset/WinePredictor.csv')

if __name__ == "__main__":
    main()