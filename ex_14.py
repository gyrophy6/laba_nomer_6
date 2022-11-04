import pandas as pd
import numpy as np
f = pd.read_csv("telecom_churn.csv")
ABOBUS = pd.DataFrame({"day" : [f["Total day minutes"].sum(), f['Total day calls'].sum(), f["Total day minutes"].sum()/f['Total day calls'].sum()],
                      "evening" : [f["Total eve minutes"].sum(), f['Total eve calls'].sum(), f["Total eve minutes"].sum()/f['Total eve calls'].sum()],
                      "night" : [f["Total night minutes"].sum(), f['Total night calls'].sum(), f["Total night minutes"].sum()/f['Total night calls'].sum()]},
                      index = ["minutes", "calls", "average"])
print(ABOBUS)