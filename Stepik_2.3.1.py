number = [2, 5, 13, 7, 6, 4]
size = 6
sum = 0 
avg = 0
i = 0
while i < size:
    sum = sum + number[i]
    i = i + 1
    avg = sum / size
print(avg)