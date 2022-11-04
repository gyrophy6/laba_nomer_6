import pandas as pd
import numpy as np
f = pd.read_csv("telecom_churn.csv")
f['count'] = 1
print(f.groupby("Customer service calls").agg({'count' : 'count'}))