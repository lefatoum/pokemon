import pandas as pnd
import numpy as nmp
import os

combats = pnd.read_csv("datas/combats.csv", encoding='latin-1')

# print(combats.columns.values)

# print(combats.head(10))

# print(combats.shape)

# print(combats.info())

# nbFoisPremierePosition = combats.groupby('Premier_Pokemon').count()
# print(nbFoisPremierePosition)

# taillesDataFrame = pnd.DataFrame({"taille": [175, pnd.np.nan, 160, 170, 180]})

nbFoisSecondepositon = combats.groupby('Second_Pokemon').count()
print(nbFoisSecondepositon)