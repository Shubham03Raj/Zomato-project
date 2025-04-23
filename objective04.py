import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("zomato.csv", encoding='ISO-8859-1')

df_delivery = df[['Has Online delivery', 'Aggregate rating']].dropna()
df_delivery = df_delivery[df_delivery['Has Online delivery'].isin(['Yes', 'No'])]

df_delivery['Aggregate rating'] = pd.to_numeric(df_delivery['Aggregate rating'], errors='coerce')
df_delivery.dropna(inplace=True)

rating_by_delivery = df_delivery.groupby('Has Online delivery')['Aggregate rating'].mean()

plt.figure(figsize=(6, 6))
plt.pie(rating_by_delivery,
        labels=rating_by_delivery.index,
        autopct='%1.1f%%',
        colors=['lightcoral', 'mediumseagreen'],
        startangle=140,
        wedgeprops={'edgecolor': 'white'})

plt.title('Average Aggregate Rating\nOnline Delivery vs No Online Delivery')
plt.tight_layout()
plt.show()
