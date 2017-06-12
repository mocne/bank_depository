# -*- coding: utf-8 -*-
# encoding: utf-8
__author__ = 'pkf'

import unittest
import time
import HTMLTestRunner
import cnaidai_Login
import cnaidai_checkAuthState

class cnaidai_BankDepository(unittest.TestCase):
    def start_to_test(self):
        cnaidai_Login.cnaidaiLogin('wz025', 'a1111111', '1111')
    def check_user_state(self):
        state = cnaidai_checkAuthState.check_auth_state()
        print state
        if state != 'allAuthenticated':
            print '未实名认证'
    def check_depository_state(self):
        browser = cnaidai_Login.browser
        try:
            browser.find_element_by_link_text('立即开通').click()
        except:
            return

if __name__ == '__main__':
    f = open('./Logs/' + str(time.strftime('%Y%m%d')) + '.txt', 'a+')
    suite = unittest.TestSuite()
    suite.addTest(cnaidai_BankDepository('start_to_test'))
    suite.addTest(cnaidai_BankDepository('check_user_state'))
    suite.addTest(cnaidai_BankDepository('check_depository_state'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='银行存管项目', description='测试报告书')
    runner.run(suite)
    f.close()