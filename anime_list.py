# Anime List
import pandas as pd

file_path = "AnimeList.csv"
df = pd.read_csv(file_path)

# Display the first 5 rows
df.head()

# Get column names.
df.columns

# Summary of the DataFrame.
df.info()

# Statistical summary.
df.describe()

# Data types of columns.
df.dtypes

# Get rows and columns count.
df.shape

# Check for missing values.
print(df.isnull())