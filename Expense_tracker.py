# Expense Tracker Analysis
import pandas as pd
import seaborn  as sns
import matplotlib.pyplot as plt


data = {
    'Date':['2026-06-01','2026-06-02','2026-06-03','2026-06-04','2026-06-05','2026-06-06'],
    'Category':['Food','Travel','Shopping','Food','Bills','Travel'],
    'Amount':[200,100,1500,250,800,120]
}

df = pd.DataFrame(data)

print("Total expense:",df['Amount'].sum())

print("Highest expense:\n",df.loc[df['Amount'].idxmax()])

print("Lowest expense:\n",df.loc[df['Amount'].idxmin()])

print("Expense above ₹500:\n",df[df['Amount']>500])

category_expense = df.groupby('Category')['Amount'].sum()
print(category_expense)

print("Average expense:",df['Amount'].mean())

df['Expense_type'] = df['Amount'].apply(
   lambda x:'High' 
   if x >=500 
   else 'Normal'
)
print(df)

category_data = category_expense.reset_index()
sns.barplot(x = 'Category', y = 'Amount',data = df)
plt.title("Category wise Expense")
plt.show()

sns.histplot(df['Amount'],bins = 5,kde = True)
plt.title("Expense Distibution")
plt.show()

sns.countplot(x = 'Expense_type',data = df)
plt.title('Expense vs normal')
plt.show()

Highest_category = df.groupby('Category')['Amount'].sum().idxmax()
print(Highest_category)