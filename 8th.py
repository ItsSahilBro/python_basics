# problem 1

# Length =input("Enter the legnth :")
# Breadth =input("Enter the breadth :")

# if Length >= Breadth:
#     print("Its a Square ." )

# else:
#     print("Its a Rectangle.")

# problem 2

# a =input("Write a integer number :")
# b =input("Write another integer number :")
# c =input("Write another integer number : ")

# if a > b and c:
#     print("1st integer is greatest.")

# elif b > a and c:
#     print("2nd integer is greatest.")

# else:
#     print("3rd integer is greatest.")

# prob 3

# a = int(input("Enter number :"))

# if a%2 == 0:
#     print(a,"is an even number.")

# else:
#     print(a,"is a odd number")

# prob 4

# marks =int(input("Enter your marks :"))

# if marks >= 91:
#     print("Your grade is A.")

# elif marks >= 81 and marks <= 90:
#     print("Your grade is B.")
    
# elif marks >=60 and marks <= 80 :
#     print("Your grade is C.")

# else:
#     print("Your grade is D.")

year = int(input("Enter Year = "))
if year%400==0 and year%100==0:
    print(year,",It is a leap year")
elif year%4==0 and year%100!=0:
    print(year,",It is a leap year")
else:
    print(year, ",It is not leap year")