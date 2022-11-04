import pandas as pd
import numpy as np
f = pd.read_csv("telecom_churn.csv")
f['count'] = 1
sum = f['count'].sum()
voice = f[f['Voice mail plan'] == "Yes"]['count'].sum()
intl = f[f['International plan'] == "Yes"]['count'].sum()
print('intl : ', intl / sum, '\nvoice : ', voice / sum)