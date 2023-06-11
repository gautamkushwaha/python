# print("1st day")
# print("2nd day")
# print("3rd day")
# print("4th day")

# name="gautam"
# age =22
# is_adult = True
# print(name)
# print(age)


# taking input from users

# name = input("what is your name?")
# print("Hello" +  name)

# type conversion

# old_age = input('enter your old age:')
# new_age = int(old_age) + 2
# print(new_age)

# print(float(new_age)) 
# str()
# bool()


#  sum of two numbers

# first = input("enter first number: ")
# second = input("enter second number: ")
# sum = int(first) + int(second)
# print("the sum is" +  str(sum))



#string
# name = "Tony Stark"

# print(name.lower())
# print(name)
# print(name.find('stark'))

# print(name.replace("Stark","Mahato"))
# print(name)

# print("M" in name)



# Arithmetic operators
 
# print(2 +3)
# print(2 *3)
# print(5 /3)
# print(5// 3)
# print(5%2)
# print(5**2)

#operators precedence

# result = 2 + 3 / 5
# print(result)

# print(not 3 >2)

# i = 5
# while(i >= 1):
#  print(i * "*")
#  i = i - 1


# i = 1
# while(i <= 5):
#  print(i * "*")
#  i = i + 1

# for i in range(5):
#   print(i * "*")
#   i = i + 1

# for i in range(10):
#     print(i * "*")
#     i +=1


#Lists
# friends=["Gautam","Ramesh","Lithusan","Atal"]
# print(friends[0:3])

# for friend in friends:
#     print(friend)


#operations in Lists
# # friends.insert(3,"Sekhar")
# print("Ramesh" in friends)
# print(len(friends))

# i =0
# while i <len(friends):
#     print(friends[i])
#     i=i+1


# friends.clear()
# print(friends)


#Break and continue

friends =[1, 3, 5, 6]

i= 0
while i< len(friends):
    if(i==5):
        break
    i+=1
    print(i)
