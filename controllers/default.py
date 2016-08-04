from urllib2 import *
import urllib
def index():
    keyword = str(request.vars.inputkeyword)

    
    f = { 'q' : keyword}

    connection = urlopen('http://localhost:8983/solr/nlpdata/select?'+urllib.urlencode(f)+'&rows=200&wt=json&indent=true')
    response = eval(connection.read())
    matches = response['response']['numFound']
    news = response['response']['docs']
    news = sorted(news, key=lambda k: k ['date'][0], reverse= True)
    newsList = []
    dates = []
    for n in news: # news = []
        new = {}
        d = n['date'][0]
        new['date'] = d
        new['desc'] = n['desc'][0]
        new['title'] = n['title'][0]
        dates.append(d)
        newsList.append(new)
    dates = list(set(dates)) # coklu degerleri uniqe yapar
    return dict(match = matches, name=news, con =keyword, dates = dates,newsList = newsList)

def desc():
    return dict(msg={})
