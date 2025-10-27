import pandas as pd
from wordcloud import WordCloud
import matplotlib.pylab as plt

df = pd.read_csv(r"C:\Users\Amruta\Desktop\Netfkix_EDA\Netflix\netflix_titles.csv")
print("\n\nFirst five rows of the data: \n\n",df.head())
print("\n\nShape of the data: \n\n",df.shape)
print("\n\nDescription of the data: \n\n",df.describe())
df.info()

#finding null values
print("\n\n",df.isnull().sum())

#handling missing values null values
df['director']= df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = df['date_added'].fillna(df['date_added'].mode()[0])
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
df['duration'] = df['duration'].fillna(df['duration'].mode()[0])
print(df.isnull().sum())

print(df.nunique())   # to see unique counts
print(df.duplicated().sum())  # check duplicate rows
df.drop_duplicates(inplace=True)

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

#Content Added Over Time
df['year_added'] = df['date_added'].dt.year
df['year_added'].value_counts().sort_index().plot(kins='bar',figsize=(10,5), color='lightblue')
plt.title('Content Added to Netfix Over the Years')
plt.xlabel('Year Added')
plt.ylabel('Number of Titles')
plt.show()

#Movies vs TV Shows count
df['type'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Movies vs TV Shows')
plt.ylabel("")
plt.show()


#Most common genres
df['listed_in'].str.split(",").explode().str.strip().value_counts().head(10)
genres = df['listed_in'].str.split(",").explode().str.strip().fillna("")
text = " ".join(genres)
wordcloud = WordCloud(width=800, height=400, background_color="black", colormap="Set2").generate(text)
plt.figure(figsize=(10,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

#Top 10 countries producing Tv shows vs Movies
top_countries = df.groupby(['country','type']).size().unstack().fillna(0)
top_countries = top_countries.sum(axis=1).sort_values(ascending=False).head(10).index
filtered = df[df['country'].isin(top_countries)]

plt.figure(figsize=(10,5))
filtered.groupby(['country','type']).size().unstack().plot(kind='bar', stacked=True, figsize=(10,5), color=['#66b3ff','#99ff99'])
plt.title('Top 10 Countries by Content Type')
plt.ylabel('Number of Titles')
plt.show()


#Most frequent directors/actors
print("\n\nMost frequent directors/actors\n\n",df['director'].value_counts().head(10))

#Most frequent directors/actors
print("\n\nMost frequent directors/actors\n\n",df['cast'].str.split(',').explode().value_counts().head(10))

#Year-wise content release trend
df['release_year'].value_counts().sort_index().plot(kind='line')
plt.title('content growth over years')
plt.xlabel('year')
plt.ylabel('Number of Titles')
plt.show()

#most common rating per type
plt.figure(figsize=(10,5))
df.groupby(['type','rating']).size().unstack().fillna(0).T.plot(kind='bar', figsize=(10,6))
plt.title('Content Ratings by Type')
plt.ylabel('Number of Titles')
plt.show()

