from bs4 import BeautifulSoup
from urllib.request import urlopen

def cnn_scrapper(link):
    html_response = link
    soup = BeautifulSoup(urlopen(link))
    print("Title: ", soup.find('h1').get_text())
    temp_ls = soup.find_all('span', {"class":'metadata__byline__author'})
    for temp in temp_ls:
        print("Author: ", temp.find('a').get_text())
    temp_time = soup.find('p', {'class':'update-time'})
    print("Time: ", temp_time.get_text())
    def get_full_text(doc):
        soup = BeautifulSoup(urlopen(doc))
        for s in soup(['script', 'style']):
            s.extract()
        return (soup.text.strip()).encode('ascii', 'ignore').decode("utf-8")
    print("Fulltext:", get_full_text(html_response))
    return get_full_text(html_response)
