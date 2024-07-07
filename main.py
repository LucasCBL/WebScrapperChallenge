from crawler import WebCrawler
from crawler import NewsHandler
from time import gmtime, strftime


url = 'https://news.ycombinator.com/'
html = WebCrawler.get_html(url)
news = WebCrawler.get_news(html)
option  = 0
sorting_keys = ['comments', 'points', 'number']
logs = []

while(option != 'quit'):
    print('------------ Current news ------------------ \n')
    for article in news:
        print(article)
    print('-------------------------------------------- \n')
    print('------------- OPTIONS -------------\n')
    print(' * filter: to filter by wordcount write filter\n')
    print(' * sort: to sort the news input sort filter\n')
    print(' * export: to export the current set of articles write export\n')
    print(' * update: input update to get a new set of 30 articles\n')
    print(' * quit: enter quit to exit the program\n')

    option = input('  -> ')
    
    if (option == 'filter'):
        count = -1
        while count <= 0:
            print('please input the threshhold word count (must be a digit greater than 0)')
            count = int(input('  -> '))
        greater = -1
        while greater <= 0 or greater > 2:
            print('------- options --------\n')
            print('[1] if you want to keep the titles with word counts greater than ' + str(count) + ' and discard the rest\n')
            print('[2] if you want to keep the titles with lesser or equal word counts than ' + str(count) + ' and discard the rest\n')
            greater = int(input('  -> '))
        news = NewsHandler.filter_word_count(news, count, greater == 1)
        logs.append({'time': strftime("(%Y-%m-%d)%H:%M:%S", gmtime()), 'command': 'filter ' + str(count) + ' ' + str(greater)})

    if (option == 'sort'):
        key = -1
        while key <= 0 or key > 3:
            print('------- Sort by --------\n')
            print('[1] Comments\n')
            print('[2] Points\n')
            print('[3] Number\n')
            key = int(input('  -> '))
        ascendent = -1
        while ascendent <= 0 or ascendent > 2:
            print('------- options --------\n')
            print('[1] ascendent order\n')
            print('[2] reverse order \n')
            ascendent = int(input('  -> '))
        news = NewsHandler.sort_by(news, sorting_keys[key - 1], ascendent == 1)
        
        logs.append({'time': strftime("(%Y-%m-%d)%H:%M:%S", gmtime()), 'command': 'sort ' + sorting_keys[key - 1] + ' ' + str(ascendent)})
    
    if (option == 'update'):
        html = WebCrawler.get_html(url)
        news = WebCrawler.get_news(html)
        logs.append({'time': strftime("(%Y-%m-%d)%H:%M:%S", gmtime()), 'command': 'update'})
    
    if (option == 'export'):
        print('choose the name of the csv file, this will replace an existing csv if there is already one with this name, the file will be created at the location of this executable\n')
        name = input('  -> ')
        NewsHandler.export_csv(news, name)
        logs.append({'time': strftime("(%Y-%m-%d)%H:%M:%S", gmtime()), 'command': 'export ' + name})

print('Logs for this session were stored at: ')
NewsHandler.export_csv(logs, strftime("log%Y-%m-%d-%H-%M-%S", gmtime()))
