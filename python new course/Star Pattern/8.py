'''
Result ==>   
****
 ***
  **
   *

'''
num = int(input("Enter the number of lines you Wanted: "))
for i in range(0,num):
    for j in range(0,num):
        if j>=i:
            print("*",end="")
        else:
            print(" ",end="")
    print()