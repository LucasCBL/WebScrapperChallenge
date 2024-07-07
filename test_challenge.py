import unittest 

# ---- parameters -----
# url of the website we are scrapping
url = 'https://news.ycombinator.com/'
from crawler import NewsHandler, WebCrawler

class TestChallengeFunctions(unittest.TestCase):  
    
    # We test that the crawler returns a text containing a html end tag
    def test_get_html(self):
        html = WebCrawler.get_html(url)
        self.assertRegex(html, r'<\/html>') 

    # Test for the correct extraction of news from the hacker news website
    def test_extract_news(self):
        html = WebCrawler.get_html(url)
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
        html = WebCrawler.get_html(url)
        unfiltered_news = WebCrawler.get_news(html)
        long_news = NewsHandler.filter_word_count(news = unfiltered_news, count = 5, greater = True )
        short_news = NewsHandler.filter_word_count(news = unfiltered_news, count = 5, greater = False )
        self.assertEqual(len(short_news) + len(long_news), 30)
    
    # Test for news sorting
    def test_news_sorting(self):
        html = WebCrawler.get_html(url)
        unsorted_news = WebCrawler.get_news(html)
        sorted_news = NewsHandler.sort_by(news = unsorted_news, value = 'comments', ascending = True)
        sorted_comments = [article['comments'] for article in sorted_news]
        is_sorted = all(a <= b for a, b in zip(sorted_comments, sorted_comments[1:]))
        self.assertTrue(is_sorted, "correctly sorts by comments in ascending order")

        sorted_news = NewsHandler.sort_by(news = unsorted_news,  value = 'points', ascending = False)
        sorted_points = [article['points'] for article in sorted_news]
        is_sorted = all(a >= b for a, b in zip(sorted_points, sorted_points[1:]))
        self.assertTrue(is_sorted, "correctly sorts by oints in descending order")



