import pandas as pd
import numpy as np
f = pd.read_csv("telecom_churn.csv")
print(f["Total day calls"].mean())