# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 07:18:37 2023

@author: sheno
"""
shape = input()
pi = 3.14

if shape == 'треугольник':
    a, b, c = int(input()), int(input()), int(input())
    p = (a + b + c)/2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif shape == 'прямоугольник':
    a, b = int(input()), int(input())
    print(a * b)
elif shape == 'круг':
    r = int(input())
    print(pi * (r ** 2))
    
    

