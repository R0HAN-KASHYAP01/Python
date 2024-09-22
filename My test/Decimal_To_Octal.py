def DecimalToBinary(num):
        if num>= 1:
            DecimalToBinary(num//8)
            print(num%8,end= '')

dec_val= int(input("Enter a number: "))
if __name__ == '__main__':
        dec_val = dec_val

DecimalToBinary(dec_val)