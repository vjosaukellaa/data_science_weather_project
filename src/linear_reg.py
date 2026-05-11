from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def temp_model(df):
    #Inputs to predict temperature
    X = df[["Year","Month","PRCP"]]
    #Target temperature
    Y = df["TAVG"]
    
    dates = df["DATE"]

    #Training data and testing sets
    X_train, X_test, Y_train, Y_test, dates_train, dates_test = train_test_split(
        X,
        Y,
        dates,
        test_size = 0.2,
        random_state = 34
    )

    #Linear Regression Model!
    model = LinearRegression()

    #Train model
    model.fit(X_train, Y_train)

    #Predicting temperature values!
    predictions = model.predict(X_test)

    #Analyzing how accurate the model is
    mae = mean_absolute_error(Y_test, predictions)
    mse = mean_squared_error(Y_test, predictions)
    r2 = r2_score(Y_test, predictions)

    #Return calculated values
    print("Mean Absolute Error:", mae)
    print("Mean Squared Error:", mse)
    print("R-squared:", r2)

    #Return values for later use
    return model, Y_test, predictions, dates_test

