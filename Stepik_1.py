# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 07:18:37 2023

@author: sheno
"""
num_1, num_2 = float(input()), float(input())
op = input()

if op == '+':
    print(num_1 + num_2)
elif op == '-':
    print(num_1 - num_2)
elif op == '*':
    print(num_1 * num_2)
elif op == '/':
    if num_2 == 0:
        print('Деление на 0!')
    else:
        print(num_1 / num_2)
elif op == 'mod':
    if num_2 == 0:
        print('Деление на 0!')
    else:
        print(num_1 % num_2)
elif op =='pow':
    print(num_1 ** num_2)
elif op == 'div':
    if num_2 == 0:
        print('Деление на 0!')
    else:
        print(num_1 // num_2)
    
    

