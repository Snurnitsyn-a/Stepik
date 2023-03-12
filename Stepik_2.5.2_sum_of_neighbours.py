Line = input().split()
L = []
for num in Line:
    L.append(int(num))
L1 = []
L2 = []
L3 = []
if len(L) == 1:
    fin_L = str(L[0])
else:    
    for i in range(len(L)):
        if i == 0:
            L2.append(L[1] + L[-1])
        elif i == len(L) - 1:
            L3.append(L[i - 1] + L[0])
        else:
            L1.append(L[i - 1] + L[i + 1])
    fin_L = " ".join(str(x) for x in L2 + L1 + L3)
print(fin_L)




        
        


