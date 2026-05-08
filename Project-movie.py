# Pandas Fundamentals
#Creating DataFrames
#============ Example =================================
import pandas as pd

# Create movie dataset
movies_data = {
    'title': ['Inception', 'The Dark Knight', 'Interstellar', 'The Matrix', 'Pulp Fiction'],
    'year': [2010, 2008, 2014, 1999, 1994],
    'rating': [8.8, 9.0, 8.6, 8.7, 8.9],
    'genre': ['Sci-Fi', 'Action', 'Sci-Fi', 'Sci-Fi', 'Crime'],
    'duration_min': [148, 152, 169, 136, 154]
}

movies_df = pd.DataFrame(movies_data)

print("Movies DataFrame:")
print(movies_df)
print("\nDataFrame Info:")
movies_df.info()

#Basic DataFrame Operations
#============ Example =================================
# Accessing data
print("First 3 movies:")
print(movies_df.head(3))

print("\nMovie titles:")
print(movies_df['title'])

print("\nDescriptive statistics:")
print(movies_df.describe())



#Filtering and Selection
#============ Example =================================
# Filter movies after 2000
recent_movies = movies_df[movies_df['year'] > 2000]
print("Movies after 2000:")
print(recent_movies)

# High-rated Sci-Fi movies
high_rated_sci_fi = movies_df[(movies_df['genre'] == 'Sci-Fi') & (movies_df['rating'] > 8.5)]
print("\nHigh-rated Sci-Fi movies:")
print(high_rated_sci_fi)

# Using query method
long_movies = movies_df.query('duration_min > 150')
print("\nMovies longer than 150 minutes:")
print(long_movies)





#Sorting and Aggregation
#============ Example =================================
# Sort by rating (descending)
sorted_by_rating = movies_df.sort_values('rating', ascending=False)
print("Movies sorted by rating:")
print(sorted_by_rating)

# Group by genre
genre_stats = movies_df.groupby('genre').agg({
    'rating': ['mean', 'max', 'count'],
    'duration_min': 'mean'
})
print("\nGenre statistics:")
print(genre_stats)






#Handling Missing Data
#============ Example =================================
# Create dataset with missing values
movies_with_na = movies_df.copy()
movies_with_na.loc[2, 'rating'] = None
movies_with_na.loc[4, 'duration_min'] = None

print("Dataset with missing values:")
print(movies_with_na)

# Handle missing values
cleaned_movies = movies_with_na.fillna({
    'rating': movies_with_na['rating'].mean(),
    'duration_min': movies_with_na['duration_min'].median()
})
print("\nCleaned dataset:")
print(cleaned_movies)



#3. Real Movie Dataset Exploration
#Let's work with a more realistic dataset:
#============ Example =================================
# Create comprehensive movie ratings dataset
movie_ratings_data = {
    'movie_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 
              'Pulp Fiction', 'Forrest Gump', 'Inception', 'The Matrix', 'Goodfellas'],
    'release_year': [1994, 1972, 2008, 1994, 1994, 2010, 1999, 1990],
    'genre': ['Drama', 'Crime', 'Action', 'Crime', 'Drama', 'Sci-Fi', 'Sci-Fi', 'Crime'],
    'director': ['Frank Darabont', 'Francis Ford Coppola', 'Christopher Nolan',
                'Quentin Tarantino', 'Robert Zemeckis', 'Christopher Nolan', 
                'Lana Wachowski', 'Martin Scorsese'],
    'rating': [9.3, 9.2, 9.0, 8.9, 8.8, 8.8, 8.7, 8.7],
    'votes': [2500000, 1800000, 2400000, 2000000, 1900000, 2200000, 1700000, 1100000],
    'duration_min': [142, 175, 152, 154, 142, 148, 136, 146]
}

ratings_df = pd.DataFrame(movie_ratings_data)

# Advanced analysis
print("Dataset Overview:")
print(f"Total movies: {len(ratings_df)}")
print(f"Years range: {ratings_df['release_year'].min()} - {ratings_df['release_year'].max()}")

# Movies by genre
genre_counts = ratings_df['genre'].value_counts()
print("\nMovies by genre:")
print(genre_counts)

# Directors with multiple movies
director_stats = ratings_df['director'].value_counts()
print("\nDirectors with multiple movies:")
print(director_stats[director_stats > 1])

# Correlation analysis
correlation = ratings_df[['rating', 'votes', 'duration_min']].corr()
print("\nCorrelation matrix:")
print(correlation)



#Visualization (Bonus)
#============ Example =================================
import matplotlib.pyplot as plt

# Basic plots
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
ratings_df['genre'].value_counts().plot(kind='bar')
plt.title('Movies by Genre')

plt.subplot(1, 3, 2)
plt.scatter(ratings_df['release_year'], ratings_df['rating'])
plt.title('Rating vs Release Year')
plt.xlabel('Year')
plt.ylabel('Rating')

plt.subplot(1, 3, 3)
ratings_df['rating'].plot(kind='hist', bins=5)
plt.title('Rating Distribution')

plt.tight_layout()
plt.show()