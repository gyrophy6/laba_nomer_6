import pandas as pd
import numpy as np
f = pd.read_csv("telecom_churn.csv")
f["count"] = 1
avgTDCandTEC1 = f.groupby("State").agg({"Total day calls" : "sum", "Total eve calls":"sum", "count" : "sum"})
avgTDCandTEC1["day > eve"] = avgTDCandTEC1["Total day calls"] > avgTDCandTEC1["Total eve calls"]
avgTDCandTEC1["Total day calls"] = avgTDCandTEC1["Total day calls"] / avgTDCandTEC1["count"]
avgTDCandTEC1["Total eve calls"] = avgTDCandTEC1["Total eve calls"] / avgTDCandTEC1["count"]
del avgTDCandTEC1["count"]
print(avgTDCandTEC1)