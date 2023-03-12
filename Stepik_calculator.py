# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 07:18:37 2023

@author: sheno
"""
shape = input()
a, b, c, r = int.(input()), int.(input()), int.(input()), int.(input())
pi = 3.14
p = (a + b + c)/2

if shape == 'треугольник':
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif shape == 'прямоугольник':
    print(a * b)
elif shape == 'круг':
    print(p * (r ** 2) / 2)
    
    

