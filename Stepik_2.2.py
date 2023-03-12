# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 15:28:01 2023

@author: sheno
"""

i = int(input())

while i <= 100:
    i = int(input())
    if i < 10:
        continue
    if i > 100:
        break
    print(i)
