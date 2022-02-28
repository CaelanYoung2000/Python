# EX01
# EX01
# EX01
# EX01

#Check if they are all equal
def allTheSame(x, y, z):
    if x == y and x == z:
        return True

    else:
        return False

#Check if they are sorted from smallest to largest
def sortedFunc(x, y, z):
    if x > y and y > z:
        return True

    elif x > z and z > y:
        return True

    elif y > x and x > z:
        return True

    elif y > z and z > x:
        return True

    elif z > x and x > x:
        return True

    elif z > y and y > x:
        return True

    else:
        return False

#Print results
def main():

    x = float(input("Enter a number for x: "))
    y = float(input("Enter a number for y: "))
    z = float(input("Enter a number for z: "))

    print("All the same: ", allTheSame(x, y, z))
    print("Sorted: ", sortedFunc(x, y, z))

main()

# EX01
# EX01
# EX01
# EX01



# EX02
# EX02
# EX02
# EX02


#Counts vowels staring from 0
def countVowels(string):
    count = 0
    for ch in string:
        if ch in "aeiouAEIOU":
            count += 1
    return count

#User input/results
def main():
    s = input("\nEnter a string: ")
    print("The string", s, "contains", countVowels(s), "vowels")


main()

# EX02
# EX02
# EX02
# EX02



# EX03
# EX03
# EX03
# EX03

#Converts c value into roman numbering
def value(c):

   if c == 'M':

       return 1000

   elif c == 'D':

       return 500

   elif c == 'C':

       return 100

   elif c == 'L':

       return 50

   elif c == 'X':

       return 10

   elif c == 'V':

       return 5

   elif c == 'I':

       return 1


#Prompt user input
romanString=input("\nPlease enter a Roman number: ")

total = 0


#While not empty continue
while(romanString!=''):

#Find length of roman number
    length=len(romanString)



    if( value(romanString[length-1])<= value(romanString[length-2]) or len(romanString)==1 ):

#Adds value of first character to total
        total+=value(romanString[length-1])

#Remove the first character from the string
        romanString=romanString[0:length-1]

    else:

        total+=value(romanString[length-1])-value(romanString[length-2])

        romanString=romanString[0:length-2]

print ('The Roman number you have entered is equal to: '+str(total))


# EX03
# EX03
# EX03
# EX03


# EX04
# EX04
# EX04
# EX04

def isValidPassword(password):

    if (len(password)<8):
        print("\nmust be at least 8 characters long")
        return False

    if not any(digit.isdigit() for digit in password):
        print("\nmust have at least one digit")
        return False

    if not any(digit.isupper() for digit in password):
        print("\nmust have at least one upper case")
        return False


    if not any(digit.islower() for digit in password):
        print("\nmust have at least one lower case")
        return False

    return True

def main():

    isSafe = False
    isMatch = False
    password = ""
    reenter_password = ""

    while(isSafe == False):

        password = input("\nEnter your password: ")

        isSafe = isValidPassword(password)

    while(isMatch == False):

        reenter_password = input("\nRe-enter your password: ")

    if (password == reenter_password):
        print("That pair of passwords will work.")

main()

# EX04
# EX04
# EX04
# EX04
