# # a=10
# # b=20
# # sum=a+b
# # print(sum)
# a=30
# b=20
# print(not False)
# print((a>b))

# val1 = True
# val2 = True
# print("and operator is:", val1 and val2)


#type conversion
# a = int("2")
# b = 2.5

# sum = a+b 
# print(a + b)
# print(type(a))
# val = int(input("enter some value:"))
# print(type(val), val)
# name = str(input("enter name:"))
# age = int(input("enter age:"))
# marks = float(input("enter marks:"))

# print("wellcome", name)
# print("age", age)
# print("marks", marks)

# a = int(input("enter a val1:"))
# b = int(input("enter val2:"))
# print("the sum of two number is :", a+b)



#area of rectangle
# length = int
#wap to print average of two float numbers
# num1 = float(input("Enter first float value:"))
# num2 = float(input("Enter second float value:"))
# print("Average of two float number is :", (num1+num2)/2)


"""""
wap to input 2 int numbers, a and b.
print true if a is greater(input("the squire's length is:"))
# bredth = int(input("the squire's bredth is :"))
# print("the area of square is :",length*bredth)

 then or equal to b. if not print false
"""""
#  a = int(input("enter a :"))
#  b = int(input("enter b :"))
#  print( a >= b )
# print("hello world")






# ------------------------------------------------------------------------------------------------------------------------------------------

#strings
# str1 = "This is a string.\'We are creating it in python\'"
# print(str1)

#concatination: adding of two strings
#length of string
# str1 = "vinod"
# str2 = "venkat"
# str3 = "bavage"
# final_string = str1 +" " + str2 + " " + str3
# print(final_string)
# print(len(str1))
# print(len(str2))
# print(len(str3))
# print(len(final_string))

#indixing
# str = "vinod bavage"
# ch = str[6]
# print("the indexing charecter  is:", ch)

# slicing
# str = "vinod bavage"
# print(str[6:3:2])
# print(str[-6:-0])


#String functions
# str = "i am studing python from AppnaCollege"
# str = str.capitalize()
# str2 = "i am studing python from AppnaCollege"
# str2 = str.capitalize()
# print(str.endswith("lege"))
# print(str)
# print(str2)

# str = "i am studing python from AppnaCollege"
# print(str.capitalize())
# print(str.replace("python","java"))
# print("we fond item at index:",str.find("e"))
# print("we are counting the item to check how many time it is repeated:", str.count("e"))


# name = input("enter user's first name:")
# print(len(name))

# light = "yellow"

# if(light == "green"):
#     print("go")

# elif(light == "red"):
#     print("stop")

# elif(light == "yellow"):
#     print("wait")


# num = 5 

# if(num >= 4):
#     print("greater then 2")

# if(num >= 58):
#     print("number is less then 4")


"""
conditional statements
Grade students based on marks
  marks >=90, grade = "a"
  90 > marks >=80 grade = "b"
  80 > marks >=70 grade = "c"
  70 > marks, grade = "d"
"""
# marks = int(input("enter the students marks : "))

# if (marks >= 90):
#     print("grade A")
# elif(90 > marks >=80):
#     print("grade B")
# elif(80 > marks >=70 ):
#     print("grade C")
# elif(70 > marks >=35):
#     print("grade D")
# else:
#     print("fail")

# if (marks >= 90):
#     grade = "A"
# elif(90 > marks >=80):
#     grade = "B"
# elif(80 > marks >=70 ):
#     grade = "C"
# elif(70 > marks >=35):
#     grade = "D"
# else:
#     grade = "fail"

# print("the grade of the student is :",grade)    

# #Nesting
# age = int(input("Enter the age:"))
# if(age >= 18):
#     if(age >= 80):
#         print("can not drive")
#     else:
#         print("can drive")
# else:
#     print("can not drive")

# WAP to check if the number enterd is odd or even
# num = int(input("enter a number :"))
# if(num % 2 == 0):
#     print("The number is Even")
# else:
#     print("The number is odd")

