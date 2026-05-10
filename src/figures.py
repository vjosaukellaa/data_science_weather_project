import matplotlib.pyplot as plt 

def temp_vs_t(df):

    plt.figure(figsize=(10,5))
    plt.plot(df["DATE"],df["TAVG"])

    plt.xlabel("Date")
    plt.ylabel("Average Temperature")
    plt.title("Average Temperature Over Time in New Brunswick, NJ")

    plt.show()

def precip_vs_t(df):
    
    plt.figure(figsize=(10,5))
    plt.plot(df["DATE"],df["PRCP"])

    plt.xlabel("Date")
    plt.ylabel("Precipitation")
    plt.title("Precipitation Over Time in New Brunswick, NJ")

    plt.show()

def monthly_temp(df):
    tempmonth = df.groupby("Month")["TAVG"].mean()

    plt.figure(figsize=(8,5))
    plt.bar(tempmonth.index, tempmonth.values)

    plt.xlabel("Month")
    plt.ylabel("Average Temperature")
    plt.title("Average Temperature by Month in New Brunswick, NJ")