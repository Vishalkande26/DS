import pandas as pd
import matplotlib.pyplot as mt
import numpy as nu

df1=pd.read_csv('/home/itsl1-08/AirQuality.csv',sep=';')
print(df1)

df2=pd.read_csv('/home/itsl1-08/heart.csv',sep=',')
print(df2)

#a)Data Cleaning d)Error Correcting
#Removal of Duplicate for heart
df3=df2.drop_duplicates()
print(df3)

#Removal of Duplicate for Airquality
df4=df1.drop_duplicates()
print(df4)

#Removal of irrelevant 
df5=df1.dropna(subset=['CO(GT)'])
print(df5)

#Handling a missing Values
df6=df1.isnull()
print(df6)

#Correcting Columns
df7=df1.columns.tolist()
print(df7)

#d)Error Correcting Remove outliers 
def remove_outliers(df1,columns,n_std):
    for col in columns:
        print('working on columns: {}'.format(col))
        mean=df1[col].mean()
        sd=df1[col].std()
        df1=df1[(df1[col]<=mean+(n_std*sd))]
    return df1
print(df1)

#b)Data integration
di=pd.concat([df1,df2])
print(di)

#c)Data transformation
#groupby
gb=df2.groupby(['age','sex'])
print(gb.first())

#e)Data model building
#Histogram
mt.hist(df2)
mt.show()

#BoxPlot
mt.boxplot(df2)
mt.show()

#scatter diagram
x = df2['age']
y = df2['sex']
mt.scatter(x, y)
mt.xlabel('age')
mt.ylabel('sex')
mt.title('Scatter Diagram')
mt.show()
