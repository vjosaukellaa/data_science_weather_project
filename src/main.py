from clean_data import clean_data
from figures import (
    temp_vs_t,
    precip_vs_t,
    monthly_temp
)
from linear_reg import temp_model

df = clean_data()

temp_vs_t(df)
precip_vs_t(df)
monthly_temp(df)

model = temp_model(df)