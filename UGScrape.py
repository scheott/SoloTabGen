import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape a single tab page
def scrape_tab(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the title of the tab
    title = soup.find('h1', class_='t_title').get_text(strip=True)
    
    # Extract the tab content
    tab_content = soup.find('pre', class_='js-tab-content').get_text(strip=True)
    
    return title, tab_content

# Function to scrape the tabs from search results
def scrape_search_results(search_query, num_tabs=10):
    base_url = 'https://www.ultimate-guitar.com'
    search_url = f'{base_url}/search.php?search_type=title&value={search_query}'
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all tab links in the search results
    tab_links = []
    for link in soup.find_all('a', class_='js-tp_link'):
        tab_links.append(base_url + link['href'])
        if len(tab_links) >= num_tabs:
            break
    
    tabs = []
    for link in tab_links:
        try:
            title, content = scrape_tab(link)
            tabs.append({'title': title, 'content': content})
        except Exception as e:
            print(f'Error scraping {link}: {e}')
    
    return tabs

# Save the scraped data to a CSV file
def save_to_csv(tabs, filename='guitar_tabs.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'content'])
        writer.writeheader()
        for tab in tabs:
            writer.writerow(tab)

# Example usage
if __name__ == '__main__':
    search_query = 'Metallica'
    tabs = scrape_search_results(search_query, num_tabs=5)
    
    # Print out the tabs before saving
    for tab in tabs:
        print(f"Title: {tab['title']}")
        print(f"Content:\n{tab['content']}\n")
        print("-" * 40)  # Separator between tabs

    # Save the tabs to a CSV file
    # save_to_csv(tabs)
    print(f'Scraped {len(tabs)} tabs and saved to guitar_tabs.csv')
