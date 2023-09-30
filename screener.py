import requests
import re
from bs4 import BeautifulSoup
from bsedata.bse import BSE
b = BSE(update_codes = True)

pattern = r"^5\d{5}$"
base_url = input("Enter your Screener Screen Public Link : ")
#base_url = "https://www.screener.in/screens/1199674/newbegining/?page="

#pg = int(input("Enter no of pages in your Screen : "))

# URL to scrape
for page_number in range(1, 20):
    url =f'{base_url}{page_number}'
    print(url)

# Send a GET request to the URL
    response = requests.get(url)

# Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    rows = [row.find_all('td') for row in soup.find_all('tr')]
    #a = rows[1][1].a['href'].split("/")[2]
    
    length = len(rows)
    #print(length)
    for i in range(1, length-1):
        if i % 16 == 0 and i != 0:
            continue    
        company_names = rows[i][1].a['href'].split("/")[2]
        if re.match(pattern, company_names):
            q = b.getQuote(company_names)
            bs = q['securityID']
            print(bs)
            #print(type(print(q)))
        else:
            print(company_names)
        #stocks = nse.get_stock_codes()




