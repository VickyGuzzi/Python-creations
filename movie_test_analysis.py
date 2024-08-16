import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
title_basics = pd.read_csv('/Users/vickyguzzi/Downloads/SecurityAnalystExam_(1) (2)/title_basics_2018.csv')
title_ratings = pd.read_csv('/Users/vickyguzzi/Downloads/SecurityAnalystExam_(1) (2)/title_ratings.csv')
print(title_basics.head())
print(title_ratings.head())
print(title_basics.info())
print(title_ratings.info())

# Question 1: How Many 2018 Films Were Categorized as a Comedy?

# Filter for 2018 films that are comedies
comedy_films = title_basics[title_basics['genres'].str.contains('Comedy', na=False)]

# Count the number of comedy films
num_comedy_films = comedy_films.shape[0]
print(f"Number of 2018 comedy films: {num_comedy_films}")

# Question 2: How Many 2018 Films Got a Score of 8.0 or Higher?

# Merge the datasets on 'tconst'
merged_data = pd.merge(title_basics, title_ratings, on='tconst')

# Filter for 2018 films with a score of 8.0 or higher
high_rated_films = merged_data[(merged_data['averageRating'] >= 8.0)]

# Count the number of high-rated films
num_high_rated_films = high_rated_films.shape[0]
print(f"Number of 2018 films with a score of 8.0 or higher: {num_high_rated_films}")

# Question 3: What Was the Best Film of 2018?

# Find the best film(s) based on the highest average rating
best_films = merged_data[merged_data['averageRating'] == merged_data['averageRating'].max()]

# If there's a tie, choose based on the number of votes
best_film = best_films.loc[best_films['numVotes'].idxmax()]

print(f"The best film of 2018 is: {best_film['primaryTitle']} with a rating of {best_film['averageRating']}")

# Question 4: Do Audiences Prefer Longer Films or Shorter Films?

import matplotlib.pyplot as plt
import seaborn as sns

# Plot runtime vs. average rating
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_data, x='runtimeMinutes', y='averageRating')
plt.title('Runtime vs. Average Rating')
plt.xlabel('Runtime (minutes)')
plt.ylabel('Average Rating')
plt.show()

# Calculate correlation
correlation = merged_data['runtimeMinutes'].corr(merged_data['averageRating'])
print(f"Correlation between runtime and average rating: {correlation}")




