import pandas as pd
import numpy as np
f = pd.read_csv("telecom_churn.csv")
print(f.groupby("State").agg({"Total day charge" : "sum"}).sort_values(by="Total day charge", ascending = True))