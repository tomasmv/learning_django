from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.PhantomJS()
# browser.implicitly_wait(3)
# browser.get('http://www.bloomberg.com/topics/travel')
#
# html_source = browser.page_source
#
# soup = BeautifulSoup(html_source, 'lxml')
#
# articles = soup.findAll('li', {'class': 'index-page__item  type-article site-bbiz'})
#
# for article in articles:
#     print article.find('a')['href']
