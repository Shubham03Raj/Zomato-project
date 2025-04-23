import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("zomato.csv", encoding='ISO-8859-1')

df = df[['City', 'Average Cost for two']].dropna()
df['Average Cost for two'] = pd.to_numeric(df['Average Cost for two'], errors='coerce')
df = df.dropna()

city_avg_cost = df.groupby('City')['Average Cost for two'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
city_avg_cost.plot(kind='barh', color='coral')
plt.title('Top 10 Cities with Highest Average Cost for Two')
plt.xlabel('Average Cost for Two')
plt.ylabel('City')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
