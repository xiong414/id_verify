# -*- coding:utf-8 -*-
# @Auther: XiongGuoqing
# @Datetime: 2019/12/18 7:04 下午
# @Contact: xiong3219@icloud.com

import numpy as np


def getCheckCode(id):
    sum = 0
    for i, n in zip(range(1, 18), id):
        w = np.mod(np.power(2, 18 - i), 11)
        sum += int(n) * w
    checkcode = str(np.mod(12 - np.mod(sum, 11), 11))
    if checkcode == '10':
        checkcode = 'X'
    return checkcode


if __name__ == '__main__':
    id =  '22020220200202002'
    id += getCheckCode(id)
    id2 = '22020220200202222'
    id2 += getCheckCode(id2)
    print(id)
    print(id2)

