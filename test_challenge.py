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

    def test_filter_news(self):
        html = WebCrawler.get_html(url)
        news = WebCrawler.get_news(html)
        # we check that the amount of news is the one expected
        self.assertEqual(len(news), 30)
        # we check whether the objects extracted contain the expected keys
        self.assertIn('title', news[0].keys())
        self.assertIn('points', news[0].keys())
        self.assertIn('comments', news[0].keys())
        self.assertIn('number', news[0].keys())
