import pandas as pd 
import numpy as np 

arquivo = open('F:\\ws\\cienciasDados\\DataScience\\Python\\iris.csv', 'r')
base = pd.read_csv(arquivo)
base.shape

np.random.seed(2345)
amostra = np.random.choice([0,1],150,replace=True, p=[0.7 , 0.3])

baseFinal = base.loc(amostra == 0)
print(baseFinal)
