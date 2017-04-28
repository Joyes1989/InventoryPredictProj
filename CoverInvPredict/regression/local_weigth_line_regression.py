#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/27 14:24
# @Author  : joyesjiang
# @Site    : 
# @File    : local_weigth_line_regression.py
# @Software: PyCharm Community Edition

from common_udf import *


#  Locally Weighted Linear Regression
def lwlr(testPoint, xArr, yArr, k=1.0):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    N = shape(xMat)[0]
    weights = mat(eye(N))
    for ii in range(N):
        diffMat = testPoint - xMat[ii, :]
        weights[ii, ii] = exp(diffMat * diffMat.T / (-2.0 * k ** 2))
    xTx = xMat.T * (weights*xMat)
    lambda_w = mat(eye(shape(xTx)[0]))
    lambda_w[0, 0] = 0
    print "lambda_w:", lambda_w
    if linalg.det(xTx + lambda_w) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    print "cur_k:", k
    ws = (xTx + lambda_w).I * (xMat.T* (weights * yMat))
    return testPoint * ws


def do_lwlr(f_name, k=1.0):
    print "cur_file_name: %s" % f_name
    x_arr, y_arr = load_file_data(f_name)
    x_mat = mat(x_arr)
    y_mat = mat(y_arr).T
    print "x_mat: %s, y_mat: %s" % (x_mat, y_mat)
    test_mat = copy.copy(x_mat)

    N = shape(test_mat)[0]
    y_pre = zeros(N)
    for idx in range(N):
        print 'test: ', test_mat[idx], x_arr, y_arr, k
        y_pre[idx] = lwlr(test_mat[idx], x_arr, y_arr, k)

    error = rss_error(y_arr, y_pre)
    print "error:", error
    dis_plot(x_mat, y_mat, y_pre)


if __name__ == "__main__":
    f_name = "0dfpyvfa7tp0ewe_28"
    do_lwlr(f_name, 2)
