import lxml.html
from lxml import etree
import requests
from readability.readability import Document
from bs4 import BeautifulSoup, SoupStrainer

url = ""

def get_html(url):
    r = requests.get(url)
    html = r.text
    return html

def write_readable_text_from_url(url,out_file):
    readable_article = Document(get_html(url)).summary()
    readable_article = readable_article.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c","\"").replace(u"\u201d", "\"")
    out_file.write("<!DOCTYPE html>\n<html><head><meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\" /></head>")
    out_file.write(readable_article[6:])

def get_cleaned_html_from_url(url):
    readable_article = Document(get_html(url)).summary()
    readable_article = readable_article.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c","\"").replace(u"\u201d", "\"")
    string_out = "<!DOCTYPE html>\n<html><head><meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\" /></head>"
    string_out += readable_article[6:]
    return string_out
    
def get_all_links_from_html(html):    
    dom =  lxml.html.fromstring(html)

    for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
        print(link)

def parse_html(html):
    root = lxml.html.fromstring(html)
    return root

def find_link_matching_string(html,string):
    root = parse_html(html)
    e = root.xpath('.//a[contains(text(),"%s")]' % string)
    e = e[0].get('href')
    return e

def follow_links_and_write_text(start_url,next_item_match_string,filename):
    with open(filename,"w") as file:
        html = get_cleaned_html_from_url(start_url)
        file.write(html)
        file.write('\n\n')
        while 1:
            out = find_link_matching_string(html,next_item_match_string)
            print('Following link: ' + out)
            html = get_cleaned_html_from_url(out)
            file.write(html)
            file.write('\n\n')        


follow_links_and_write_text(url,"Next","supertest.html")
