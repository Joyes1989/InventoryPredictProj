#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/27 16:52
# @Author  : joyesjiang
# @Site    : 
# @File    : ride_regression.py
# @Software: PyCharm Community Edition

from common_udf import *


### Ridge Regression ###
def ridgeRegres(xMat, yMat, lam=0.2):
    xTx = xMat.T * xMat
    # denom = xTx + lam * eye(shape(xMat)[1])
    denom = xTx + eye(shape(xMat)[1])
    print "denom:", denom
    if linalg.det(denom) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = denom.I * (xMat.T * yMat)
    return ws


def ridgeTest(xArr, yArr):
    xMat = mat(xArr)
    xMeans = mean(xMat, 0)
    xVar = var(xMat, 0)
    xMat = (xMat - xMeans) / xVar
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    yMat = yMat - yMean
    numTestPts = 30
    wMat = zeros((numTestPts, shape(xMat)[1]))

    print "xMat:", xMat
    for ii in range(numTestPts):
        ws = ridgeRegres(xMat, yMat, exp(ii - 10))
        wMat[ii, :] = ws.T
    return wMat


def ridgeTest2(xArr, yArr, test_point=5):
    xMat = mat(xArr)
    print "xMat:", xMat
    xMeans = mean(xMat, 0)
    xVar = var(xMat, 0)
    xMat = (xMat - xMeans) / xVar
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    yMat = yMat - yMean
    print "xMeans:", xMeans
    print "xVar:", xVar
    print "xMat:", xMat
    ws = ridgeRegres(xMat, yMat, exp(test_point - 10))
    return ws


def ride_plot_ws_mat(xArr, yArr, test_point=10):
    xMat = mat(xArr)
    yMat = mat(yArr)
    yHat = zeros(shape(yArr))
    xCopy = mat(xArr)
    xCopy.sort(0)

    wMat = ridgeTest(xArr, yArr, test_point)
    ws_num = shape(wMat[0])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten().A[0])
    ax.plot(xMat[:, 1].flatten().A[0], yHat)
    print "yHat:", yHat
    print "ws:", ws
    plt.show()

    return corr


def ride_plot(xArr, yArr, test_point=10):
    xMat = mat(xArr)
    yMat = mat(yArr)
    yHat = zeros(shape(yArr))
    xCopy = mat(xArr)
    xCopy.sort(0)

    ws = ridgeTest2(xArr, yArr, test_point)
    yHat = xCopy * ws

    corr = corrcoef(yHat.T, yMat)
    print "corrcoef:", corr

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten().A[0], color='red')
    ax.plot(xMat[:, 1].flatten().A[0], yHat)
    print "yHat:", yHat
    print "ws:", ws
    plt.show()

    return corr

if __name__ == "__main__":
    f_name = '0dfpyvfa7tp0ewe_28'
    x_arr, y_arr = load_file_data(f_name)
    print "x_arr: %s, y_arr: %s" % (x_arr, y_arr)

    # error = rssError(y_arr, y_predict)
    # print "error:", error
    print "lambda-5:"
    ride_plot(x_arr, y_arr, 5)

    print "lambda-15:"
    ride_plot(x_arr, y_arr, 15)