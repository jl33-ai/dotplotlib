# Let's start from the beginning with improved code
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'axes.facecolor': 'lavender'})  # Background color for the plot
%matplotlib inline

# Get data
ratings = pd.read_csv('ratings.csv', encoding='iso8859')

# Sort values by rating
ratings = ratings.sort_values(by=['Your Rating'])

# Loop to create a new variable, which will turn scatterplot to a dot plot
movie_count = []

for index, year in enumerate(ratings['Year']):
    subset = ratings.iloc[:index + 1]  # Create subset starting at the beginning of dataset until the movie itself
    count = len(subset[subset['Year'] == year])  # Count all movies from the same year in this subset
    movie_count.append(count)  # Appended counts will be used as vertical values in the scatterplot,
    # which will help to create a dot plot

# Data for the plot
x = ratings['Year']
y = movie_count
hue = ratings['Your Rating']

# Dot plot created using scatter plot
plt.figure(figsize=(15, 10))
ax = sns.scatterplot(x, y, hue=hue, s=60, legend="full", palette="RdYlGn")
ax.grid(False)  # Remove grid
ax.get_legend().remove()  # Delete default legend
scale_legend = plt.Normalize(hue.min() - 1, hue.max())  # Create a scale for the colormap.
# hue.min-1 because I never rated a movie 1/10, but still wanted to create a consistent color map.
color_map = plt.cm.ScalarMappable(cmap="RdYlGn", norm=scale_legend)  # Colormap used in legend.
color_map.set_array([])  # Dummy variable needed to create a colormap.
ax.figure.colorbar(color_map)  # Add colormap as a legend.
plt.xlim([1950, 2020])  # There are just few movies I seen from before 1950.
plt.ylabel("Count", size=14)
plt.xlabel("Release year", size=14)
plt.title("Movies seen by year and rating", size=20)
plt.gcf().text(0.83, 0.5, "Rating", fontsize=14, rotation=90)  # Label used for colormap.
plt.show()
