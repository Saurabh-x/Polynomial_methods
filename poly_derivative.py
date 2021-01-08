# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:15:41 2020

@author: Saurabh Dixit
"""

from math import factorial


#Use poly_derivative to evaluate polynomial value by putting derivative_order as 0.
def poly_derivative(cffarray,derivative_order,x):
    n=len(cffarray)-1 #the polynomial order
    p=derivative_order
    drtv=0
    if(p>n):
        return 0
    else:
        for i in range(0,(n-p)+1):
            drtv=drtv+factorial(n-i)/factorial(n-p-i)*cffarray[i]*(x**(n-p-i))
        return(drtv)
    
#This function prints the polynomial given its coefficients.
def poly_disp(cffarray):
    l=len(cffarray)
    for i in range(l-1,1,-1):
        if(cffarray[i]!=0):
            print(cffarray[l-i-1],'x^',i,'+',end='',sep='')
    print(cffarray[l-1])
    