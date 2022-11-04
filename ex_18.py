import pandas as pd
import numpy as np
f = pd.read_csv("telecom_churn.csv")
print(f.loc[[100, 102, 104], ["State", "Churn"]])