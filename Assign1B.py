import pandas as pd

df=pd.read_csv('/home/itsl1-08/YASH/dataset_Facebook.csv',sep=';')
print(df)

#a) Create data 1st subsets of Dataset columnwise
df1=df[['Page total likes','Type','Category','Post Month','Post Weekday','Post Hour','Paid','Lifetime Post Total Reach','Lifetime Post Total Impressions']]
print(df1)
#2nd subsets of Dataset columnwise
df2=df[['Lifetime Engaged Users','Lifetime Post Consumers','Lifetime Post Consumptions','Lifetime Post Impressions by people who have liked your Page','Lifetime Post reach by people who like your Page','Lifetime People who have liked your Page and engaged with your post','comment','like','share','Total Interactions']]
print(df2)
# creating subsets rowwise
df3=df.loc[[1,3,5,7,9,11,13,15]]
print(df3)
# display 1st two column and from 0-5 rows
df4=df.loc[0:5,['Type','Category']]
print(df4)

#b) Merge Dataset df1 and df2
df5=pd.concat([df1,df2])
print(df5)

#c) Sort Data
df6=df.sort_values(by=['Category'], ascending=False)
print(df6)

# Sorting by Multiple datasets
df7=df.sort_values(by=['Type','Category'],ascending=(False,True))
print(df7)

#d) Transpose 
df8=df.transpose()
print(df8)

#e) Shape and Rshape Data
#i)Shape Function
df9=df.shape
print("format={}".format(df9))

#ii) Reshape Function
#Using melt() method 
df10=df.melt()
print(df10)

#Using pivot() method
df11=pd.pivot_table(df, values='like',index=['Type','Category'])
print(df11)
