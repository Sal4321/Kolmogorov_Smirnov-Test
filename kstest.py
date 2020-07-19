# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:49:35 2020

@author: Salehin
"""

from scipy import stats
import random
import math
from sympy import init_printing

init_printing()
n=1000
ecdf=[]
j=0
x0=1510
j=0
pas1=0
Stats1=[]
Stats2=[]
l=[]
l1=[]
for i in range(n):
    l1.append(random.uniform(0,1))
    x1=(7**5*x0)%(2**31-1)
    l.append(x1/(2**31-1))
    x0=x1    
a=stats.kstest(l,'uniform')

print(a)
print(l)


   
  