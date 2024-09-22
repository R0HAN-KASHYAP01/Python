import random
fraud_list = []
Checking_list = []
def fraud_table(num):
    for i in range(1, 11):
        if i == 4:
            a = random.randrange((num*i-1), (num*i+1))
            fraud_list.append(a+5)
        else:
            a = num * i
            fraud_list.append(a)
            
def Checking_table(num):
    for i in range(1, 11):
        a = num*i
        Checking_list.append(a)

def Correct_table(lst):
    for i in range(len(lst)):
        if lst[i][0] == lst[i][1]:
            pass
        elif lst[i][0] != lst[i][1]:
            print(f"The table is wrong at {i+1}")
            print(f"The wrong number is {lst[i][0]}")
            print(f"The correct number is {lst[i][1]}")

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    fraud_table(n)
    Checking_table(n)
    correct_list = [answer for answer in zip(fraud_list, Checking_list)]
    # print(correct_list)
    print(f"Fraud's table:- {fraud_list}\n")
    print(f"Trusted's table:- {Checking_list}\n")
    Correct_table(correct_list)
    print(f"\nThe correct table is:-\n{Checking_list}")
