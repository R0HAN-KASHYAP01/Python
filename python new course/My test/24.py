sub1 = int(input("Enter your marks of Physics: "))
sub2 = int(input("Enter your marks of Chemistry: "))
sub3 = int(input("Enter your marks of Mathematics: "))

if(sub1>33 or sub2>33 or sub3>33):
    print("Congratulation! you are passed in exam")

elif(((sub1 + sub2 + sub3)/300)*100) > 40:
    print("Congratulation! you are passed in exam") 

else:
    print("You are failed in exam")

