from bs4 import BeautifulSoup
import requests
import random

user_agents = [
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'

]


# Describing Scrapping functions to get imported in main
# query is the input
def web_request(query):  

    google_base_link = 'https://www.google.com/search?ei=LBEuYI-mEMyAyAPx26uICA&q={}&oq={}&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAELEDMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgoIABDqAhC0AhBDOgoILhDqAhC0AhBDOgQIABBDOgoIABCxAxCDARBDOggIABCxAxCDAToCCC46BwguEEMQkwI6BwgAELEDEEM6BAguEEM6BwgAEMkDEEM6BQgAEJIDOgUIABCRAjoECAAQA1DNcViwhAFggYYBaAFwAngAgAGXAogBnhKSAQYwLjEzLjKYAQCgAQGqAQdnd3Mtd2l6sAEKwAEB&sclient=gws-wiz&ved=0ahUKEwiP7Kbs7vLuAhVMAHIKHfHtCoEQ4dUDCA0&uact=5'
    header = {
        'User-Agent' : random.choice(user_agents)
    }

    # in google_base_link two format{} are given which are filled with query using below
    google_response = requests.get(google_base_link.format(query, query), headers=header, allow_redirects=True)
    return google_response.text

def scrape_data(response):
    page_object = BeautifulSoup(response,'html.parser')
    head_response = page_object.find_all('dev',{'class': 'xpdopen'})

    try:
        side_response = page_object.find('div',{'class': 'kno-rdesc'})
        question_response = side_response.find_all('span')[0].text
    
    except AttributeError :
        question_response = " "

    return question_response
