import pickle
with open("Employee.dat","rb+") as f:

    pickle.load(f)
    
    lst = pickle.load(f)
    try:
        while lst[0] != "":
            if lst[2] >= 20000 and lst[2] <= 40000:
                print(lst)
            lst = pickle.load(f)
    except EOFError:
        print("End of file reached.")

#     Heading = pickle.dump("empno : ename : salary\n",f)
#     data1 = pickle.dump([1, "Rohan", 34000],f)
#     data2 = pickle.dump([2, "Uday", 20000],f)
#     data3 = pickle.dump([3, "Atul", 24000],f)
#     data4 = pickle.dump([4, "Dipesh", 44000],f)


