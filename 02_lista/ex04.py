import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(16.).reshape((4, 4)), index=['a', 'b', 'c', 'd'], columns=['c1', 'c2', 'c3', 'c4'])
sr = pd.Series([1., 2., 3., 4.])

sr.index = df.columns
res = df - sr

print(res)

sr.index = df.columns
res = df.sub(sr)

print("a")
print(res)

sr.index = df.columns
res = df.sub(sr)

print("b")
print(res)

sr.index = df.index
res = df - sr

print("c")
print(res)

sr.index = df.columns
res = df.sub(sr, axis='columns')

print("d")
print(res)

sr.index = df.index
res = df.sub(sr, axis='index')

print("e")
print(res)

sr.index = df.index
res = df.sub(sr)

print("f")
print(res)

sr.index = df.columns
res = df.sub(sr, axis='index')

print("g")
print(res)

sr.index = df.index
res = df.sub(sr, axis='columns')

print("h")
print(res)


print("sr")
print(sr)