# List = ["24", "35","36","88"]
# List = list(map(int, List))
#
# print(List[2] + 1)

# ****************FILTER******************
# number = [34, 53,5, 35,3, 5, 3, 5,3]
# is_greater = list(filter(lambda x: x>10 , number))
# print(is_greater)
#***************REDUCE*******************
from functools import reduce
number = [2,435,65,46,46,46,4,6]
division = reduce(lambda x,y: x/y , number)
print(division)