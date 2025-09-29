#head() tall()
#head() 5
#tall()

import pandas as pd

df = pd.read_excel(r"C:\Users\Asus\OneDrive\Documents\Custom Office Templates\April_23.xlsx")

print('display 8 rows of first')
print(df.head(8))


print("display 8 rows of Last")
print(df.tail(8))
print("display the 8 rows and the ")
