#EX01
#EX01
#EX01
#EX01


try:

    userInputFile = input('Enter the input file name: ') #Get user input for file name

    openedFile = open(userInputFile, 'r') #Open the user input file

    #Initilize for calculations
    columnOneTotal = 0.0
    columnTwoTotal = 0.0
    amountInColumn = 0.0
    columnOneAverage = 0.0
    columnTwoAverage = 0.0

    #Calculate column totals and averages
    for line in openedFile:

        separatedColumns = line.split() #Split the columns apart

        if len(separatedColumns) > 1:

            columnOneTotal += float(separatedColumns[0]) #Column one total

            columnTwoTotal += float(separatedColumns[1]) #Column two total

            amountInColumn = amountInColumn + 1

    columnOneAverage = columnOneTotal / amountInColumn #Column one average

    columnTwoAverage = columnTwoTotal/ amountInColumn #Column two average

    #Close the file
    openedFile.close()

    print('The averages are',columnOneAverage,'and',columnTwoAverage)
except IOError:
    print('That file could not be opened.')


#EX01
#EX01
#EX01
#EX01


#EX02
#EX02
#EX02
#EX02


studentId = input('\nEnter the student id: ') #User input for student Id

print('\nStudent ID',studentId)

with open('classes.txt','r') as fileOpen:
    for line in fileOpen:
        lineSplittingOne = line.split()
        fileOpen = lineSplittingOne[0]+'.txt'

        #Split into class and letter grade

        with open(fileOpen,'r') as fileOpen2:
            for lines in fileOpen2:
                lineSplittingTwo = lines.split()
                if lineSplittingTwo[0] == studentId:
                    print(lineSplittingOne[0],lineSplittingTwo[1])


#EX02
#EX02
#EX02
#EX02


#EX03
#EX03
#EX03
#EX03


userInputFile = input('\nEnter the input file name: ') #Get user input for file name

filename = userInputFile #Holds input file name

serviceOffered = {} #Holds service after stored

#open file
with open(filename) as openFile:

    for line in openFile:

        cost = line.strip().split(';')

        service = cost[1]

        amount = float(cost[2])

        serviceOffered[service] = serviceOffered.get(service,0)+amount

print('Totals: ')

for target in serviceOffered:

    print(target + ':',serviceOffered[target])


#EX03
#EX03
#EX03
#EX03