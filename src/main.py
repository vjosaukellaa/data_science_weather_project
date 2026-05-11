from clean_data import clean_data
from figures import (
    temp_vs_t,
    precip_vs_t,
    monthly_temp,
    act_vs_pred,
    corr_heatmap
)
from linear_reg import temp_model

#Clean data
df = clean_data()

#Graphs
temp_vs_t(df)
precip_vs_t(df)
monthly_temp(df)
#Linear regression model
model, Y_test, predictions, dates_test = temp_model(df)
#Comparing actual and predicted temperatures
act_vs_pred(Y_test, predictions)
#Correlation heat map
corr_heatmap(df)
