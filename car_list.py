car_list1 = ['MERCEDES', 9000000]
car_list2 = ['BMW', 5200000]
car_list3 = ['SUBARU', 5600000]
car_list4 = ['TOYOTA', 3400000]
car_list5 = ['COROLLA', 6500000]
car_list6 = ['AUDI', 2300000]
car_list7 = ['TESLA', 7700000]
car_list8 = ['DODGE', 3300000]
car_list9 = ['RANGE ROVER', 5500000]
car_list10 = ['JEEP', 6600000]

list = []

list.append(car_list1)
list.append(car_list2)
list.append(car_list3)
list.append(car_list4)
list.append(car_list5)
list.append(car_list6)
list.append(car_list7)
list.append(car_list8)
list.append(car_list9)
list.append(car_list10)

for i in list:
    print(i)

x = car_list1[1]
y = car_list10[1]
Total_sum = x + y
print('The sum of the first and last car prices are :', Total_sum, ';')


