from ezgraphics import GraphicsImage, GraphicsWindow
# EX01
# EX01
# EX01
# EX01

x=int(input('Enter smaller integer: '))
y=int(input('Enter larger integer: '))
xPlaceHolder = x
yPlaceHolder = y

temp = x
while x < y:
  x = x + 2
  temp = temp + x
  sum = temp
  if x > y:
    break

print('The total of the odd numbers from ',xPlaceHolder,' to ',yPlaceHolder,' is ',sum)

z=int(input("\nEnter an integer: "))
zPlaceHolder = z
sum_s=0

while(z!=0):
    r=z%10
    if(r%2==1):
        sum_s+=r
    z=int(z/10)

print("The total of the odd digits in ",zPlaceHolder,' is ',sum_s,'\n')

# EX01
# EX01
# EX01
# EX01


# EX02
# EX02
# EX02
# EX02

count2 = 1

while count2 <=10:
    print(count2,'', end = '')
    count2 = count2 + 1

count2 = 1
print('\n')

while count2 <=10:
    print(count2 * 2,'', end = '')
    count2 = count2 + 1

count2 = 1
print('\n')

while count2 <= 10:
    print(count2 * 3, '', end='')
    count2 = count2 + 1

count2 = 1
print('\n')

while count2 <= 10:
    print(count2 * 4, '', end='')
    count2 = count2 + 1

count2 = 1
print('\n')

while count2 <= 10:
    print(count2 * 5, '', end='')
    count2 = count2 + 1

count2 = 1
print('\n')

while count2 <= 10:
    print(count2 * 6, '', end='')
    count2 = count2 + 1

count2 = 1
print('\n')

while count2 <= 10:
    print(count2 * 7, '', end='')
    count2 = count2 + 1

count2 = 1
print('\n')

while count2 <= 10:
    print(count2 * 8, '', end='')
    count2 = count2 + 1

count2 = 1
print('\n')

while count2 <= 10:
    print(count2 * 9, '', end='')
    count2 = count2 + 1

count2 = 1
print('\n')

while count2 <= 10:
    print(count2 * 10, '', end='')
    count2 = count2 + 1

count2 = 1
print('\n')

# EX02
# EX02
# EX02
# EX02


# EX03
# EX03
# EX03
# EX03

val = float(input("How many yen in a dollar (e.g., 104.80): "))


dollars = float(input("Enter an amount in dollars (0 to quit): "))

while dollars!=0:
        print("{:.2f} dollars = {:.2f} yens".format(dollars,val*dollars))
        dollars = float(input("Enter amount in dollars to convert: (0 to quit) "))

# EX03
# EX03
# EX03
# EX03


# EX04
# EX04
# EX04
# EX04

filename = input("\nEnter the name of the image file: ")

print('See the converted image!')

win = GraphicsWindow(525, 350)
canvas = win.canvas()

image = GraphicsImage(filename)

width = image.width()
height = image.height()

for row in range(height):
    for col in range(width):

        red = image.getRed(row, col)
        green = image.getGreen(row, col)
        blue = image.getBlue(row, col)

        num = 0

        redS = redE = redSE = 0
        greenS = greenE = greenSE = 0
        blueS = blueE = blueSE = 0

        if row != height - 1:
            redS = image.getRed(row + 1, col)
            greenS = image.getGreen(row + 1, col)
            blueS = image.getBlue(row + 1, col)
            num = num + 1

        if col != width - 1:
            redE = image.getRed(row, col + 1)
            greenE = image.getGreen(row, col + 1)
            blueE = image.getBlue(row, col + 1)
            num = num + 1

        if col != width - 1 and row != height - 1:
            redSE = image.getRed(row + 1, col + 1)
            greenSE = image.getGreen(row + 1, col + 1)
            blueSE = image.getBlue(row + 1, col + 1)
            num = num + 1

        if num == 0:
            image.setPixel(row, col, 0, 0, 0)

        else:
            redNeighbors = (redS + redE + redSE) / num
            greenNeighbors = (greenS + greenE + greenSE) / num
            blueNeighbors = (blueS + blueE + blueSE) / num

            distance = abs(red - redNeighbors) + abs(green - greenNeighbors) + abs(blue - blueNeighbors)

            if distance > 30:
                image.setPixel(row, col, 0, 0, 0)
            else:
                image.setPixel(row, col, 255, 255, 255)

canvas.drawImage(image)

win.wait()

# EX04
# EX04
# EX04
# EX04