L1 = input().split()
L = [int(i) for i in L1]
L.sort()

count = 1 

for i in range(1,len(L)):
    if L[i] == L[i - 1]:
        count += 1
        if i == len(L) - 1:
            print(L[i])
    else:
        if count > 1:
            print(L[i - 1], end = ' ')
        else:
            continue
        count = 1

        
    
        
        
            
        

        

            
            
            

    