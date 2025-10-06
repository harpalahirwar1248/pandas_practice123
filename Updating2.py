import pandas as pd
data = pd.read_excel(r"C:\Users\Asus\OneDrive\Documents\Custom Office Templates\April_23.xlsx")

df = pd.DataFrame(data)
print(df)

# increment salary by 5%
df["quantity"]=df["quantity"]*0.10
print(df)


