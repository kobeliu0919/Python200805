# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:30:43 2020

@author: USER
"""

while True:
    print('-------------')
    print('1.加法')
    print('2.減法')
    print('3.乘法')
    print('4.除法')
    print('5.離開')
    a=int(input('你選擇是?:'))
    if a == 1:
        x=int(input('數字 1:'))
        y=int(input('數字 2:'))
        print(x+y)
    elif a == 2:
        x=int(input('數字 1:'))
        y=int(input('數字 2:'))
        print(x-y)
    elif a == 3:
        x=int(input('數字 1:'))
        y=int(input('數字 2:'))
        print(x*y)
    elif a == 4:
        x=int(input('數字 1:'))
        y=int(input('數字 2:'))
        print(x/y)
    else:
        break