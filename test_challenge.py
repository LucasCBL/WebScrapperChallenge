import unittest 

# ---- parameters -----
# url of the website we are scrapping
url = 'https://news.ycombinator.com/'

from crawler import WebCrawler

class TestChallengeFunctions(unittest.TestCase):  

    # We test that the srapper returns a text containing a html end tag
    def test_get_html(self):
        html = WebCrawler.get_html(url)
        self.assertRegex(html, r'<\/html>')