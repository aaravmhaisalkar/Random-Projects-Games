import turtle
import time
import sys
shape = True
debounce = 0
circlesUsed = []
circles = []
squares = []

t = turtle.Turtle()
distanceChecker = turtle.Turtle()
distanceChecker.hideturtle()
distanceChecker.speed(0)
distanceChecker.penup()
screen = turtle.Screen()
t.speed(0)
t.hideturtle()

locations = [
    [-100,100],
    [0,100],
    [100,100],
    [-100,0],
    [0,0],
    [100,0],
    [-100,-100],
    [0,-100],
    [100,-100]
]

def square(middle):
    t.penup()
    t.goto(middle)
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.pendown()
    for _ in range(4):
        t.forward(100)
        t.right(90)
             
for location in locations:
    square(location)

def f(x,y):
    global debounce
    global circlesUsed
    
    if time.time() - debounce <= .5:
        return
    debounce = time.time()
    distances = []
    t.penup()
    t.goto(x,y)
    distanceChecker.goto(0,0)
    if t.distance(distanceChecker) > 205:
        write("Out of bounds")
        return
    else:
        for i in locations:
            distanceChecker.goto(i)
            distance = t.distance(distanceChecker)
            distances.append(distance)
        mindistance = min(distances)
        circleNum = distances.index(mindistance)
        if circleNum in circlesUsed:
            if len(circlesUsed) >= 9:
                write("Game over, draw.")
                sys.exit()
            write("Spot is taken")
            return
        circlesUsed.append(circleNum)
        print(f'Circle number {circleNum+1}')
        markShape(circleNum)
        logic()

def markShape(num):
    global shape
    global circles
    global squares
    if shape == True:
        circles.append(num+1)
        x = int(locations[num][0])
        y = int(locations[num][1]) - 40
        t.goto(x,y)
        t.pendown()
        t.circle(40)
        t.penup()
    elif shape == False:
        squares.append(num+1)
        x = int(locations[num][0]) - 20
        y = int(locations[num][1]) + 20
        t.goto(x,y)
        t.pendown()
        for _ in range(4):
            t.forward(45)
            t.right(90)
        t.penup()
        
    shape = not shape
    print(circles)
    print(squares)

def write(text):
    distanceChecker.goto(-220,250)
    distanceChecker.pendown()
    distanceChecker.write(f"{text}", font=("Arial", 16, "bold"))
    distanceChecker.penup()
    time.sleep(1.5)
    distanceChecker.clear()

def logic():
    #1. if the lists have numbers in sequential order (1,2,3 or 7,8,9)
    #2. if the lists have numbers in ascending order from 3 (1,4,7 or 3,6,9)
    #3. if the number has the numbers (1,5,7) or (1,5,9), this might need to be hardcoded to check
    global circles
    global squares
    
    rules = [
        {3,5,7},
        {1,5,9},
        {1,2,3},
        {4,5,6},
        {7,8,9},
        {1,4,7},
        {2,5,8},
        {3,6,9}
    ]
    for i in rules:
        if i.issubset(set(squares)):
            write("game over")
            time.sleep(4)
            sys.exit()
        if i.issubset(set(circles)):
            write("game over")
            time.sleep(4)
            sys.exit()
        
screen.onscreenclick(f)  

screen.mainloop()