#WAP to find greatest of four numbers enterd by the user

# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c = int(input("enter third number:"))
# d = int(input("enter the fourth number:"))
# if(a > b and a > c and a > d):
#     print("the first number is largest :", a)
# elif(b > c and b > d ):
#     print("the second  number is largest:", b)
# elif(c > d):
#     print("the third number is largest", c)
# else:
#     print("the fourth number is largest:",d)
 
# num = int(input("enter a number"))
# if(num % 5== 0):
#     print("multile of 5")
# else:
#    print("non multiple of 5")
# slicing
# str = "appna college"
# print(str[1:2:3])

#------------------------------------------------------------------------------------------------------------------------------------------


#lists

# Marks = [23.6, 58.3, 63.2, 94.1, 69.4, 45.3, 14.7, 99.9]
# print(Marks)
# print(type(Marks))
# print(len(Marks))
# print(Marks[3])
# print(Marks[7])

# student = ["vinod", 89, 22, "wadi"]
# print(student)
# print(type(student))
# print("length of student list is :",len(student))
# print("student name is :", student[0])
# student[0] = "praveen"
# print(student)

# List slicing
# student = ["vinod", 22, 99, "bhalki"]
# print(student)
# print(student[1:3])
# print(student[2:])
# print(student[:3])

#methods or functions

# val = [23, 43, 56, 82, 64, 82, 13, 453, 3, 42]
# list.append(4)
# print(val)
# list.sort()
# list.sort(reverse = True)
# list.reverse()
# list.insert()

# list=[3, 2, 3, 23, 43, 56, 82, 64, 82, 13, 453, 3]
# list.append(4 )
# print("The appemded list is",list)
# list.sort()
# print("the sorted list is:",list)
# list.sort(reverse = True)
# print("the reverse sorted list is:",list)
# list.reverse()
# print(list)                                         

# list=[3, 2, 3, 23, 43, 56, 82, 64, 82, 13, 453, 3]
# print(list.append(8))
# list=[3, 2, 3, 23, 43, 56, 82, 64, 82, 13, 453, 3]
# list.reverse()
# print(list)
# list=["banana", "apple", "mango", "graphs", "orange"]
# list.append("doubleapple")
# print("The appemded list is",list)
# list.sort()
# print("the sorted list is:",list)
# list.sort(reverse = True)
# print("the reverse sorted list is:",list)
# # list.reverse()
# # print("the reversed list is",list) 
# list.insert(3,"priya")  
# print("the inserted list is",list)
# list.remove("priya")
# print("the list after removing element is :",list)
# list.pop(3)
# print(list)

# list=[3, 2, 3, 23, 43, 56, 82, 64, 82, 13, 453, 3]
# print(type(list))
# str = "vinod bavage"
# print(type(str))
# tup = (5,8,9,12,"vinod")
# print(type(tup))

# a=[3, 2, 3, 23, 43, 56, 82, 64, 82, 13, 453, 3]
# print(type(a))
# b = "vinod bavage"
# print(type(b))
# c = (5,8,9,12,"vinod")
# print(type(c))
# d = (1)
# print(type(d))
# e = (1.23)
# print(type(e))
# f = ('vinpd')
# print(type(f))
# g = (2,)    #if there is a single value in tuple you must give a coma
# print(type(g))

# tup = (5, 8, 65, 42, "vinod",200,5)
# print(type(tup))
# print(tup[1])
# print(tup[5])
# print(tup[4])
# print(tup.count(5))
# print(tup.index("vinod"))#in bracket write the  element not index


#WAP to ask the user to enter the names of three movies and store them in a list

movie1 = list[input("enter the 1st movie name:")]
movie2 = list[input("enter the 2nd movie name:")]
movie3 = list[input("enter the 3rd movie name:")]
print(movie1, movie2, movie3)


