import requests
from bs4 import BeautifulSoup
import pandas



request = input("Request: ") # Getting request from user
link = f'/search?q={request}' # Create the link for google search query

# Initialize some information for search engine
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
}


row_domen, row_title = [],[] # Creating lists with information for xlsx or csv file
while True:
    try:
        URL_REQUEST = f'https://www.google.com{link}'
        web_request = requests.get(URL_REQUEST, headers=headers) # Getting a page by URL_REQUEST
        src =  web_request.text

        soup = BeautifulSoup(src, 'lxml') # Format a page to bs4 format
        # searching_class = soup.body.find('div', id='search').a.parent['class'] # learn a name of block
                                                                                # with title of responce
        search_results = soup.find_all('div', class_='yuRUbf') # Get a list with all responces on the page

        for result in search_results: # Сonsider each block separately
            result_href = result.a['href'] # Get a responce's URL
            result_string = result.a.h3.string # Get a responce's title
            row_domen.append(result_href) # Add datas into domen list for table
            row_title.append(result_string) # Add datas into title list for table
            print(result_string,': ',result_href,'\n') # Print obtained title and URL for debugging

        next_page_href = soup.find('a',id='pnnext') # Get a URL to next page
        link = next_page_href.get("href") # Creat a new link for next page
    except:
        break
# The loop works until the pages are finished via try except construction


# Creating a excel table
df = pandas.DataFrame({
    'Domen': row_domen,
    'Title': row_title
})
df.to_excel('./docx.xlsx')

print('\n________________CLOSED________________') # Information about program status