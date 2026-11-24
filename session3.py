# []

# scores = [20,12,15,9,16,8,14,2]
# print(scores)
# print(type(scores)) 
# print(scores[3])

# names = ["amir","ali","reza","ahmad","jafar"]
# print(names)
# print(names[4])

# names = ["peyman","amir","ahmaad","mohammad"]

# # update
# names[2] = "ahmad"
# print(names)


# # ADD ITEMS
# # append
# names.append("arsham")
# print(names)

# # insert
# names.insert(1,"agha mehdi")
# print(names)

# #DELETE

# # BY INDEX
# #  del
# del names[1]
# print(names)

# # pop
# # deleted_name = names.pop(0)
# # print(names)
# # print(deleted_name)

# deleted_name = names.pop()
# print(names)
# print(deleted_name)

# # remove
# names.remove("amir")
# print(names)

# numbers = [10,12,9,5,20,14,29]
# numbers.sort()
# numbers.sort(reverse=True)
# print(numbers)

# names = ["amir","ali","reza","ahmad"]
# names.sort()
# print(names)

# new_names = sorted(names)
# print(new_names)
# print(names)

# names.reverse()
# print(names)




# names = ["amir","ali","reza","ahmad"]
# print(len(names))

# name = "amirhossein"
# print(len(name))

# scores = [10,12,9,8,7,20]

# print(max(scores))
# print(min(scores))
# print(sum(scores))

# print(sum(scores)/len(scores))


# cars = ["benz","bmw","prado"]
# carsale_cars = cars

# cars.append("206")
# carsale_cars.append("405")

# print(cars)
# print(carsale_cars)


# cars = ["benz","bmw","prado"]
# carsale_cars = cars[:]

# cars.append("206")
# carsale_cars.append("405")

# print(cars)
# print(carsale_cars)

# a=10
# b=a

# a=12


score = int(input("please enter score: "))
if score>=10:
    print("pass")
else:
    print("fail")
