import turtle
t = turtle.Turtle()
t.speed(0)
color =0
t.width(4)
turtle.bgcolor('black')
t.color('white')
for i in range(100000000):
    x = 1
    x = i/100
    t.lt(6)
    t.fd(x)
    if color//30 == 0:
        color = color +1
    if color//30 == 1:
        t.color('red')
        color = color +1
    if color//30 == 2:
        t.color('orange')
        color = color +1
    if color//30 == 3:
        t.color('yellow')
        color = color +1
    if color//30 == 4:
        t.color('green')
        color = color +1
    if color//30 == 5:
        t.color('skyblue')
        color = color +1
    if color//30 == 6:
        t.color('blue')
        color = color +1
    if color//30 == 7:
        t.color('purple')
        color = color +1
    if color//30 == 8:
        t.color('white')
        color = 0
