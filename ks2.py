# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 18:55:42 2020

@author: Salehin
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:10:02 2020

@author: Salehin
"""
import random
import math
import matplotlib.pyplot as plt
n=1000
ecdf=[]
pas=0

fail=0
j=0
Initials=[]
Statistics=[]
failindex=[]

l=[]
x0=random.randint(1,10000)
print(x0)
Initials.append(x0)
for i in range(n):
    x1=(7**5*x0)%(2**31-1)
    l.append(x1/(2**31-1))
    x0=x1
#    plt.hist(l,edgecolor='black',linewidth=0.2)    
for i in range(n):
    ecdf.append((i+1)/n)
    
#    s=sum(l)/n
#    for i in range(n):
#        l1.append(l[i]**2)
#    v=(sum(l1)/n)-(s**2)
#    variance.append(v)    
#    means.append(s)
l.sort()
plt.plot(l,ecdf) 
plt.plot(ecdf,ecdf)
max3=0
for i in range(n):
   x=i/n
   y=(i+1)/n
   g=abs(x-l[i])
   h=abs(y-l[i])
   maxx=max(g,h)
   if(maxx>max3):
       max3=maxx       
Statistics.append(max3)


if(max3<1.6276/math.sqrt(n)):
   pas+=1 
else:
    fail+=1
    failindex.append(j)   
  
    

   