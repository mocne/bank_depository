# -*- coding: utf-8 -*-
# encoding: utf-8
__author__ = 'pkf'

import cnaidai_Login

def check_auth_state():
    browser = cnaidai_Login.browser
    try:
        browser.find_element_by_class_name('u-phone own f-hide')
    except:
        print 'phone in not auth'
        return