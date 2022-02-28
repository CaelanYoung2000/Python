from ezgraphics import GraphicsWindow;

#Homework 02 - Caelan Young 09/21/2020

# EX01
# EX01
# EX01
# EX01


# Store input numbers
num1 = input('Enter an integer: ')
num2 = input('Enter another integer: ')

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('Sum: {0}'.format(sum))

# Subtract two numbers
difference = float(num1) - float(num2)

# Display the difference
print('Difference: {0} '.format(difference))

# Product of two
product = float(num1) * float(num2)

# Display the product
print('Product: {0} '.format(product))

average =  sum/2;

# Display the average
print('Average: {0} '.format(average))

# Subtracts two from one
distanceNum1 = float(num1) - float(num2)

# Subtracts one from two
distanceNum2 = float(num2) - float(num1)

if num1 > num2:
    print('Distance: {0} '.format(distanceNum1))
    print('Minimum: {0} '.format(num2))
    print('Maximum: {0} '.format(num1))

if num1 < num2:
        print('Distance: {0} '.format(distanceNum2))
        print('Minimum: {0} '.format(num1))
        print('Maximum: {0} '.format(num2))

# EX02
# EX02
# EX02
# EX02


# Store input numbers
gasInTank = input('\nEnter the amount of gas in the tank: ')
fuelEfficiency = input('Enter the fuel efficiency in mpg: ')
gallonOfGasCost = input('Enter the cost of a gallon of gas: ')

rateOfTravel = 100/float(fuelEfficiency)
priceToDrive100 = float(rateOfTravel) * float(1.99)

howFarCanTravel = float(gasInTank) * float(fuelEfficiency)

print('It takes ${0}  of fuel to drive 100 miles.'.format(priceToDrive100))
print('The car can travel {0} miles with the gas in the tank. '.format(howFarCanTravel))


# EX03
# EX03
# EX03
# EX03


# Store input numbers
time1 = input('\nPlease enter the first time: ')
time2 = input('Please enter the second time: ')

minutes1 = int(time1[:2]) * 60 + int(time1[2:])
minutes2 = int(time2[:2]) * 60 + int(time2[2:])

minutesDif = minutes2 - minutes1

minutes3 = int(time2[:2]) * 60 + int(time1[2:])
minutes4 = int(time1[:2]) * 60 + int(time1[2:])

minutesDif2 = minutes3 - minutes4
print('{0} hours {1} minutes'.format(minutesDif // 60, minutesDif % 60))


# EX04
# EX04
# EX04
# EX04


win = GraphicsWindow()
win.setTitle("My First Drawing")

canvas = win.canvas()
canvas.drawOval(60, 10, 100, 100)
canvas.drawOval(90, 40, 10, 10)
canvas.drawOval(120, 40, 10, 10)
canvas.drawLine(80, 80, 140, 80)
win.wait()

# EX05
# EX05
# EX05
# EX05
initialBalance = float(input("\nInitial balance: $"))
interest = float(input("Annual interest rate in percent: %"))

initialBalance = initialBalance+initialBalance*(interest/100)
print("After first month: ",initialBalance)

initialBalance = initialBalance+initialBalance*(interest/100)
print("After second month: ",initialBalance)

initialBalance = initialBalance+initialBalance*(interest/100)
print("After third month: ",initialBalance)


