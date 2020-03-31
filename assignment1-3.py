import pandas as pd
from pandas import Series,DataFrame
import numpy as np
data = pd.read_csv("C:\\Users\\ytjh0\\Desktop\\lottery.csv")
data2=pd.DataFrame(np.random.randint(0,2,size=(716,3)),columns=list("wea")) #made new columns
data2=data2.rename(columns={"w": "weather", "e": "win","a": "purcharsed"}) #edit name
data2=data2.replace({'win':{0: '0-lose', 1: '1-win'}}) #detail win/lose 
data2=data.join(data2)
print(data2)
data2.to_csv("lottery2.csv", mode="w")
