import numpy as ny 
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

colnames = ['sepal-length','sepal-width','petal-length','petal-width','class']

iris = pd.read_csv(url, names=colnames)

print(iris.head())

print(type(iris))

print(iris.shape)

## diferença entre metodos e atributos

print(len(iris['class']))