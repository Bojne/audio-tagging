import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('../data/tags_train.csv')
df['split'] = np.random.randn(df.shape[0], 1)

msk = np.random.rand(len(df)) <= 0.9

train = df[msk]
test = df[~msk]

train.info()
test.info()

train.to_csv("../data/tags_train.csv")
test.to_cvs("../data/tags_test.csv")