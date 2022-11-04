import pandas as pd
import numpy as np
f = pd.read_csv("telecom_churn.csv")
f['count'] = 1
SerCalandCh = f.groupby('Customer service calls').agg({"Churn" : 'sum', 'count' : 'sum'})
SerCalandCh['Churn'] = SerCalandCh['Churn'] / SerCalandCh['count']
del SerCalandCh['count']
print(SerCalandCh)

import matplotlib.pyplot as plt
from secretstorage import SecretStorageException
plt.bar(x=range(0,10), height=SerCalandCh['Churn'])
plt.xlabel('Service customer calls')
plt.ylabel('Churn')
plt.show()

#z xtcnyj ctqxfc gjlj[ye&&&