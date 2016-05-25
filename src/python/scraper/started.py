from bs4 import BeautifulSoup
import urllib
import pandas as pd
r = urllib.urlopen('http://www.realclearpolitics.com/epolls/2016/president/oh/ohio_trump_vs_clinton-5634.html').read()
soup = BeautifulSoup(r)

datatable = soup.find("div", {"id": "polling-data-full"})


df = pd.read_html(str(datatable), flavor="bs4", attrs = {'class': 'data large '})

print df[0].head()

