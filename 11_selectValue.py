import pandas as pd
import numpy as np


dates = pd.date_range('20200101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df)


print('='*30)
df.iloc[2,2] = 111
df.loc['20200102','B'] = 222

#df[df.A>4] = 0
df.B[df.A>4] = 0

df['F'] = np.nan
df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20200101',periods=6))
print(df)
