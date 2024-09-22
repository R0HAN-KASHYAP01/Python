# weight_in_kg = float(input("Enter your weight: "))
# height_in_meter = float(input("Enter your height: "))
# BMI = weight_in_kg/(height_in_meter**2)
# print("Your Body Mass Index is,", BMI)

def BMI(kg,m):
    return kg/(m**2)
weight_in_kg = float(input("Enter your weight: "))
height_in_meter = float(input("Enter your height: "))
a = BMI(weight_in_kg,height_in_meter)
print(a)