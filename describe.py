import pandas as pd
data = {
    "name":["ram",'satya','aryan','shiva','Harpal','sita'],
    "age":[12,34,19,17,19,16],
    "salary":[12000,17000,50000,30000,55000,9000],
    "performance score":[20,27,60,40,67,17]
}
df = pd.DataFrame(data)
print(""r"C:\Users\Asus\OneDrive\Documents\Custom Office Templates\April_23.xlsx")
print(df)
print('descriptive statistics')
print(df.describe())