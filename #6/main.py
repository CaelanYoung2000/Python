import random

#Ex01
#Ex01
#Ex01
#Ex01


lst = []
for i in range(10):
    lst.append(random.randint(1,9))

print("List values =>",lst)

# element at an even index.
print("\nElements at even index:")
for i in range(len(lst)):
    if(i%2==0):
        print(lst[i],end=" ")
print()

#even element.
print("\nThe even elements are: ")
for i in range(len(lst)):
    if(lst[i]%2==0):
        print(lst[i],end=" ")
print()

#reverse order.
print("\nIne reverse order:")
for i in range(len(lst)-1,-1,-1):
    print(lst[i],end=" ")
print()

#first and last element.
print("\nFirst and last:")
print(lst[0],lst[-1])

#Ex01
#Ex01
#Ex01
#Ex01



#Ex02
#Ex02
#Ex02
#Ex02

temp_list=[1,2,3,4,5,6,7,8,9,10]
permutation_list=[]

for i in range(10):
    val =random.choice(temp_list)
    permutation_list.append(val)
    temp_list.remove(val)

print("\nPermutation list:",permutation_list,"\n")


#Ex02
#Ex02
#Ex02
#Ex02




#Ex03
#Ex03
#Ex03
#Ex03

n=1
captions=[]
values=[]
while n!=-1:
    c = str(input("Enter the caption (or -1 to stop) :")) # get caption
    if c=='-1':
        n=-1
        break
    v = int (input("Enter the value for "+c+" :")) # get value
    while v<1 or v>30:
       v = int (input("re-Enter the value(1-30) for "+c+" :")) # between 1 to 30 then re-enter value
    captions.append(c) # add caption to list
    values.append(v)   # add value to list

    print("\n\n")
for i in range(len(captions)):
    a = values[i] // 2
    for j in range(a):
        print(" ", end =" ")
    print(captions[i], end =" ")
    for j in range(values[i]):
        print("*", end =" ")

    print ("<=",values[i],"\n")

#Ex03
#Ex03
#Ex03
#Ex03


#Ex04
#Ex04
#Ex04
#Ex04

def nameofBestCustomers(sales, customers):
    sale = max(sales)
    index = sales.index(sale)
    winner = customers[index]
    return winner,sale

sales = []
customers = []

while True:
    name = input("Enter the name of customer : ")
    purchase = float(input("Enter the sales to {} : ".format(name)))
    sales.append(purchase)
    customers.append(name)
    c = input("Want to enter more customers (y/n) : ")
    if c == 'n' or c=='N':
        break

winner = nameofBestCustomers(sales,customers)
print("{} was the best customer, with a purchase of {}".format(winner[0],winner[1]))

#Ex04
#Ex04
#Ex04
#Ex04
