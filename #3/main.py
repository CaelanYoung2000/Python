from matplotlib import pyplot
#Homework 03 - Caelan Young 10/07/2020

# EX01
# EX01
# EX01
# EX01

num1 = input('Enter the first integer: ')
num2 = input('Enter the second integer: ')
num3 = input('Enter the third integer: ')

if num1 == num2 == num3:
    print("They are all the same.")

elif num1 != num2 != num3:
    print("They are all different.")

else:
    print("They are neither all the same nor all different.")


# EX01
# EX01
# EX01
# EX01




# EX02
# EX02
# EX02
# EX02

grade = input("\nEnter a Letter grade: ")
value = 0
if (grade == "A+"):
    value = 4.0
elif (grade == "A"):
    value = 3.7
elif(grade == "A-"):
    value = 3.4
elif (grade == "B+"):
    value = 3.3
elif (grade == "B"):
    value = 3.0
elif (grade == "B-"):
    value = 2.7
elif (grade == "C+"):
    value = 2.3
elif (grade == "C"):
    value = 2.0
elif (grade == "C-"):
    value = 1.7
elif (grade == "D+"):
    value = 1.3
elif (grade == "D"):
    value = 1.0
elif (grade == "D-"):
    value = 0.7
elif (grade == "F"):
    value = 0.0
else:
    value = "Invalid grade entered. Try again."
print("The numeric value is",value)

# EX02
# EX02
# EX02
# EX02




# EX03
# EX03
# EX03
# EX03

pyplot.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            [1.1, 10.0, 25.4, 44.5, 61.0, 71.6, 72.7, 65.9, 54.6, 31.9, 19.9, 4.8])

pyplot.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            [-16.9, -12.7, -2.5, 20.6, 37.8, 49.3, 52.3, 46.4, 35.1, 16.5, -5.7, -12.9])

pyplot.xlim(0.8, 12.2)

pyplot.title("Average Temperatures in Fairbanks")
pyplot.xlabel("Month")
pyplot.ylabel("Temperature")
pyplot.legend(["High", "Low"])
pyplot.xticks(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

pyplot.show()

# EX03
# EX03
# EX03
# EX03



# EX04
# EX04
# EX04
# EX04

while True:
   amt1 = float(input("\nInput initial amount for Checking account:"))
   if amt1 < 0:
      print("Please enter a positive amount")
   else:
      break
while True:
   amt2 = float(input("Input initial amount for Saving account:"))
   if amt2 < 0:
      print("Please enter a positive amount")
   else:
      break

while True:
      print("\n1.Deposit")
      print("2.Withdrawl")
      print("3.Transfer")
      print("4.Exit")
      n = int(input("Enter choice:"))
      if n == 4:
         break
      if n == 1:
         print("\n1.Checking Account")
         print("2.Savings Account")
         m = int(input("Enter choice:"))
         if m == 1:
            dep1 = float(input("\nEnter deposit amount for Checking Account:"))
            amt1 = amt1 + dep1
            print("Success")
         if m == 2:
            dep2 = float(input("Enter deposit amount for Savings Account:"))
            amt2 = amt2 + dep2
            print("Success")
      if n == 2:
         print("\n1.Checking Account")
         print("2.Savings Account")
         m = int(input("Enter choice:"))
         if m == 1:
            with1 = float(input("\nEnter withdrawl amount for Checking Account:"))
            if with1 > amt1:
               print("Insufficient funds")
            else:
               amt1 = amt1 - with1
               print("Success")
         if m == 2:
            with2 = float(input("\nEnter withdrawl amount for Savings Account:"))
            if with2 > amt2:
               print("Insufficient funds")
            else:
               amt2 = amt2 - with2
               print("Success")

      if n == 3:
         print("\n1.Checking Account")
         print("2.Savings Account")
         m = int(input("Enter choice:"))
         if m == 1:
            tr1 = float(input("\nEnter transfer amount to Checking Account:"))
            if tr1 > amt2:
               print("Insufficient funds")
            else:
               amt2 = amt2 - tr1
               amt1 = amt1 + tr1
               print("Success")
         if m == 2:
            tr2 = float(input("\nEnter transfer amount to Savings Account:"))
            if tr2 > amt1:
               print("Insufficient funds")
            else:
               amt1 = amt1 - tr2
               amt2 = amt2 + tr2
               print("Success")

print("\nChecking account total balance:",amt1)
print("Saving account total balance:",amt2)


# EX04
# EX04
# EX04
# EX04
