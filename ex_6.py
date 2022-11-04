import pandas as pd
import numpy as np
f = pd.read_csv("telecom_churn.csv")
avgTotDayColForEachState = f.groupby('State').agg({"Total day calls" : "mean"})
print(avgTotDayColForEachState[avgTotDayColForEachState["Total day calls"] > f["Total day calls"].mean()])