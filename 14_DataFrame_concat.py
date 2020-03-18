import pandas as pd
import numpy as np

#concatenating
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

print(df1)
print(df2)
print(df3)

#res = pd.concat([df1,df2,df3],axis=0) #0--> vertical
res = pd.concat([df1,df2,df3],axis=0,ignore_index=True) #0--> vertical

print(res)


#join,[inner,outer]
df11 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df22 = pd.DataFrame(np.ones((3,4))*1,columns=['a','c','d','e'],index=[2,3,4])

print(df11,df22)

res1 = pd.concat([df11,df22],join='inner',ignore_index=True)
print(res1)

#join_axes
df111 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df222 = pd.DataFrame(np.ones((3,4))*1,columns=['a','c','d','e'],index=[2,3,4])
#res11 = pd.concat([df111,df222],axis=1,join_axes=[df111.index])
res11 = pd.concat([df111,df222],axis=1).reindex(df111.index)
print(res11)

#append
df1111 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2222 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3333 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
#res11 = pd.concat([df111,df222],axis=1,join_axes=[df111.index])
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
#res111 = df1111.append([df2222,df3333],ignore_index=True)
res111 = df1111.append(s1,ignore_index=True)
print(res111)

