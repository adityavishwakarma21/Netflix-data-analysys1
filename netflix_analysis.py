# Netflix_Analysis.py

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
df = pd.read_csv("netflix_titles.csv")

# Check data
print(df.head())
print(df.info())

# Content type count
type_count = df['type'].value_counts()
plt.figure(figsize=(6, 4))
sns.barplot(x=type_count.index, y=type_count.values, palette='viridis')
plt.title("Count of Movies vs TV Shows on Netflix")
plt.ylabel("Count")
plt.xlabel("Type")
plt.savefig("type_distribution.png")
plt.show()

# Top 10 countries content
country_count = df['country'].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=country_count.index, y=country_count.values, palette='magma')
plt.title("Top 10 Countries with Most Content")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig("top_countries.png")
plt.show()

# Content added per year
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year
year_count = df['year_added'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x=year_count.index, y=year_count.values, marker='o')
plt.title("Content Added to Netflix by Year")
plt.ylabel("Number of Titles")
plt.xlabel("Year")
plt.savefig("content_trend.png")
plt.show()

# Top genres
df['listed_in'] = df['listed_in'].astype(str)
all_genres = ','.join(df['listed_in']).split(',')
genre_series = pd.Series(all_genres).value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_series.values, y=genre_series.index, palette='coolwarm')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Count")
plt.savefig("top_genres.png")
plt.show()