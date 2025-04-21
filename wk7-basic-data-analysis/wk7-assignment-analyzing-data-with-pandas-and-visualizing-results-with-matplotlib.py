#usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import os


# Download, create or load a CSV file called iris.csv'.csv

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the file
file_path = os.path.join(script_dir, "iris.csv")

#Load the CSV file using pandas.

try:
    iris_data = pd.read_csv(file_path)
    iris_data.drop_duplicates()
    iris_data.fillna()
    
    iris_data['sepal_length'] = iris_data['sepal_length'].astype(float)
    iris_data['sepal_width'] = iris_data['sepal_width'].astype(float)
    iris_data['petal_length'] = iris_data['petal_length'].astype(float)
    iris_data['petal_width'] = iris_data['petal_width'].astype(float)
    iris_data['setosa'] = iris_data['setosa'].astype(str)

    print("✅ File opened successfully :)")

except FileNotFoundError:
    print("❌ Error: The file was not found.")
    
except IOError:
    print("❌ Error: Unable to read or write the file.")
    
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    
print(f'{iris_data.head()}')
print(f'{iris_data['sepal_length'].describe().round(2)}')

iris = iris_data.groupby('species')['petal_length'].mean().reset_index()
print(f'Petal Length Data: \n{iris}')

#Line chart showing trends over time (for example, a time-series of sales data).
iris.plot(kind='line')
plt.xlabel(iris.columns[0])
plt.ylabel(iris.columns[1])
plt.title('Average Petal Length')
plt.show()

# Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species).
iris.plot(kind='bar')
plt.xlabel(iris.columns[0])
plt.ylabel(iris.columns[1])
plt.title('Average Petal Length')
plt.show()


# Histogram of a numerical column to understand its distribution.

# Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).
plt.scatter(iris_data['sepal_length'] , iris_data['petal_length'])
plt.title('sepal length vs. petal length')
plt.show()