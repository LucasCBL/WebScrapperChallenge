from urllib.request import urlopen

class WebCrawler:
    # returns the html of the provided url in a string
    def get_html(url):
        urlResponse = urlopen(url)
        html = urlResponse.read().decode("utf-8")
        return html