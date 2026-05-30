from sklearn import tree

#Rough = 1
#Smooth = 0

# Cricket = 2
# Tennis = 1

def main():
    print("Ball Classification Case Study ")

    # Original encoded data set
    #Independent Variables
    X  = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    #Dependent  Variables
    Y = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    # Independent Variables for traing
    Xtrain = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]]

    # Independent Variables for testing
    Xtest = [[35,1],[95,0]]
    
    # Dependent Variables for traing
    Ytrain = [1,1,2,1,2,1,2,1,1,1,2,1,2]
    
    # Dependent Variables for testing
    Ytest = [1,2]

    modelobj = tree.DecisionTreeClassifier()

    trainedmodel = modelobj.fit(Xtrain, Ytrain)

    Result = trainedmodel.predict([[35,1]])          # 1 2

    print("Model predicts the object as : ",Result)

    print(type(Result))
    
    if Result == 1:
        print("Object looks like tennins ball")
    elif Result == 2:
        print("object  looks like cricket ball")


    
if __name__  == "__main__":
    main()
