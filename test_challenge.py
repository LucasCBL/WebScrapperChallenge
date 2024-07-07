import unittest 

# ---- parameters -----
# url of the website we are scrapping
url = 'https://news.ycombinator.com/'
html = ''
news = {}
from crawler import WebCrawler

class TestChallengeFunctions(unittest.TestCase):  
    
    # We test that the crawler returns a text containing a html end tag
    def test_get_html(self):
        html = WebCrawler.get_html(url)
        self.assertRegex(html, r'<\/html>') 

    # Test for the correct extraction of news from the hacker news website
    def test_extract_news(self):
        news = WebCrawler.get_news(html)
        # we check that the amount of news is the one expected
        self.assertEqual(len(news), 30)
        # we check whether the objects extracted contain the expected keys
        self.assertIn('title', news[0].keys())
        self.assertIn('points', news[0].keys())
        self.assertIn('comments', news[0].keys())
        self.assertIn('number', news[0].keys())

    # Test for filtering news by title work length
    def test_filer_by_word_count(self):
        long_news = NewsHandler.filter_word_count(count = 5, greater = True )
        short_news = NewsHandler.filter_word_count(count = 5, greater = False )
        self.assertIn(len(short_news) + len(long_news), 30)
    
    # Test for news sorting
    def test_news_sorting(self):
        sorted_news = NewsHandler.sortBy(key = 'comments', ascending = True)
        is_sorted = all(a <= b for a, b in zip(sorted_news.comments, sorted_news[1:].comments))
        self.assertTrue(is_sorted, "correctly sorts by comments in ascending order")

        sorted_news = NewsHandler.sortBy(key = 'points', ascending = False)
        is_sorted = all(a >= b for a, b in zip(sorted_news.comments, sorted_news[1:].comments))
        self.assertTrue(is_sorted, "correctly sorts by oints in descending order")



