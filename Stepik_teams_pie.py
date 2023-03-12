# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:09:31 2023

@author: sheno
"""

a, b = int(input()), int(input())
d = a

while d % a != 0 or d % b != 0:
    d += a 
print(d)

    
    