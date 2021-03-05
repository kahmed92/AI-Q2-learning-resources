#Q1.
import pandas as pd, numpy as np
df=pd.read_csv("states0.csv")
Male=df["GenderPop"].str.split("_")
df.GenderPop.str.split('_')
gender_split = df.GenderPop.str.split('_')
df["Male"],df["Female"]=(gender_split.str.get(0)).str[:-1],(gender_split.str.get(1)).str[:-1]
del df["GenderPop"]
del df["Unnamed: 0"]
df["Income"]=df["Income"].str[1:].astype("float")
df["WomenProp"]=df["TotalPop"]/df["Female"].astype("int32")
df.plot(x="Income", y=['WomenProp'],kind="scatter")


#Q2.
import glob, pandas as pd
df=pd.DataFrame([])
for name in glob.glob('C:\\Users\Kaleem Ahmed\states?.csv'): 
    df1=pd.read_csv(name,index_col=[0])
    df=pd.concat([df,df1], axis=0).reset_index(drop=True)
df.to_csv('us_census.csv')
df2=pd.read_csv('us_census.csv',index_col=[0])
df2.head()

#Q3.
df2.columns
df2.dtypes
df2["White"]=df2["White"].str[:-1].astype("float")
df2["White"]=df2["White"]/df2["White"].max()
df2.hist("White")


#Q4.
df2["Hispanic"]=df2["Hispanic"].str[:-1].astype("float")
df2["Black"]=df2["Black"].str[:-1].astype("float")
df2["TotalPop"]=df2["TotalPop"].astype("int32")
df2["Native"]=df2["Native"].str[:-1].astype("float")
df2["Asian"]=df2["Asian"].str[:-1].astype("float")
df2["Pacific"]=df2["Pacific"].str[:-1].astype("float")
df2["Income"]=df2["Income"].str[1:].astype("float")
gender_split = df2["GenderPop"].str.split('_')
df2["Male"],df2["Female"]=(gender_split.str.get(0)).str[:-1],(gender_split.str.get(1)).str[:-1]
del df2["GenderPop"]
df2

#Q5.
import re
df2["Income"]=[re.sub('[$]', '',i) for i in df2["Income"].astype("str")]

#Q6.
gender_split = df2.GenderPop.str.split('_')
df2["Men"],df2["Women"]=(gender_split.str.get(0)),(gender_split.str.get(1))

#Q7.
df2["Men"]=df2["Men"].str[:-1]
df2["Women"]=df2["Women"].str[:-1]

#Q8.
import  matplotlib.pyplot as plt 
plt.scatter(df2["State"],df2["TotalPop"])
plt.legend()
plt.show()

#Q9.
df2["Women"]=df2["TotalPop"].astype('int32')-df2["Men"].astype('int32')

#Q10.
df2[df2.duplicated()]

#Q11.
df2.drop_duplicates()

#Q12.
import  matplotlib.pyplot as plt 
plt.scatter(df2["TotalPop"],df2["Women"])
plt.legend()
plt.show()

#Q13.
df2.columns


#Q14.
df2["Hispanic"]=df2["Hispanic"].str[:-1].astype("float")
df2["Black"]=df2["Black"].str[:-1].astype("float")
df2["TotalPop"]=df2["TotalPop"].astype("int32")
df2["Native"]=df2["Native"].str[:-1].astype("float")
df2["Asian"]=df2["Asian"].str[:-1].astype("float")
df2["Pacific"]=df2["Pacific"].str[:-1].astype("float")
df2["Income"]=df2["Income"].str[1:].astype("float")
gender_split = df2["GenderPop"].str.split('_')
df2["Male"],df2["Female"]=(gender_split.str.get(0)).str[:-1],(gender_split.str.get(1)).str[:-1]
del df2["GenderPop"]
df2.drop_duplicates()

import  matplotlib.pyplot as plt 
plt.scatter(df2["TotalPop"].astype("int32"),df2["Hispanic"].str[:-1].astype("float")*df2["TotalPop"].astype("int32")/100)
plt.scatter(df2["TotalPop"].astype("int32"),df2["Black"].str[:-1].astype("float")*df2["TotalPop"].astype("int32")/100)
plt.scatter(df2["TotalPop"].astype("int32"),df2["Native"].str[:-1].astype("float")*df2["TotalPop"].astype("int32")/100)
plt.scatter(df2["TotalPop"].astype("int32"),df2["Asian"].str[:-1].astype("float")*df2["TotalPop"].astype("int32")/100)
plt.scatter(df2["TotalPop"].astype("int32"),df2["Pacific"].str[:-1].astype("float")*df2["TotalPop"].astype("int32")/100)
plt.show()

#Q1.
import glob, pandas as pd
df=pd.read_csv('inventory.csv',index_col=[0])

#Q2.
df.head(10)

#Q3.
df.head(10).to_csv('staten_island.csv')

#Q4.
df2=pd.read_csv('staten_island.csv',index_col=[0])
product_request=df2["product_description"]
product_request

#Q5.
df3=pd.read_csv('inventory.csv',index_col=[0])
seed_request=df3.query('location=="Brooklyn" and product_type=="seeds"')
print(seed_request)

#Q6.
df3["in_stock"]=df3["quantity"]>0

#Q7.
df3["total_value"]=df3["quantity"]*df3["price"]

#Q8.
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

#Q9.
df3["full_description"]=df3.apply(combine_lambda,axis=1)
