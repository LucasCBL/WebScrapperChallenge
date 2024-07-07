import unittest 

# ---- Initial parameters -----
# url of the website we are scrapping
url = 'https://news.ycombinator.com/'

from scrapper import Scrapper

class TestChallengeFunctions(unittest.TestCase):  

    # We test that the srapper returns a 
    def test_get_html(self):
        html = Scrapper.get_html(url)
        self.assertRegex(html, r'<\/html>')