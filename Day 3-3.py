# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:38:22 2020

@author: USER
"""


def As(n):
    ts=0
    for item in score:
        ts=ts+item
    return ts/a 

def Highest_score(w):
    hs=0
    for t in score:
       if t > hs:
           hs=t
       else:
               hs=hs
    return(hs)   
     
def Lowest_score(v):
    ls=100
    for t in score:
        if t < ls:
            ls=t
        else:
            ls=ls
    return(ls)   
     
name=[]
score=[]
a=int(input("How many people in the class"))    
for i in range(a):
      score.append(int(input("How does he score")))
      
print(As(score))
print(Highest_score(score))
print(Lowest_score(score))