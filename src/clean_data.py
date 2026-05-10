import pandas as pd 

def clean_data():
    df = pd.read_csv("weather.csv")
    df = df[df["NAME"] == "NEW BRUNSWICK 3 SE, NJ US"]
    df["DATE"] = pd.to_datetime(df["DATE"])
    weather_cols = ["PRCP", "SNOW", "TAVG", "TMAX", "TMIN"]

    for col in weather_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        
    df = df.dropna(subset=["TAVG", "PRCP"])

    df["Year"] = df["DATE"].dt.year
    df["Month"] = df["DATE"].dt.month 

    return df

    
