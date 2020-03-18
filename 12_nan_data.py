import pandas as pd
import numpy as np


dates = pd.date_range('20200101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])


print('='*30)
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

print(df)
print(np.any(df.isnull()) == True)
print(df.isnull())
#print(df.dropna(axis=0,how='any')) #how={'any','all'}
print(df.fillna(value=0))
