import pandas as pd
import numpy as np
f = pd.read_csv("telecom_churn.csv")
avgTDCandTEC = f.groupby("State").agg({"Total day calls" : "mean", "Total eve calls":"mean"})
print(avgTDCandTEC)