#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/26 15:56
# @Author  : joyesjiang
# @Site    : 
# @File    : line_regression.py
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
        print curLine, len(curLine)
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

if __name__ == "__main__":
    f_name = 'test_data_square.txt'
    x_arr, y_arr = loadDataSet(f_name)
    print "x_arr: %s, y_arr: %s" % (x_arr, y_arr)
    w_s = stdRegres(x_arr, y_arr)
    testing(x_arr, y_arr, w_s)