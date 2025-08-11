# Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# reading csv file
df = pd.read_csv("C:/Users/rasto/OneDrive/Desktop/Python for Data Analyst/Projects/Customer Churn.csv")
df.head()

# inspection of data
# print(df.info())

# Replacing the blanks with 0 as tenure is 0 and no total charges are recorded
df["TotalCharges"] = df["TotalCharges"].replace(" ","0")
df["TotalCharges"] = df['TotalCharges'].astype("float")

# print(df.info())

# checking null values
# print(df.isnull().sum())

# descriptive analysis
# print(df.describe())

# duplicate values
# print(df.duplicated().sum())

# checking for a unique column in our data
# print(df['customerID'].duplicated().sum())

# conversion in seniorcitizen
def conv(value):
    if value == 1:
        return "Yes"
    else:
        return "No"
    
df['SeniorCitizen'] = df["SeniorCitizen"].apply(conv)

# Churning in customer
ax = sns.countplot(x = df['Churn'],data=df)
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Churn")
plt.show()

gb = df.groupby("Churn").agg({'Churn':"count"})
# print(gb)
plt.pie(gb['Churn'],labels= gb.index, autopct="%1.2f%%")
plt.title("Percentage of Churned Customers")
plt.show()

# Exploration by Gender 
sns.countplot(x = 'gender',data=df, hue="Churn")
plt.title("Churn by Gender")
plt.show()

# Exploration by Senior Citizen
ax = sns.countplot(x = 'SeniorCitizen',data=df, hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Count of SeniorCitizen")
plt.show()

# Create crosstab of counts
ct = pd.crosstab(df['SeniorCitizen'], df['Churn'], normalize='index') * 100  # percentage per SeniorCitizen group

# Plot stacked bar
ax = ct.plot(kind='bar', stacked=True, figsize=(8, 5), colormap='coolwarm')

# Add labels
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%', label_type='center')

# Title & labels
plt.title("Churn by SeniorCitizen (Percentage)", fontsize=14)
plt.xlabel("SeniorCitizen")
plt.ylabel("Percentage (%)")
plt.legend(title="Churn")
plt.ylim(0, 100)  # because we're showing percentages
plt.tight_layout()
plt.show()


# Historogram
sns.histplot(x="tenure", data=df, bins=50, hue="Churn")
plt.show()

# People who stayed because of contract
ax = sns.countplot(x = 'Contract', data= df, hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Contract")
plt.show()

# Creating subplots
cols = [
    'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies'
]

# Set up subplot grid
n_cols = 3  # number of plots per row
n_rows = (len(cols) + n_cols - 1) // n_cols  # calculate needed rows

fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 4 * n_rows))
axes = axes.flatten()

for i, col in enumerate(cols):
    sns.countplot(x=col, data=df, ax=axes[i], palette="viridis", hue="Churn")
    axes[i].set_title(f"Count of {col}", fontsize=12)
    axes[i].set_xlabel("")
    axes[i].set_ylabel("Count")
    axes[i].tick_params(axis='x', rotation=45)  # rotate labels if needed

# # Remove unused subplots (if any)
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

# Churned Customer by PaymentMethod
plt.figure(figsize= (6,4))
ax = sns.countplot(x = 'PaymentMethod', data= df, hue="Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Churned Customers by Payment Method")
plt.xticks(rotation = 45)
plt.show()
