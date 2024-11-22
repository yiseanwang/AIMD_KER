import pandas as pd
import os

# 1.read in the csv file
df=pd.read_csv('bond_length.csv')  

#2. define the fragmentation rules
## H2O+ H2O+
cond1=df.loc[(df[' 0-3'] > 10) & (df[' 0-1'] < 2) & (df[' 0-2'] < 2) & (df[' 3-4'] < 2)  & (df[' 3-5'] < 2)]
count1=len(cond1)

## H3O+ OH+
cond2a=df.loc[(df[' 0-3'] > 10) & (df[' 0-1'] < 2) & (df[' 0-2'] < 2) & (df[' 0-5'] < 2)  & (df[' 3-4'] < 2)]
cond2b=df.loc[(df[' 0-3'] > 10) & (df[' 0-1'] < 2) & (df[' 0-2'] < 2) & (df[' 0-4'] < 2)  & (df[' 3-5'] < 2)]

cond2c=df.loc[(df[' 0-3'] > 10) & (df[' 0-1'] < 2) & (df[' 2-3'] < 2) & (df[' 3-4'] < 2)  & (df[' 3-5'] < 2)]
cond2d=df.loc[(df[' 0-3'] > 10) & (df[' 0-2'] < 2) & (df[' 1-3'] < 2) & (df[' 3-4'] < 2)  & (df[' 3-5'] < 2)]
count2=len(cond2a)+len(cond2b)+len(cond2c)+len(cond2d)

## H2O+ OH+ H | H2O+ OH H+
#                   0-3                O1-H2              #O1-H3             #O3-H5             #O3-H6              # O1-H6
cond3a=df.loc[(df[' 0-3'] > 10) & (df[' 0-1'] < 2) & (df[' 0-2'] < 2) & (df[' 3-4'] < 2)  & (df[' 3-5'] >3) & (df[' 0-5'] >3)]
cond3b=df.loc[(df[' 0-3'] > 10) & (df[' 0-1'] < 2) & (df[' 0-2'] < 2) & (df[' 3-5'] < 2)  & (df[' 3-4'] >3) & (df[' 0-4'] >3)]
#                   0-3                O4-H5              #O4-H6             #O1-H2             #O1-H3              # O1-H6
cond3c=df.loc[(df[' 0-3'] > 10) & (df[' 3-4'] < 2) & (df[' 3-5'] < 2) & (df[' 0-1'] < 2)  & (df[' 0-2'] >3) & (df[' 2-3'] >3)]
cond3d=df.loc[(df[' 0-3'] > 10) & (df[' 3-4'] < 2) & (df[' 3-5'] < 2) & (df[' 0-2'] < 2)  & (df[' 0-1'] >3) & (df[' 1-3'] >3)]
count3=len(cond3a)+len(cond3b)+len(cond3c)+len(cond3d)
#cond3=cond2.loc[df['0-2'] < 2]
#cond4=cond3.loc[df['3-4'] < 2]
#cond5=cond4.loc[df['3-5'] < 2]
print(os.getcwd().split("/")[-3])
print("H2O+ H2O +: ",count1)
print("H3O+ OH+ :", count2)
print("H2O+ OH+ H : ", count3)
#cond3=cond2.describe() #3. count it 計算
#cond3.to_csv('count.csv') # index=False可以移除第一行
