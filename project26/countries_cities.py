import json

with open('countries+cities.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

country_city_mapping = {}

for country in data:
    country_name = country['name']
    cities = [city['name'] for city in country['cities']]
    country_city_mapping[country_name] = cities

# Step 3: Write the transformed data to a new JSON file
with open('country_city_mapping.json', 'w', encoding='utf-8') as outfile:
    json.dump(country_city_mapping, outfile, indent=4)

print("Data has been written to 'country_city_mapping.json'")
