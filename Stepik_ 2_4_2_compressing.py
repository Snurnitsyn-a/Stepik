a = input()
new_a = []
count = 1
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        count += 1
    else:
        new_a.append(a[i] + str(count))
        count = 1
new_a.append(a[-1] + str(count))
result = "".join(new_a)
print(result)




