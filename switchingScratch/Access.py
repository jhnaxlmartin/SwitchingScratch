from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import activeAliasTracker
import pyautogui
import getpass
import json
from switchingScratch import template

active_indexname = activeAliasTracker.currentIndex
switchto_indexname = 'accenturedotcom20201029a' #targetindex
#active_indexpath = '//*[@id="{}"]'.format(active_indexname)
#switchto_indexpath = '//*[@id="{}"]'.format(switchto_indexname)

class Access():
    def __init__(self):
        try:
            eid = input('Accenture EID: ')
            password = getpass.getpass()
        except Exception as error:
            print('Access Error.', error)
        else:
            self.login = {'eid': eid, 'password': password}

        opts = Options()
        opts.add_argument("--start-maximized")
        self.browser = webdriver.Chrome(options=opts)
        self.browser.get("https://searchcleanindex2.accenture.com/amz/enrichment/aliasSwitcher.html")
        sleep(2)
        pyautogui.typewrite("dir\\" + self.login["eid"])
        pyautogui.press("tab")
        pyautogui.typewrite(self.login["password"])
        pyautogui.press("enter")
        assert 'Search Enrichment : Alias Switcher' in self.browser.title


    def switching_alias(self):
        sleep(10)
        browser = self.browser
        browser.find_element_by_id('filterResults').send_keys(active_indexname)
        sleep(5)
        browser.find_element_by_id(active_indexname).click()
        sleep(5)
        browser.find_element_by_id(switchto_indexname).click()
        sleep(5)
        browser.find_element_by_id('switchButton').click()
        sleep(5)
        browser.find_element_by_id('switchConfirmed').click()
        sleep(5)

        exit()



