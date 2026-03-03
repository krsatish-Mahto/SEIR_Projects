#  Python Project
# PART-1:
# ○ Write a python program that takes a URL on the command line, fetches the page, and 
# outputs (one per line)
# ■ Page Title (without any HTML tags)
# ■ Page Body (without any html tags)
# ■ All the URLs that the page points/links to




import requests
import sys
from bs4 import BeautifulSoup

def fetch_data(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url="https://" +url

    user={"User-Agent":"Mozilla/5.0"}
    try:
        response=requests.get(url, headers=user, timeout=10)
        response.raise_for_status()
    except requests.exceutions.RequestException as e:
        print("Error found during fetching URL:",e)
        return 
    soup=BeautifulSoup(response.text,'html.parser')

    titles=soup.find('title')
    print("\n \n \n")
    print(".........................PAGE TITLES:.................................................................\n")
    if titles:
        print(titles.string)
    else:
        print("No title found.")

    
    print("\n \n \n")
    print("..........................................BODY TEXTS :....................................................\n")
    if soup.body:
        body_text = soup.body.get_text(" ", strip=True)
        print(body_text)
    else:
        print("Body not found in this webpage.")


    links = soup.find_all("a", href=True)
    print()
    print("..........................................................LINKS:....................................................................... \n")
    print("\n \n \n")
    
    for link in links:
        href=link.get("href")
        print(href)

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Give input in correct format:\n eg: python script.py <url>") 
        sys.exit(1)  
    
    url =sys.argv[1]
    fetch_data(url)
# fetch_data('https://www.cricbuzz.com/')