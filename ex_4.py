import pandas as pd
import numpy as np
f = pd.read_csv("telecom_churn.csv")
print(f[f["State"] == "KS"]["Total day calls"].mean())