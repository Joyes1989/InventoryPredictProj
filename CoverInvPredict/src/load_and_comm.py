#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/27 9:38
# @Author  : joyesjiang
# @Site    : 
# @File    : load_data_set.py
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


def rssError(yArr, yHatArr):
    return ((yArr-yHatArr)**2).sum()




