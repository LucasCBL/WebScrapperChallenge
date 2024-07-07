from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

class WebCrawler:
    # returns the html of the provided url in a string
    def get_html(url):
        urlResponse = urlopen(url)
        html = urlResponse.read().decode("utf-8")
        return html
    
    # function to extract number from string with format \d\d.*
    def get_number(tag):
        match = re.search(r'\d+', tag.text);
        if (match):
            return int(match.group())
        return 0
    
    # Function to extract score safely
    def get_score(tag):
        next_tr_tag = tag.find_next_sibling()
        if (next_tr_tag):
            score_tag = next_tr_tag.find(class_='score')
            if (score_tag):
               return WebCrawler.get_number(score_tag) 
        return 0
    

    #Function to extract comments safely
    def get_comments(tag):
        next_tr_tag = tag.find_next_sibling()
        if (next_tr_tag):
            span_tag = next_tr_tag.find('span')
            if (span_tag):
                span_children_tags = span_tag.find_all('a')
                if(span_children_tags and len(span_children_tags) == 4):
                    return WebCrawler.get_number(span_children_tags[3])
        return 0

    def get_news(html):
        soup = BeautifulSoup(html, 'html.parser')

        # We need to find and extract all the tags with class 'athing' since it seems to be what the hacker news site uses as news
        raw_news = soup.find_all(class_='athing')

        news = [{
            'title': tag.find(class_='titleline').text,
            'number': tag.find(class_='rank').text,
            'points': WebCrawler.get_score(tag), 
            'comments': WebCrawler.get_comments(tag) } for tag in raw_news]

        return news