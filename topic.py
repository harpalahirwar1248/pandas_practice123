"""
1- how big is your datasets
2- what are your name of columns
"""

import pandas as pd
data = {
    "name":["siva","vijay",'satya','aryan','Harpal','divya'],
    "age":[12,34,9,21,17,19],
    "salary":[10000,50000,29999,700000,400000,4000],
    "performance":[10,50,80,85,90,30]
}
df = pd.DataFrame(data)
print(df)
print(f"shape: {df.shape}")
print(f"columns:{df.columns}")
import pandas as pd
data = {
    "name":["divya","vijay","raj","rita"],
    "age":["19","23","15","23"],
    "salary":[2100,8100,7899,6723]
}
df = pd.DataFrame(data)
print(df)
print(f"shape: {df.shape}")
print(f"column:{df.columns}")

df = pd.read_excel(""r"C:\Users\Asus\OneDrive\Documents\Custom Office Templates\April_23.xlsx")
print(df)
print(f"shape:{df.shape}")
print(f"columns:{df.columns}")