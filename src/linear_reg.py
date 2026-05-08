from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_error

def temp_model(df):
    X = df[["Year","Month"]]
    Y = df["TAVG"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size = 0.2,
        random_state = 34
    )

    model = LinearRegression()

    model.fit(X_train, Y_train)

    predictions = model.predict(X_test)

    mse = mean_squared_error(Y_test, predictions)
    r2 = r2_score(Y_test, predictions)

    print("Mean Squared Error:", mse)
    print("R-squared:", r2)

    return model
    