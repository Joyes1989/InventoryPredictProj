#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/26 15:56
# @Author  : joyesjiang
# @Site    : 
# @File    : main.py
# @Software: PyCharm Community Edition


from line_regression import *
from lwlr_algo import *


if __name__ == "__main__":
    f_name = 'test_data_square.txt'
    x_arr, y_arr = loadDataSet(f_name)
    print "x_arr: %s, y_arr: %s" % (x_arr, y_arr)
    w_s = stdRegres(x_arr, y_arr)
    testing(x_arr, y_arr, w_s)
