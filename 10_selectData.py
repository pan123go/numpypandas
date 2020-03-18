import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,44,1])
#print(s)

dates = pd.date_range('20200101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df)

print(df['A'],df.A)
print(df[0:3],df['20200103':'20200105'])
print('=========')

#select by label: loc 
print(df.loc['20200102'])
print(df.loc[:,['A','B']])

#select by position:iloc
print(df.iloc[3,1])
print(df.iloc[3:5,1:3])

#mixed selection:ix
#print(df.ix[:3,['A','C']])

#Boolean indexing
print(df)
print(df[df.A>8])





#3333df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
#3333print(df1)
