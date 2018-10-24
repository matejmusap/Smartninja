from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from random import shuffle

quote_url = 'http://quotes.yourdictionary.com/theme/marriage/'
quote_html = urlopen(quote_url).read()
qoute_soup = BeautifulSoup(quote_html)
qoutes = qoute_soup.findAll("p", attrs={"class": "quoteContent"})
list_of_quotes = []
for quote in qoutes:
    list_of_quotes.append(quote.text)
shuffle(list_of_quotes)
gift = list_of_quotes[:5]
for x in gift:
    print x