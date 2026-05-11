#Imports
import pandas as pd 
#Cleaning the data for only the New Brunswick data
def clean_data():
    #Load in the data
    df = pd.read_csv("weather.csv")
    
    #Isolating the New Brunswick data and dates
    df = df[df["NAME"] == "NEW BRUNSWICK 3 SE, NJ US"]
    df["DATE"] = pd.to_datetime(df["DATE"])
   
    #Isolate the data
    weather_data = ["PRCP", "SNOW", "TAVG", "TMAX", "TMIN"]
    for col in weather_data:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    #Dropping any data that is null or emply
    df = df.dropna(subset=["TAVG", "PRCP"])
    
    #Isolating the Year and Months
    df["Year"] = df["DATE"].dt.year
    df["Month"] = df["DATE"].dt.month 

    #Return the final data
    return df

    
