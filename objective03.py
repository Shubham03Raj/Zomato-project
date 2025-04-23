import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("zomato.csv", encoding='ISO-8859-1')

df_price_rating = df[['Price range', 'Aggregate rating']].dropna()

df_price_rating['Price range'] = pd.to_numeric(df_price_rating['Price range'], errors='coerce')
df_price_rating['Aggregate rating'] = pd.to_numeric(df_price_rating['Aggregate rating'], errors='coerce')

df_price_rating.dropna(inplace=True)

plt.figure(figsize=(8, 6))
df_price_rating.boxplot(column='Aggregate rating', by='Price range', grid=False, patch_artist=True,
                        boxprops=dict(facecolor='skyblue'))
plt.title('Aggregate Rating by Price Range')
plt.suptitle('')  
plt.xlabel('Price Range (1 = Low, 4 = High)')
plt.ylabel('Aggregate Rating')
plt.tight_layout()
plt.show()
