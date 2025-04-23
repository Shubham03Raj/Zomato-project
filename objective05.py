import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("zomato.csv", encoding='ISO-8859-1')

filtered_df = df[df['Aggregate rating'] > 0]

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.countplot(
    x='Aggregate rating',
    data=filtered_df,
    palette='Blues_d',
    order=sorted(filtered_df['Aggregate rating'].unique())
)

plt.title('Distribution of Restaurant Ratings', fontsize=16)
plt.xlabel('Aggregate Rating', fontsize=12)
plt.ylabel('Number of Restaurants', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
