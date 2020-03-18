import pandas as pd
import numpy as np

#merge
left = pd.DataFrame({'key':['K0','K1','K2','K3'],
					'A':['A0','A1','A2','A3'],
					'B':['B0','B1','B2','B3'],})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],
					'C':['C0','C1','C2','C3'],
					'D':['D0','D1','D2','D3'],})

print(left)
print(right)


res = pd.merge(left,right,on='key')
print(res)
'''  key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
  key   A   B   C   D
0  K0  A0  B0  C0  D0
1  K1  A1  B1  C1  D1
2  K2  A2  B2  C2  D2
3  K3  A3  B3  C3  D3
'''
left1 = pd.DataFrame({'key1':['K0','K0','K1','K2'],
			    	'key2':['K0','K1','K0','K1'],	
					'A':['A0','A1','A2','A3'],
					'B':['B0','B1','B2','B3'],})
right1 = pd.DataFrame({'key1':['K0','K1','K1','K2'],
						'key2':['K0','K0','K0','K0'],
					'C':['C0','C1','C2','C3'],
					'D':['D0','D1','D2','D3'],})
print(left1)
print(right1)
#how=['left','right','outer','inner']
res1 = pd.merge(left1,right1,on=['key1','key2'])#how='inner' 
print(res1)

#handle overlapping

boys  = pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls = pd.DataFrame({'k':['K0','K1','K2'],'age':[4,5,6]})
print(boys)
print(girls)
res11 = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')
print(res11)
