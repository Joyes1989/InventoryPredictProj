#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/27 14:05
# @Author  : joyesjiang
# @Site    :
# @File    : line_regression.py
# @Software: PyCharm Community Edition

from common_udf import *


#  Standard Regression
def stdRegres(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    print "xMat: %s, yMat: %s, xMat.T: %s, multi: %s" % (xMat, yMat, xMat.T, xMat.T * xMat)
    xTx = xMat.T * xMat
    print "xTx: ", xTx
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws


def do_std_regress(f_name):
    print "train_data_file_name: %s" % f_name
    x_arr, y_arr = load_file_data(f_name)
    print "x_arr: %s, y_arr: %s" % (x_arr, y_arr)
    ws = stdRegres(x_arr, y_arr)
    ride_plot(x_arr, y_arr, ws)

if __name__ == "__main__":
    print "Do line_regression test:"
    do_std_regress("0dfpyvfa7tp0ewe_28")
