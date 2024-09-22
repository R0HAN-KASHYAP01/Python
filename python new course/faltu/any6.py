s = "LOST"
L = [10,21,33,4]
D = {}
for i in range(len(s)):
    if i%2 ==0:
        D[L.pop()] = s[i]
    else:
        D[L.pop()] = i+3
        
for K,V in D.items():
    print(K,V,sep="*")