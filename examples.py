# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 23:33:16 2021

@author: Saurabh Dixit
"""

import poly_derivative as pd
import Taylor_sum as ts
# Coefficients of the polynomial are stored in decreasing order of terms.

cffarray=[1,0,2,0,9]

#Print the polynomial expression
pd.poly_disp(cffarray)

# Evaluate the polynomial value at x=7
value=pd.poly_derivative(cffarray,0,1.5)
print(value)

#Evaluate first derivative at x=2
value=pd.poly_derivative(cffarray,1,2)
print(value)

#Evaluate third derivative at x=3
value=pd.poly_derivative(cffarray,3,3)
print(value)


#Evaluate sixth derivative at x=1
value=pd.poly_derivative(cffarray,6,1)
print(value)

#Evaluate the first term in the Taylor's Series at x=5 with delta_x=0.1
value=ts.Taylor_terms(cffarray,5,0.1,1)
print(value)

#Evaluate the second term in the Taylor's Series at x=5 with delta_x=0.1
value=ts.Taylor_terms(cffarray,5,0.1,2)
print(value)

#Evaluate Taylor polynomial with 3 terms at x=2 and delta_x=0.1
value=ts.Taylor_sum(cffarray,2,0.1,3)
print(value)