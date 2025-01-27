import pandas as pd

# Sample data (replace with your actual data)
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Accessing data
print(df['Name'])  # Accessing a single column
print(df[['Name', 'Age']])  # Accessing multiple columns
print(df.loc[0])  # Accessing a row by label (index)
print(df.iloc[1])  # Accessing a row by position

# Filtering data
print(df[df['Age'] > 25])  # Filter rows where Age is greater than 25

# Sorting data
print(df.sort_values(by='Age'))  # Sort by 'Age' column

# Grouping and aggregation
print(df.groupby('City')['Age'].mean())  # Calculate average age for each city

# Adding a new column
df['Country'] = ['USA', 'UK', 'France', 'Japan']
print(df)

# Saving to CSV
df.to_csv('my_data.csv', index=False) 

# Loading from CSV
df_from_csv = pd.read_csv('my_data.csv')
print(df_from_csv)