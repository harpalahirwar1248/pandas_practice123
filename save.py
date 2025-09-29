import pandas as pd

data = {

    "name":['ram',"sita","aryan","divya"],
    "Age" :["40","20","23","34"],
    "city":["nagpur","bhopal","panna","jabalpur"]

}

df = pd.DataFrame(data)
print(df)

df.to_excel("output.xlsx",index=False)