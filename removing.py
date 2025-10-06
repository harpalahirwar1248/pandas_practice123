import pandas as pd
data = pd.read_excel(r"C:\Users\Asus\OneDrive\Documents\Custom Office Templates\April_23.xlsx")
df = pd.DataFrame(data)
print(df)

# df.drop(column=["column_name"], inplace=True
print("modified data")
df.drop(columns=["payment_method","Fooditem"], inplace=True)
print(df)