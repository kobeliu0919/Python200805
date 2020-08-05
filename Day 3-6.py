# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:15:34 2020

@author: USER
"""

d={}

print('歡迎來到中英辭典')
while True:
    print("----------")
    print('1.建立詞彙')
    print('2.列出所有單字')
    print('3.中翻英')
    print('4.英翻中')
    print('5.測驗學習結果')
    print('6.離開')
    a=int(input('請輸入選項:'))
    if a == 1:
        while True:
            sw1=input('請輸入單字(0跳出):')
            sw2=input('請輸入翻譯:')
            if  sw1 == '0':
                break
            else:
                d[sw1]=sw2
    elif a == 2:
        for item in d:
            print(item, "是",d[item])
        

    