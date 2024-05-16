Sure! Here is a basic Python code template for web scraping using the requests and BeautifulSoup libraries:

```python
import requests
from bs4 import BeautifulSoup

# Specify the URL to scrape
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract and process the desired information
    # Example: find all <a> tags and print the href attribute
    for link in soup.find_all('a'):
        print(link.get('href'))
        
else:
    print('Failed to retrieve page. Status code:', response.status_code)
```

Remember to install the required libraries (`requests` and `beautifulsoup4`) using pip before running the code.

Let me know if you need more assistance with web scraping or any other topic!