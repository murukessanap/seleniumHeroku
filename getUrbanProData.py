#!/usr/bin/env python
# export PATH=$PATH:/home/muru/myFlaskPython
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


#import time
#import requests
#from urllib.parse import urlparse
#from urlparse import urlparse

import urllib.parse as urlparse

#from six.moves.urllib.parse import urlparse

#from urlparse import urljoin
from selenium.webdriver.firefox.options import Options


#options = Options()
#options.add_argument("--headless")
#driver = webdriver.Firefox(firefox_options=options, executable_path="/home/muru/myFlaskPython")
#print("Firefox Headless Browser Invoked")

display = Display(visible=0, size=(1024, 768))
display.start()

driver = webdriver.Firefox()
#driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs')
#driver.get('url')
'''timeout = 5
try:
    element_present = EC.presence_of_element_located((By.ID, 'element_id'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print "Timed out waiting for page to load"'''

def get():
    browser = webdriver.Firefox()
    browser.get('http://www.urbanpro.com/login')

    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.ID, 'j_password'))
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
        exit()
    username = browser.find_element_by_id("j_username")
    username.send_keys("murukessanap@gmail.com")
    browser.find_element_by_css_selector('.newBtn.blueBtn.loginNxt.mt-10').click()

    password = browser.find_element_by_id("j_password")
    password.send_keys("apm@indian007")

    browser.find_element_by_css_selector('.newBtn.blueBtn.mt-15.submitBtn.recaptchSubmit').click()
    browser.get('https://www.urbanpro.com/register/providerDashboard')
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    '''while(1):
        time.sleep(5)
        browser.refresh()'''

    # print(browser.page_source)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    # soup = BeautifulSoup(browser.page_source, 'lxml')

    links = []
    # for card in soup.select('.provider-list-card.unread'):
    for card in soup.select('.provider-list-card'):
        l = card.find('a')['href']
        links.append(urlparse.urljoin('https://www.urbanpro.com', l))
        #print(l)

    names = []
    for l in links:
        browser.get(l)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        p = soup.find_all('p')
        for i in range(len(p)):
            if p[i].text == "Class Location":
                loc = p[i + 1].text

        name = soup.select_one('.list-title').text
        if loc.strip('\n') == "Online class":
            names.append([name, soup.select_one('.list-txt').text, soup.select_one('.list-txt.pos-rel').text, loc])

    return ''.join(str(names))
