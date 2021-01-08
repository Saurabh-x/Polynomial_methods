# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:18:46 2020

@author: Saurabh Dixit
"""

from math import factorial
import poly_derivative as pd

def Taylor_sum(xcoeff,t,delta_t,upto_terms):
    sum=0
    for i in range(0,upto_terms):
        sum=sum+pd.poly_derivative(xcoeff,i,t)*(delta_t**(i))/factorial(i)
    return(sum)


def Taylor_terms(xcoeff,t,delta_t,term_no):
    i=term_no-1
    value=pd.poly_derivative(xcoeff,i,t)*(delta_t**(i))/factorial(i)
    return(value)