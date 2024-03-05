import pandas as pd
data={
    'name':['kowsalya','kurush','vglug','aravinth'],
    "age":[55,78,90,13]
    }
df=pd.DataFrame(data)
print(df)
print(df.loc[0])