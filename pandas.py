
import pandas as pd
import numpy as np

# 1. List to Series Conversion
a = [10, 20, 30, 40, 50]
s = pd.Series(a)
print(s)


# 2. Generate Series of Dates
dates = pd.date_range(start='2021-05-01', end='2021-05-12')
print(dates)


# 3. Dictionary to DataFrame
data = {
    'Name': ['Anu', 'Binu', 'Cinu'],
    'Age': [20, 21, 22],
    'Mark': [80, 90, 85]
}
df = pd.DataFrame(data)
print(df)


# 4. 2D List to DataFrame
data = [
    ['Anu', 20, 80],
    ['Binu', 21, 90],
    ['Cinu', 22, 85]
]
df = pd.DataFrame(data, columns=['Name', 'Age', 'Mark'])
print(df)


# 5. Read CSV File into DataFrame
df = pd.read_csv('data.csv')
print(df)


# 6. Sort DataFrame by Multiple Columns
data = {
    'Name': ['Anu', 'Binu', 'Cinu', 'Divya'],
    'Age': [20, 21, 20, 22],
    'Mark': [80, 90, 95, 85]
}
df = pd.DataFrame(data)
df = df.sort_values(by=['Age', 'Mark'])
print(df)


# 7. Convert Custom Indexing to Default Indexing
data = {'Name': ['Anu', 'Binu', 'Cinu']}
df = pd.DataFrame(data, index=[10, 20, 30])
df = df.reset_index(drop=True)
print(df)


# 8. Select First 2 Rows
data = {
    'Name': ['Anu', 'Binu', 'Cinu'],
    'Mark': [80, 90, 85]
}
df = pd.DataFrame(data)
print(df.head(2))


# 9. Average Salary per Occupation
data = {
    'Name': ['Anu', 'Binu', 'Cinu', 'Divya'],
    'Occupation': ['Teacher', 'Doctor', 'Teacher', 'Doctor'],
    'Salary': [20000, 40000, 30000, 50000]
}
df = pd.DataFrame(data)
print(df.groupby('Occupation')['Salary'].mean())


# 10. Fill NaN Values with 0
data = {'Name': ['Anu', 'Binu', 'Cinu'],
        'Mark': [80, np.nan, 90]}
df = pd.DataFrame(data)
df = df.fillna(0)
print(df)


# 11. Convert Profit Values to Boolean
data = {
    'cname': ['A', 'B', 'C', 'D'],
    'profit': [1000, -500, 2000, -200]
}
df = pd.DataFrame(data)
df['profit'] = df['profit'] > 0
print(df)


# 12. Merge Two DataFrames
df1 = pd.DataFrame({
    'eid': [1, 2, 3],
    'ename': ['Anu', 'Binu', 'Cinu'],
    'stipend': [5000, 6000, 7000]
})

df2 = pd.DataFrame({
    'eid': [1, 2, 3],
    'designation': ['Manager', 'Developer', 'Tester']
})

df = pd.merge(df1, df2, on='eid')
df = df.rename(columns={'designation': 'position'})
print(df)
