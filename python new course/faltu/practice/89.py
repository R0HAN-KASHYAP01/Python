dic = {1: {"name":"Rohan"},
       2: {"name":"Uday"},
       3 : {"name":"Atul"},
       4: {"name":"Dipesh"},
       3:"aditya"}

a = sorted(dic.items())
print(a)
b = dict(sorted(dic.items()))
print(b)
print(dic)
