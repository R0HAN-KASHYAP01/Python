import pickle

def copy():
    with open("Empfile.dat","rb") as f:
        line = pickle.load(f)
        with open("New_emp.dat","ab") as f1:
            try:
                while True:
                    pickle.dump(line,f1)
                    line = pickle.load(f)
                    if line == "":
                        break
            except EOFError:
                print("Data add successfully!")

copy()

# with open("New_emp.dat","rb") as f:
#     line = pickle.load(f)
#     try:
#         while True:
#             print(line)
#             line = pickle.load(f)
#             if line == "":
#                 break
#     except EOFError:
#         pass
