# -*- coding: utf-8 -*-
# encoding: utf-8
__author__ = 'pkf'

import unittest
import time
import cnaidai_Login

class cnaidai_BankDepository(unittest.TestCase):
    def start_to_login(self):
        cnaidai_Login.cnaidaiLogin('wz020', 'a1111111', '1111')

if __name__ == '__main__':
    f = open('./Logs/' + str(time.strftime('%Y%m%d')) + '.txt', 'a+')
    suite = unittest.TestSuite()
    suite.addTest(cnaidai_BankDepository('start_to_login'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    f.close()