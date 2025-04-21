#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import os


# Download or create a CSV file called sales_data.csv

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the file
file_path = os.path.join(script_dir, "sales_data.csv")

#Load the CSV file using pandas.
sales_data = pd.read_csv(file_path)

#Calculate the total revenue.
print(f'Total Revenue:\n {sales_data['Revenue'].sum()}')

#Find the best-selling product (based on Quantity Sold).
max = sales_data.groupby('Product')['Order_Quantity'].sum().reset_index()
max_sales = max.max()

print(f'Max sales: \n{max_sales}')

#Identify the day with the highest sales.
sales = sales_data.groupby('Date')['Revenue'].sum().reset_index()
highest_sales = sales.max()

print(f'Highest Sales Date: \n{highest_sales}')

#Save the results to a new file called sales_summary.txt.
my_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sales_summary.txt')
with open(my_path, "w") as f:
    f.write(f'Total Revenue:\n {sales_data['Revenue'].sum()} \n\nMax sales: \n{max_sales} \n\nHighest Sales Date: \n{highest_sales}')

#Print the insights in a user-friendly format.

#Visualize sales trends using matplotlib or seaborn.

# Plotting a pie chart for the monthly sales trends
trend = sales_data.groupby('Month')['Revenue'].sum().reset_index()
plt.figure(figsize=(12, 12))
plt.pie([x for x in pd.to_numeric(trend['Revenue'])], labels = [x for x in trend['Month']], autopct='%1.1f%%', startangle=90,)
plt.title('Sales Trends')
plt.show()

# Plotting a bar chart for the Order Quantity
sales_data.groupby('Sub_Category')['Order_Quantity'].sum().plot(kind='bar')
plt.xlabel('Product')
plt.ylabel('Average Order_Quantity')
plt.title('Sales Trends')
plt.show()