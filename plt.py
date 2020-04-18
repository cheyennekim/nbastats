import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import sql, orm
from app import db
import models
import math
from statistics import mean, median


dic = models.setDic()
dfT = pd.DataFrame(data=dic)
df = dfT.T 
df2 = df[[4, 14, 19, 21, 23, 25, 27]].copy()
df3 = df2.T


def pltPerc(player):
	my_range=(range(1,len(df3.index)+1))
	comps = models.kNearPhys(player, 20)[0]
	for player in comps:
		None

	labels = ["fgper", "THptper", "drPer", "casPer", "pullPer", "postPer", "elbPer"]

	compsDF = df2.loc[comps, :]
	med = compsDF.median(axis=0)

	plt.hlines(y=my_range, xmin=df3["JJ Redick"], xmax=med, color='grey', alpha=0.4)
	plt.scatter(df3["JJ Redick"], my_range, color='skyblue', alpha=1, label="JJ Redick")
	plt.scatter(med, my_range, color='green', alpha=0.4 , label='Tacko')
	plt.legend()
	plt.yticks(my_range, labels)
	plt.title("Comparison of the value 1 and the value 2", loc='left')
	plt.xlabel('Value of the variables')
	plt.ylabel('Group')


	print(plt.show())


# print(med)
# # print(df3.head())
print(pltPerc("JJ Redick"))
comps = models.kNearPhys("JJ Redick", 20)[0]

compsDF = df2.loc[comps, :]
med = compsDF.median(axis=0)
print(df3["JJ Redick"])
# print(df3["LeBron James"])
print(med)


