def FindOut(Names,HisName):
    for i in range(len(Names)):
        if Names[i] == HisName:
            print(f"{HisName} at {i}")

Names = ["Rohan", "Atul", "Uday", "Dipesh"]
FindOut(Names,"Atul") 
