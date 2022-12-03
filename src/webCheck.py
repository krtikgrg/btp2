import requests
from bs4 import BeautifulSoup as bs
import warnings
import time
from googlesearch import search as gsearch

warnings.filterwarnings("ignore", module='bs4')
ctr = 0


def search(query, num):
    # global ctr
    # url = 'https://www.google.com/search?q=' + query
    # urls = []
    # ctr += 1    
    # page = requests.get(url, headers = {'User-agent': str(ctr)})
    # soup = bs(page.text, 'html.parser')

    # for link in soup.find_all('a'):
    #     url = str(link.get('href'))
    #     if url.startswith('http'):
    #         if not url.startswith('http://go.m'): 
    #             if not url.startswith('https://go.m'):
    #                 urls.append(url)
    urls = []
    for j in gsearch(query, num=num, stop=num, pause=0.5):
        urls.append(j)
    return urls

def extractText(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    return soup.get_text()

def getSimilarArticleURLS(wordsSentences):
    counters = {}
    for sentence in wordsSentences:
        currentSentence = " ".join(sentence)
        currentUrls = search(currentSentence, 2)
        for url in currentUrls:
            if url not in counters:
                counters[url] = 0
    
    urls = counters.keys()
    return urls
        