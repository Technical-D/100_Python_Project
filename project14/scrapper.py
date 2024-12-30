# Wikipedia Scrapper
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"  

response = requests.get(url)
response.raise_for_status()  

soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', {'class': 'wikitable'})

dataframes = []
for i, table in enumerate(tables):
    df = pd.read_html(str(table))[0]
    dataframes.append(df)
    print(f"Table {i + 1} extracted with shape: {df.shape}")

for idx, df in enumerate(dataframes):
    filename = f"table_{idx + 1}.csv"
    df.to_csv(filename, index=False)
    print(f"Table {idx + 1} saved as {filename}")

print(dataframes[0].head())