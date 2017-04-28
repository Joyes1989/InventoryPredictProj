#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/26 13:42
# @Author  : joyesjiang
# @Site    : 
# @File    : lwlr_algo.py
# @Software: PyCharm Community Edition

from numpy import *
import matplotlib.pyplot as plt


def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for ii in range(numFeat):
            lineArr.append(float(curLine[ii]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


### Standard Regression ###
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


def testing(xArr, yArr, ws):
    xMat = mat(xArr)
    yMat = mat(yArr)
    yHat = xMat * ws
    corr = corrcoef(yHat.T, yMat)
    print "corrcoef:", corr

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xMat[:, 0].flatten().A[0], yMat.T[:, 0].flatten().A[0], color='red')
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy * ws
    ax.plot(xCopy[:, 0], yHat)
    print "xCopy[:, 1]:", xCopy[:, 0]
    print "yHat:", yHat
    print "ws:", ws
    plt.show()

    return corr


### Locally Weighted Linear Regression ###
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
    return testPoint * ws, ws


def rssError(yArr, yHatArr):
    return ((yArr-yHatArr)**2).sum()


def lwlrTest(testArr, xArr, yArr, k=1.0):
    N = shape(testArr)[0]
    yHat = zeros(N)
    for ii in range(N):
        print 'test: ', testArr[ii], xArr, yArr, k
        yHat[ii], ws = lwlr(testArr[ii], xArr, yArr, k)
    return yHat, ws


def lwlr_testing(xArr, yArr, ws, k=1.0):
    xMat = mat(xArr)
    yMat = mat(yArr)
    yHat = zeros(shape(yArr))
    xCopy = mat(xArr)
    xCopy.sort(0)

    for i in range(shape(xArr)[0]):
        yHat[i], ws = lwlr(xCopy[i], xArr, yArr, k)

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
    f_name = 'test_data.txt'
    x_arr, y_arr = loadDataSet(f_name)
    print "x_arr: %s, y_arr: %s" % (x_arr, y_arr)
    # w_s = stdRegres(x_arr, y_arr)
    # testing(x_arr, y_arr, w_s)

    # y_predict, ws = lwlrTest(x_arr, x_arr, y_arr)
    # error = rssError(y_arr, y_predict)
    # print "error:", error
    # lwlr_testing(x_arr, y_arr, ws)
    #
    # y_predict, ws = lwlrTest(x_arr, x_arr, y_arr, 0.1)
    # error = rssError(y_arr, y_predict)
    # print "error:", error
    # lwlr_testing(x_arr, y_arr, ws)

    # y_predict, ws = lwlrTest(x_arr, x_arr, y_arr, 0.01)
    # error = rssError(y_arr, y_predict)
    # print "error:", error
    # lwlr_testing(x_arr, y_arr, ws)

    y_predict, ws = lwlrTest(x_arr, x_arr, y_arr, 10000000000)
    error = rssError(y_arr, y_predict)
    print "error:", error
    lwlr_testing(x_arr, y_arr, ws)
