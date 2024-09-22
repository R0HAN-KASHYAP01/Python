'''
Result ==>   
   *
  **
 ***
****

'''


# num = int(input("Enter the number of lines you Wanted: "))
# for i in range(1,num+1):
#     print(" "*(num-i)+"*"*(i))
        
        

num = int(input("Enter the number of lines you Wanted: "))
for i in range(0,num):
    for j in range(0,num):
        if i+j >= (num-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
'''   
   *
  **
 ***
****
'''