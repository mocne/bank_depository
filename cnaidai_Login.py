# -*- coding: utf-8 -*-
# encoding: utf-8
__author__ = 'pkf'

from selenium import webdriver
from time import sleep

global browser
browser = webdriver.Chrome()
browser.maximize_window()

def cnaidaiLogin(username, password, valicode):
    browser.get('http://a.cnaidai.com/webjr/login.htm')
    sleep(2)
    browser.find_element_by_name('username').send_keys(username)
    browser.find_element_by_name('password').send_keys(password)
    browser.find_element_by_name('valicode').send_keys(valicode)
    sleep(1)
    browser.find_element_by_class_name('submit').click()

if __name__ == '__main__':
    cnaidaiLogin()