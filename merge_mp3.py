# -*- coding: utf-8 -*-
import urllib.request
from lxml import etree
import re
import time
from functools import reduce
import requests
#from selenium import webdriver

def download_file():
    if browser.find_element_by_link_text("下载"):
        browser.find_element_by_link_text("下载").click()

def click_merge_button(selector):
    if browser.find_element_by_class_name("btn-save"):
        browser.find_element_by_class_name("btn-save").click()
        print("find merge button")
    else:
        print("don't find merge button")


try:
    '''
    browser = webdriver.PhantomJS(executable_path='/user/bin/phantomjs')
    browser.get("https://audio-joiner.com/cn/")
    print(browser.title)
    '''
    url = "https://s114.123apps.com/ajoiner/upload/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    files = {
        'userfile': open(r"/home/gpr/code/python/download_word_pronun/1.mp3", "rb"),
        'userfile': open(r"/home/gpr/code/python/download_word_pronun/2.mp3", "rb"),
    }
    html=requests.post(url=url, headers=headers, files=files)
    print(html.status_code)
    print(html.text)
    print("---click merge button---")
    '''
    click_merge_button()
    download_file()
    '''
    print("--success---")
except:
    print ("--error--")



