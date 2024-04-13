from pandas import Series, DataFrame
sr = Series([0, 1, 3, -5, 7], index=['a', 'b', 'c', 'd', 'e'])
print(sr)

print(sr[sr >= 0])

data={
    'UF': ['PR', 'SC', 'RS'],
    'pop': [11433957, 7164788, 11377239]
}
    
df=DataFrame(data, columns=['estado', 'populacao'])
print(df)

df=DataFrame(data)
print(df)