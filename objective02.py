import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("zomato.csv", encoding='ISO-8859-1')

city_counts = df['City'].value_counts().head(10)

plt.figure(figsize=(10, 6))
city_counts.plot(kind='bar', color='coral')
plt.title('Top 10 Cities with the Most Restaurants')
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
