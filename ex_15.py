import pandas as pd
import numpy as np
f = pd.read_csv("telecom_churn.csv")
rem = f[f["Churn"] == False]["Total day charge"].sum()
left = f[f["Churn"] == True]["Total day charge"].sum()
print(left, rem, "LEFT > REMAINING")