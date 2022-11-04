import pandas as pd
import numpy as np
f = pd.read_csv("telecom_churn.csv")
from random import *
wwqrdeewrdqwerdqqwrdRUN = pd.DataFrame({"aboba": [randrange(0, 100) for i in range(50)], "kek": [randrange(0, 100) for i in range(50)]})
wwqrdeewrdqwerdqqwrdRUN["sumSquares"] = wwqrdeewrdqwerdqqwrdRUN["aboba"]**2 + wwqrdeewrdqwerdqqwrdRUN["kek"]**2
wwqrdeewrdqwerdqqwrdRUN["mean"] = wwqrdeewrdqwerdqqwrdRUN[["aboba", "kek", "sumSquares"]].apply(lambda x: x.mean(), axis=1)
print(wwqrdeewrdqwerdqqwrdRUN)