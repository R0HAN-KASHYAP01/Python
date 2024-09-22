'''
Result ==>   
**********
 ******** 
  ******  
   ****   
    **    
    *     
'''


num = int(input("Enter the number of lines you Wanted: "))
for i in range(0,num+1):
    for j in range(0,(2*num)):
        if j >= i and j <= ((2*num)-1-i) or j == num-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
