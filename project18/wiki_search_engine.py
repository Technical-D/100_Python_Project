# Wikipedia Search Engine for simple search
import requests
from bs4 import BeautifulSoup

def wiki_search(keyword):
    url = f"https://en.wikipedia.org/wiki/{keyword}"
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        paragraphs = soup.find_all('p')
        search_results = []
        for paragraph in paragraphs:
            if paragraph.text.strip(): 
                search_results.append(paragraph.text.strip())

        if not search_results or len(search_results) == 1:
            return "No information available for this topic."

        if len(search_results[0]) < 30 and len(search_results) > 1:
            return search_results[1]

        return search_results[0]

    except Exception as e:
        return f"An error occured: {e}"
            
print("Welcome to Wikipedia Search Engine!")

while True:
    keyword = input("\nEnter topic for search (q:quit): ").replace(' ', '_')
    
    if keyword.lower() == 'q':
        print("Goodbye!")
        break

    search_result = wiki_search(keyword)
    print(f"Search result: \n{search_result}")

