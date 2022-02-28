import collections

import csv

#EX01
#EX01
#EX01
#EX01


fileName = input("Enter the Name of file: ") #Get user input for file name

fileWords = [] #Stores all file text words


with open(fileName,'r') as f: #Open user input file name

    fileText = f.readlines()

for line in fileText: #Searches each line and stores to fileWords

    fileWordsReadingLine = line.split()

    fileWords.extend(fileWordsReadingLine)


uniqueWords = collections.Counter(fileWords)

print("The total fileWords is:",len(fileWords))

print("the total unique fileWords is:", len(uniqueWords))

onlyTop15 = uniqueWords.most_common(15) #Limit printing to only top 15 words

print("{0:>3} {1:<15} {2:>10}".format("No.","Word","Frequency"))


for i,x in enumerate(onlyTop15):

    print("{0:>3} {1:<15} {2:>10}".format(str(i+1)+".",str(x[0]),str(x[1])))


#EX01
#EX01
#EX01
#EX01


#EX02
#EX02
#EX02
#EX02


studentGrading = {} #Stores student information

while True:

   print("\n(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ", end='') #User prompt for functionality

   userChoice = input("") #Stores user input

   if(userChoice == 'A'): #Utilized when user enters A to add a student

       studentName = input("Enter the name of the student: ")

       if (studentName in studentGrading.keys()):

           print("Sorry, that student already exists")

       else:

        studentGrade = input("Enter the student's grade: ")

        studentGrading[studentName] = studentGrade

   elif(userChoice == 'M'): #Utilized when user enters M to modify the student list

       studentName = input("Enter the name of the student to modify: ")

       if(studentName not in studentGrading.keys()):

           print("Sorry, that student doesn't exist")

       else:

        print("The current grade is ", studentGrading[studentName])

        studentGrade = input("Enter the new grade:")

        studentGrading[studentName]=studentGrade

   elif(userChoice=='R'): #Utilized when user enters R to remove a student from the list

       studentName = input("What student do you want to remove: ")

       if(studentName not in studentGrading.keys()):

           print("Sorry, the student doesn't exist.")

           continue;

       studentGrading.pop(studentName)

   elif(userChoice=='P'): #Utilized when user enters P to print out the student records

       fixedList = studentGrading.keys()

       sorted(fixedList)

       for A in fixedList:

           print(A+":"+studentGrading[A])

   elif(userChoice=='Q'): #Utilized when user enters Q to quit

       print("Goodbye!")

       break

   else:

       print("Sorry, that wasn't a valid choice")


#EX02
#EX02
#EX02
#EX02


#EX03
#EX03
#EX03
#EX03


#Inilitze for functionality
highestScore = 0

lowestScore = 100

idForHighestScore = 0

idForLowestScore = 0

highestScoreName = ""

LowestScoreName = ""

csvReader = csv.DictReader(open("student.csv")) #Open csv file

for row in csvReader:

        #Stores information if highest score
   if int(row['score']) > highestScore :

       highestScore = int(row['score'])

       idForHighestScore = int(row['id'])

       highestScoreName = row['name']

        #Stores information if lowest score
   if int(row['score']) < lowestScore :

       lowestScore = int(row['score'])

       idForLowestScore = int(row['id'])

       LowestScoreName = row['name']

print("\nStudent with the highest score is:")

print("=> Name: " + highestScoreName + ", Id: " + str(idForHighestScore))

print("Student with the lowest score is:")

print("=> Name: " + LowestScoreName + ", Id: " + str(idForLowestScore))


#EX03
#EX03
#EX03
#EX03