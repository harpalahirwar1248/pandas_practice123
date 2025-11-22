import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Asus\Downloads\WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(df)

df.info()

df["TotalCharges"] = df["TotalCharges"].replace(" ","0")
df["TotalCharges"] = df["TotalCharges"].astype("float")

df.info()

## ham isnull function ka use null value ko dekhane
# ke liye karte hai or count karna ho to sum function add kar do
print(df.isnull())
print(df.isnull().sum())

### ham describe function ka use count,std,min,mean etc.
# dekhane ke liye karte hai

print(df.describe())

##  aab ham duplicate data check kare ge duplicated function se

print(df.duplicated().sum())

## aab jaise aapne ko column based check karna hoto

print(df["customerID"].duplicated().sum())

# aab ham vo logic lagaye ge Seniorcitizen ki jo 1 or 0 value hai
# aab ham unko yes or no me change kare ge

def conv(value):
    if value == 1:
        return "yes"
    else:
        return "no"
df['SeniorCitizen'] = df["SeniorCitizen"].apply(conv)
ax = sns.countplot(x = 'Churn',data = df)

# ham bar ki value show ke liye
ax.bar_label(ax.containers[0])
plt.title("Count of customers by Churn")

plt.show()
## size ke liye figure function ka use kare ge
plt.figure(figsize=(3,4))
gb = df.groupby("Churn").agg({'Churn':"count"})
plt.title("percentage of churned customers",fontsize = (10) )
print(gb)

plt.pie(gb['Churn'], labels=gb.index,autopct = "%1.2f%%")
plt.show()

"""
aab jo pie chart ka conclude that 26.54% of our customer have churned out
# not let's explore the reason behind it

"""

plt.figure(figsize= (7,3))
sns.countplot(x= 'gender',data = df,hue='Churn')
plt.title("Churn by gender")
plt.show()

# aaab ham senior citizen

plt.figure(figsize=(7,3))
ax = sns.countplot(x = "SeniorCitizen",data = df)
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Senior citizen")
plt.show()

# Crosstab (count)
ct = pd.crosstab(df['SeniorCitizen'], df['Churn'])

# Convert to percentage row-wise
ct_percent = ct.div(ct.sum(axis=1), axis=0) * 100

# Plot stacked bar chart
ax = ct_percent.plot(kind='bar', stacked=True, figsize=(6,4))

plt.title("Senior Citizen vs Churn (%)")
plt.ylabel("Percentage")
plt.xlabel("Senior Citizen")

# Add percentage labels inside bars
for container in ax.containers:
    for bar in container:
        height = bar.get_height()
        if height > 0:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_y() + height / 2,  # center of each bar segment
                f"{height:.1f}%",
                ha='center', va='center', color='black'
            )

plt.legend(title="Churn")
plt.tight_layout()
plt.show()



#  customers company ke saath kitne months se connected hain.


#Yeh histogram dikhata hai ki customers company ke saath kitne months ya year
#tak rahe (tenure), aur har tenure range me churn kitna hua.”

plt.figure(figsize=(9,4))
sns.histplot(x= 'tenure',data = df,bins=72,hue="Churn")
plt.show()

plt.figure(figsize=(9,3))
ax = sns.countplot(x = "Contract",data = df , hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Contract")
plt.show()

print(df.columns.values)


cat_cols = [
    'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
    'StreamingMovies'
]

# Fix all "No internet service" categories
for col in cat_cols:
    df[col] = df[col].replace("No internet service", "No")


cols = 3
rows = (len(cat_cols) + cols - 1) // cols
fig, axes = plt.subplots(rows, cols, figsize=(18, rows * 4))
axes = axes.flatten()


for i, col in enumerate(cat_cols):
    sns.countplot(x=col, data=df, hue='Churn', ax=axes[i])

    axes[i].set_title(f"{col} Countplot", fontsize=12, fontweight='bold')
    axes[i].tick_params(axis='x', labelrotation=20)
    axes[i].set_xlabel("")
    axes[i].grid(False)

plt.tight_layout(pad=3)
plt.show()




plt.figure(figsize=(6,4))
ax = sns.countplot(x='PaymentMethod', data=df, hue="Churn")

ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])

plt.title("Churned Customers by payment Method")
plt.xticks(rotation=90)
plt.show()









