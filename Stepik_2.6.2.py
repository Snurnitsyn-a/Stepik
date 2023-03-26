'''
Напишите программу, которая выводит часть последовательности 
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). 
На вход программе передаётся неотрицательное целое число n — столько элементов 
последовательности должна отобразить программа. На выходе ожидается 
последовательность чисел, записанных через пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
'''
'''
n = int(input())
i = 0
s = []

while len(s) < n:
    i += 1
    for x in range(i):
        s.append(i)
        if len(s) == n:
            break
result = ' '.join(str(x) for x in s)
print(result)
'''

n = int(input())
s = []
i = 1
while len(s) < n:
    s += [i] * min(n - len(s), i)
    i += 1
result = ' '.join(str(x) for x in s)
print(result)

'new comment'