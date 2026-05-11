#Imports
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

#Temperature vs time graph
def temp_vs_t(df):
    plt.figure(figsize=(10,5))

    #Plot the x and y variables (dates vs temperature) as a linear graph
    plt.plot(df["DATE"],df["TAVG"])

    plt.xlabel("Date")
    plt.ylabel("Average Temperature")
    plt.title("Average Temperature Over Time in New Brunswick, NJ")

    plt.show()

#Precipitation vs time 
def precip_vs_t(df):
    plt.figure(figsize=(10,5))

     #Plot the x and y variables (dates vs precipitation) as a linear graph
    plt.plot(df["DATE"],df["PRCP"])

    plt.xlabel("Date")
    plt.ylabel("Precipitation")
    plt.title("Precipitation Over Time in New Brunswick, NJ")

    plt.show()

#Average monthly temperature
def monthly_temp(df):
    #Group the average temperature by the month
    tempmonth = df.groupby("Month")["TAVG"].mean()

    plt.figure(figsize=(8,5))
    
    #Create a bar graph 
    plt.bar(tempmonth.index, tempmonth.values)

    plt.xlabel("Month")
    plt.ylabel("Average Temperature")
    plt.title("Average Temperature by Month in New Brunswick, NJ")

    plt.show()

def act_vs_pred(Y_test, predictions, dates_test):
    #Creating dataframe including the dates, actual temperature values, and predicted temperature values
    results = pd.DataFrame({
        "Date": dates_test,
        "Actual": Y_test,
        "Predicted": predictions
    })

    #Sorting by date
    results = results.sort_values("Date")

    plt.figure(figsize=(12,5))

    #Plotting the actual values linearly
    plt.plot(
        results["Date"],
        results["Actual"],
        label="Actual",
        color="blue"
    )

    #Plotting the predicted values linearly
    plt.plot(
        results["Date"],
        results["Predicted"],
        label="Predicted",
        color="red"
    )

    plt.xlabel("Date")
    plt.ylabel("Average Temperature")
    plt.title("Actual vs Predicted Temperatures")

    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

def corr_heatmap(df):
    #Correlations between the weather data 
    corr = df[["PRCP", "SNOW", "TAVG", "TMAX", "TMIN"]].corr()

    plt.figure(figsize=(7,5))

    #Creating the heat map 
    plt.imshow(corr)

    plt.colorbar()

    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
    plt.yticks(range(len(corr.columns)), corr.columns)

    plt.title("Correlation Heatmap")

    plt.show()