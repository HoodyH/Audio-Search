import os
from selenium import webdriver


class Search:

    def __init__(self):
        path = os.getcwd() + '/src/webdriver/chromedriver.exe'
        self.__browser = webdriver.Chrome(path)

    def google(self, keywords):
        self.__browser.get('http://www.google.com/search?q={}'.format(keywords))
