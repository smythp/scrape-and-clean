import lxml.html
from lxml import etree
import requests
from readability.readability import Document
from bs4 import BeautifulSoup, SoupStrainer

url = "http://www.wuxiaworld.com/issth-index/issth-book-1-chapter-1/"

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

def parse_html(html):
    root = lxml.html.fromstring(html)
    return root

def find_link_matching_string(html,string):
    root = parse_html(html)
    e = root.xpath('.//a[contains(text(),"Next")]')
    return e

    
html = get_html(url)
out = find_link_matching_string(html,"fly")
print(out)
for element in out:
    print(element.get('href'))


    
        


# try using this to match 
# .//a[text()='Example']
# or this tree.xpath(".//a[text()='Example']")[0].tag
# from here 

