#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/27 13:30
# @Author  : joyesjiang
# @Site    : 
# @File    : common_udf.py
# @Software: PyCharm Community Edition

from numpy import *
import matplotlib.pyplot as plt
import copy


# 加载样本文件
def load_file_data(file_name):
    print "cur_file_name:", file_name
    num_feature = len(open(file_name).readline().split('\t')) - 1
    data_mat = []
    label_mat = []
    fr = open(file_name)
    for line in fr.readlines():
        # 这里为每个样本设置一个偏置项1
        line_arr = [1.0]

        cur_line = line.strip().split('\t')
        for idx in range(num_feature):
            line_arr.append(float(cur_line[idx]))
        data_mat.append(line_arr)
        label_mat.append(float(cur_line[-1]))

    return data_mat, label_mat


# 计算回归的均方误差
def rss_error(y_arr, y_hat_arr):
    return ((y_arr - y_hat_arr)**2).sum()


# 根据回归得到的参数ws,画出回归曲线
def ride_plot(x_arr, y_arr, ws):
    x_mat = mat(x_arr)
    y_mat = mat(y_arr)
    x_copy = copy.copy(x_mat)

    y_hat = x_copy * ws

    corr = corrcoef(y_hat.T, y_mat)
    print "corrcoef:", corr
    print "ws:", ws
    dis_plot(x_mat, y_mat, y_hat)


def dis_plot(x_mat, y_mat, y_pre):
    print "x_mat: %s, y_mat: %s" % (x_mat, y_mat)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    print "x_mat[:, 1]:", x_mat[:, 1]
    print "y_mat.T[:, 0]: ", y_mat.T[:, 0]
    ax.scatter(x_mat[:, 1].flatten().A[0], y_mat[:, 0].flatten().A[0], color='red')
    ax.plot(x_mat[:, 1].flatten().A[0], y_pre)
    print "y_hat:", y_pre
    plt.show()