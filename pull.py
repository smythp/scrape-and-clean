import lxml.html
import requests
from readability.readability import Document
from bs4 import BeautifulSoup, SoupStrainer

url = "http://www.wuxiaworld.com/issth-index/issth-book-1-chapter-11/"

def get_html(url):
    r = requests.get(url)
    html = r.text
    return html

def write_readable_text_from_url(url,out_file):
    readable_article = Document(get_html(url)).summary()
    readable_article = readable_article.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c","\"").replace(u"\u201d", "\"")
    out_file.write("<!DOCTYPE html>\n<html><head><meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\" /></head>")
    out_file.write(readable_article[6:])


def get_all_links_from_html(html):    
    dom =  lxml.html.fromstring(html)

    for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
        print(link)
            
# print(get_all_links_from_html(get_html(url)))
