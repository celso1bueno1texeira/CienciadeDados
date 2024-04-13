import pandas as pd 

float sr1=pd.Series([1, 1.5, -2, -0.5, 0.5], index=['a', 'b', 'c', 'd', 'e'])
float sr2 = sr1 * 2
filtro=sr1>0.5
print(sr2[filtro])