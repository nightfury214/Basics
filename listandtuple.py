"""difference between list and tuple"""

import timeit

list_time = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print(f"list time:{list_time}")  #slower
print(f"tuple time:{tuple_time}") #faster


fruits = ["apple","banana"] 
fruits.append("orange") ##possible about list and impossible about tuple
print(fruits)

m_list = [1,2,3,4]
m_list[3] = 5 ##possible about list and impossible about tuple
print(m_list)



