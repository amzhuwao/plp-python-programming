#!/usr/bin/python3
import matplotlib.pyplot as plt

"""
🧪 Practice Tasks
    Create a bar chart showing 5 different countries and their population.

    Create a pie chart showing how a student spends 24 hours of their day.

    Make a line chart that shows temperature changes during the day (morning, noon, evening, night).
"""

# Bar chart: 5 countries and their population
countries = ['USA', 'India', 'China', 'Brazil', 'Nigeria']
populations = [331, 1391, 1441, 213, 206]  # Population in millions

plt.figure(figsize=(8, 5))
plt.bar(countries, populations, color='skyblue')
plt.title('Population of 5 Countries')
plt.xlabel('Countries')
plt.ylabel('Population (in millions)')
plt.show()

# Pie chart: How a student spends 24 hours
activities = ['Sleep', 'Study', 'Leisure', 'Exercise', 'Others']
hours = [8, 6, 5, 2, 3]

plt.figure(figsize=(6, 6))
plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightblue', 'pink', 'lightgreen', 'orange'])
plt.title('How a Student Spends 24 Hours')
plt.show()

# Line chart: Temperature changes during the day
times = ['Morning', 'Noon', 'Evening', 'Night']
temperatures = [20, 30, 25, 18]  # Temperatures in °C

plt.figure(figsize=(8, 5))
plt.plot(times, temperatures, marker='o', color='red', linestyle='--')
plt.title('Temperature Changes During the Day')
plt.xlabel('Time of Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

