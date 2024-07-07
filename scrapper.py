from urllib.request import urlopen

class Scrapper:
    def get_html(url):
        # result html
        urlResponse = urlopen(url)
        html = urlResponse.read().decode("utf-8")
        return html