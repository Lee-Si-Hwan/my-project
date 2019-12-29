import turtle
import random


#생성
bestpoint = 0
ar1 = 0
ar2 = 0
ar3 = 0
ar4 = 0
ar5 = 0
ar6 = 0
ar7 = 0
ar8 = 0
ar9 = 0
ar10 = 0
ar11 = 0
ar12 = 0
ar13 = 0
ar14 = 0
ar15 = 0

t1 = turtle.Turtle()
pen = turtle.Turtle()

b1_1 = turtle.Turtle()
b1_2 = turtle.Turtle()
b1_3 = turtle.Turtle()
b1_4 = turtle.Turtle()
b1_5 = turtle.Turtle()

b2_1 = turtle.Turtle()
b2_2 = turtle.Turtle()
b2_3 = turtle.Turtle()
b2_4 = turtle.Turtle()
b2_5 = turtle.Turtle()

b3_1 = turtle.Turtle()
b3_2 = turtle.Turtle()
b3_3 = turtle.Turtle()
b3_4 = turtle.Turtle()
b3_5 = turtle.Turtle()
#모양
b1_1.up()
b1_2.up()
b1_3.up()
b1_4.up()
b1_5.up()

b2_1.up()
b2_2.up()
b2_3.up()
b2_4.up()
b2_5.up()

b3_1.up()
b3_2.up()
b3_3.up()
b3_4.up()
b3_5.up()

b1_1.ht()
b1_2.ht()
b1_3.ht()
b1_4.ht()
b1_5.ht()

b2_1.ht()
b2_2.ht()
b2_3.ht()
b2_4.ht()
b2_5.ht()

b3_1.ht()
b3_2.ht()
b3_3.ht()
b3_4.ht()
b3_5.ht()

b1_1.shape("square")
b1_2.shape("square")
b1_3.shape("square")
b1_4.shape("square")
b1_5.shape("square")

b2_1.shape("square")
b2_2.shape("square")
b2_3.shape("square")
b2_4.shape("square")
b2_5.shape("square")

b3_1.shape("square")
b3_2.shape("square")
b3_3.shape("square")
b3_4.shape("square")
b3_5.shape("square")

#출발선 배치
b1_1.speed(10)
b1_2.speed(10)
b1_3.speed(10)
b1_4.speed(10)
b1_5.speed(10)

b2_1.speed(10)
b2_2.speed(10)
b2_3.speed(10)
b2_4.speed(10)
b2_5.speed(10)

b3_1.speed(10)
b3_2.speed(10)
b3_3.speed(10)
b3_4.speed(10)
b3_5.speed(10)


b1_1.goto(-275,300)
b1_2.goto(-275,300)
b1_3.goto(-275,300)
b1_4.goto(-275,300)
b1_5.goto(-275,300)

b2_1.goto(-225,300)
b2_2.goto(-225,300)
b2_3.goto(-225,300)
b2_4.goto(-225,300)
b2_5.goto(-225,300)

b3_1.goto(-175,300)
b3_2.goto(-175,300)
b3_3.goto(-175,300)
b3_4.goto(-175,300)
b3_5.goto(-175,300)

t1.speed(10)
pen.speed(10)#속도 최대치


screen = t1.getscreen()

r = 0 #각도 기준


def reset():
    global r
    r = 0    
    t1.goto(-200,0)
    t1.seth(90)

def point_up():
    global point
    point = point + 10
    pen.undo()
    pen.write(point, font=("Arial",15, "normal"))
    
def rightkey():
    global r
    r = r + 5
    l = 25 * 3.14 * 1/15
    t1.circle(25, l)


def leftkey():
    global r
    r = r - 5
    l = 25 * 3.14 * 1/15
    t1.circle(25, -l)

def replay():
    global point
    global ar1
    global ar2
    global ar3
    global ar4
    global ar5
    global ar6
    global ar7
    global ar8
    global ar9
    global ar10
    global ar11
    global ar12
    global ar13
    global ar14
    global ar15
    point = 0
    ar1 = 0
    ar2 = 0
    ar3 = 0
    ar4 = 0
    ar5 = 0
    ar6 = 0
    ar7 = 0
    ar8 = 0
    ar9 = 0
    ar10 = 0
    ar11 = 0
    ar12 = 0
    ar13 = 0
    ar14 = 0
    ar15 = 0
    
    pen.undo()
    pen.goto(200,200)
    pen.write(point, font=("Arial",15, "normal"))
    b1_1.ht()
    b1_2.ht()
    b1_3.ht()
    b1_4.ht()
    b1_5.ht()

    b2_1.ht()
    b2_2.ht()
    b2_3.ht()
    b2_4.ht()
    b2_5.ht()

    b3_1.ht()
    b3_2.ht()
    b3_3.ht()
    b3_4.ht()
    b3_5.ht()

    b1_1.goto(-275,300)
    b1_2.goto(-275,300)
    b1_3.goto(-275,300)
    b1_4.goto(-275,300)
    b1_5.goto(-275,300)

    b2_1.goto(-225,300)
    b2_2.goto(-225,300)
    b2_3.goto(-225,300)
    b2_4.goto(-225,300)
    b2_5.goto(-225,300)

    b3_1.goto(-175,300)
    b3_2.goto(-175,300)
    b3_3.goto(-175,300)
    b3_4.goto(-175,300)
    b3_5.goto(-175,300)
    
    b1_1.goto(-280, b1_1.ycor()-20)
    b1_1.st()
    ar1 = 1

    b2_1.goto(-215, b2_1.ycor()-20)
    b2_1.st()
    ar6 = 1

    b3_1.goto(-180, b3_1.ycor()-20)
    b3_1.st()
    ar11 = 1
    
def go():
    global r
    global point
    global bestpoint
    global ar1
    global ar2
    global ar3
    global ar4
    global ar5
    global ar6
    global ar7
    global ar8
    global ar9
    global ar10
    global ar11
    global ar12
    global ar13
    global ar14
    global ar15

    t1.seth(0)
    t1.lt(r)
    while True:
        t1.fd(3)
        if ar1 == 1: #블럭 첫라인 배치 및 반사
            if t1.xcor() >= b1_1.xcor()-11 and t1.xcor() <= b1_1.xcor()+11 and t1.ycor() >= b1_1.ycor()-11 and t1.ycor() <= b1_1.ycor()+11:
                if t1.ycor() <= b1_1.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar1 = 0
                    b1_1.ht()
                    b1_1.goto(-275,300)
                    point_up()

                if t1.xcor() >= b1_1.xcor() and t1.ycor() <= b1_1.ycor()+9 and t1.ycor() >= b1_1.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar1 = 0
                    b1_1.ht()
                    b1_1.goto(-275,300)
                    point_up()

                if t1.xcor() <= b1_1.xcor() and t1.ycor() <= b1_1.ycor()+9 and t1.ycor() >= b1_1.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar1 = 0
                    b1_1.ht()
                    b1_1.goto(-275,300)
                    point_up()

                if t1.ycor() >= b1_1.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar1 = 0
                    b1_1.ht()
                    b1_1.goto(-275,300)
                    point_up()
                    
        if ar2 == 1:
            if t1.xcor() >= b1_2.xcor()-11 and t1.xcor() <= b1_2.xcor()+11 and t1.ycor() >= b1_2.ycor()-11 and t1.ycor() <= b1_2.ycor()+11:
                if t1.ycor() <= b1_2.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar2 = 0
                    b1_2.ht()
                    b1_2.goto(-275,300)
                    point_up()

                if t1.xcor() >= b1_2.xcor() and t1.ycor() <= b1_2.ycor()+9 and t1.ycor() >= b1_2.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar2 = 0
                    b1_2.ht()
                    b1_2.goto(-275,300)
                    point_up()

                if t1.xcor() <= b1_2.xcor() and t1.ycor() <= b1_2.ycor()+9 and t1.ycor() >= b1_2.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar2 = 0
                    b1_2.ht()
                    b1_2.goto(-275,300)
                    point_up()

                if t1.ycor() >= b1_2.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar2 = 0
                    b1_2.ht()
                    b1_2.goto(-275,300)
                    point_up()
                    
        if ar3 == 1:
            if t1.xcor() >= b1_3.xcor()-11 and t1.xcor() <= b1_3.xcor()+11 and t1.ycor() >= b1_3.ycor()-11 and t1.ycor() <= b1_3.ycor()+11:
                if t1.ycor() <= b1_3.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar3 = 0
                    b1_3.ht()
                    b1_3.goto(-275,300)
                    point_up()

                if t1.xcor() >= b1_3.xcor() and t1.ycor() <= b1_3.ycor()+9 and t1.ycor() >= b1_3.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar3 = 0
                    b1_3.ht()
                    b1_3.goto(-275,300)
                    point_up()

                if t1.xcor() <= b1_3.xcor() and t1.ycor() <= b1_3.ycor()+9 and t1.ycor() >= b1_3.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar3 = 0
                    b1_3.ht()
                    b1_3.goto(-275,300)
                    point_up()

                if t1.ycor() >= b1_3.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar3 = 0
                    b1_3.ht()
                    b1_3.goto(-275,300)
                    point_up()

        if ar4 == 1:
            if t1.xcor() >= b1_4.xcor()-11 and t1.xcor() <= b1_4.xcor()+11 and t1.ycor() >= b1_4.ycor()-11 and t1.ycor() <= b1_4.ycor()+11:
                if t1.ycor() <= b1_4.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar4 = 0
                    b1_4.ht()
                    b1_4.goto(-275,300)
                    point_up()

                if t1.xcor() >= b1_4.xcor() and t1.ycor() <= b1_4.ycor()+9 and t1.ycor() >= b1_4.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar4 = 0
                    b1_4.ht()
                    b1_4.goto(-275,300)
                    point_up()

                if t1.xcor() <= b1_4.xcor() and t1.ycor() <= b1_4.ycor()+9 and t1.ycor() >= b1_4.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar4 = 0
                    b1_4.ht()
                    b1_4.goto(-275,300)
                    point_up()

                if t1.ycor() >= b1_4.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar4 = 0
                    b1_4.ht()
                    b1_4.goto(-275,300)
                    point_up()

        if ar5 == 1:
            if t1.xcor() >= b1_5.xcor()-11 and t1.xcor() <= b1_5.xcor()+11 and t1.ycor() >= b1_5.ycor()-11 and t1.ycor() <= b1_5.ycor()+11:
                if t1.ycor() <= b1_5.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar5 = 0
                    b1_5.ht()
                    b1_5.goto(-275,300)
                    point_up()

                if t1.xcor() >= b1_5.xcor() and t1.ycor() <= b1_5.ycor()+9 and t1.ycor() >= b1_5.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar5 = 0
                    b1_5.ht()
                    b1_5.goto(-275,300)
                    point_up()

                if t1.xcor() <= b1_5.xcor() and t1.ycor() <= b1_5.ycor()+9 and t1.ycor() >= b1_5.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar5 = 0
                    b1_5.ht()
                    b1_5.goto(-275,300)
                    point_up()

                if t1.ycor() >= b1_5.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar5 = 0
                    b1_5.ht()
                    b1_5.goto(-275,300)
                    point_up()

        if ar6 == 1:
            if t1.xcor() >= b2_1.xcor()-11 and t1.xcor() <= b2_1.xcor()+11 and t1.ycor() >= b2_1.ycor()-11 and t1.ycor() <= b2_1.ycor()+11:
                if t1.ycor() <= b2_1.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar6 = 0
                    b2_1.ht()
                    b2_1.goto(-225,300)
                    point_up()

                if t1.xcor() >= b2_1.xcor() and t1.ycor() <= b2_1.ycor()+9 and t1.ycor() >= b2_1.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar6 = 0
                    b2_1.ht()
                    b2_1.goto(-225,300)
                    point_up()

                if t1.xcor() <= b2_1.xcor() and t1.ycor() <= b2_1.ycor()+9 and t1.ycor() >= b2_1.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar6 = 0
                    b2_1.ht()
                    b2_1.goto(-225,300)
                    point_up()

                if t1.ycor() >= b2_1.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar6 = 0
                    b2_1.ht()
                    b2_1.goto(-225,300)
                    point_up()

        if ar7 == 1:
            if t1.xcor() >= b2_2.xcor()-11 and t1.xcor() <= b2_2.xcor()+11 and t1.ycor() >= b2_2.ycor()-11 and t1.ycor() <= b2_2.ycor()+11:
                if t1.ycor() <= b2_2.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar7 = 0
                    b2_2.ht()
                    b2_2.goto(-225,300)
                    point_up()

                if t1.xcor() >= b2_2.xcor() and t1.ycor() <= b2_2.ycor()+9 and t1.ycor() >= b2_2.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar7 = 0
                    b2_2.ht()
                    b2_2.goto(-225,300)
                    point_up()

                if t1.xcor() <= b2_2.xcor() and t1.ycor() <= b2_2.ycor()+9 and t1.ycor() >= b2_2.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar7 = 0
                    b2_2.ht()
                    b2_2.goto(-225,300)
                    point_up()

                if t1.ycor() >= b2_2.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar7 = 0
                    b2_2.ht()
                    b2_2.goto(-225,300)
                    point_up()

        if ar8 == 1:
            if t1.xcor() >= b2_3.xcor()-11 and t1.xcor() <= b2_3.xcor()+11 and t1.ycor() >= b2_3.ycor()-11 and t1.ycor() <= b2_3.ycor()+11:
                if t1.ycor() <= b2_3.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar8 = 0
                    b2_3.ht()
                    b2_3.goto(-225,300)
                    point_up()

                if t1.xcor() >= b2_3.xcor() and t1.ycor() <= b2_3.ycor()+9 and t1.ycor() >= b2_3.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar8 = 0
                    b2_3.ht()
                    b2_3.goto(-225,300)
                    point_up()

                if t1.xcor() <= b2_3.xcor() and t1.ycor() <= b2_3.ycor()+9 and t1.ycor() >= b2_3.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar8 = 0
                    b2_3.ht()
                    b2_3.goto(-225,300)
                    point_up()

                if t1.ycor() >= b2_3.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar8 = 0
                    b2_3.ht()
                    b2_3.goto(-225,300)
                    point_up()

        if ar9 == 1:
            if t1.xcor() >= b2_4.xcor()-11 and t1.xcor() <= b2_4.xcor()+11 and t1.ycor() >= b2_4.ycor()-11 and t1.ycor() <= b2_4.ycor()+11:
                if t1.ycor() <= b2_4.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar9 = 0
                    b2_4.ht()
                    b2_4.goto(-225,300)
                    point_up()

                if t1.xcor() >= b2_4.xcor() and t1.ycor() <= b2_4.ycor()+9 and t1.ycor() >= b2_4.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar9 = 0
                    b2_4.ht()
                    b2_4.goto(-225,300)
                    point_up()

                if t1.xcor() <= b2_4.xcor() and t1.ycor() <= b2_4.ycor()+9 and t1.ycor() >= b2_4.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar9 = 0
                    b2_4.ht()
                    b2_4.goto(-225,300)
                    point_up()

                if t1.ycor() >= b2_4.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar9 = 0
                    b2_4.ht()
                    b2_4.goto(-225,300)
                    point_up()

        if ar10 == 1:
            if t1.xcor() >= b2_5.xcor()-11 and t1.xcor() <= b2_5.xcor()+11 and t1.ycor() >= b2_5.ycor()-11 and t1.ycor() <= b2_5.ycor()+11:
                if t1.ycor() <= b2_5.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar10 = 0
                    b2_5.ht()
                    b2_5.goto(-225,300)
                    point_up()

                if t1.xcor() >= b2_5.xcor() and t1.ycor() <= b2_5.ycor()+9 and t1.ycor() >= b2_5.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar10 = 0
                    b2_5.ht()
                    b2_5.goto(-225,300)
                    point_up()

                if t1.xcor() <= b2_5.xcor() and t1.ycor() <= b2_5.ycor()+9 and t1.ycor() >= b2_5.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar10 = 0
                    b2_5.ht()
                    b2_5.goto(-225,300)
                    point_up()

                if t1.ycor() >= b2_5.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar10 = 0
                    b2_5.ht()
                    b2_5.goto(-225,300)
                    point_up()

        if ar11 == 1:
            if t1.xcor() >= b3_1.xcor()-11 and t1.xcor() <= b3_1.xcor()+11 and t1.ycor() >= b3_1.ycor()-11 and t1.ycor() <= b3_1.ycor()+11:
                if t1.ycor() <= b3_1.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar11 = 0
                    b3_1.ht()
                    b3_1.goto(-225,300)
                    point_up()

                if t1.xcor() >= b3_1.xcor() and t1.ycor() <= b3_1.ycor()+9 and t1.ycor() >= b3_1.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar11 = 0
                    b3_1.ht()
                    b3_1.goto(-225,300)
                    point_up()

                if t1.xcor() <= b3_1.xcor() and t1.ycor() <= b3_1.ycor()+9 and t1.ycor() >= b3_1.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar11 = 0
                    b3_1.ht()
                    b3_1.goto(-225,300)
                    point_up()

                if t1.ycor() >= b3_1.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar11 = 0
                    b3_1.ht()
                    b3_1.goto(-225,300)
                    point_up()

        if ar12 == 1:
            if t1.xcor() >= b3_2.xcor()-11 and t1.xcor() <= b3_2.xcor()+11 and t1.ycor() >= b3_2.ycor()-11 and t1.ycor() <= b3_2.ycor()+11:
                if t1.ycor() <= b3_2.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar12 = 0
                    b3_2.ht()
                    b3_2.goto(-225,300)
                    point_up()

                if t1.xcor() >= b3_2.xcor() and t1.ycor() <= b3_2.ycor()+9 and t1.ycor() >= b3_2.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar12 = 0
                    b3_2.ht()
                    b3_2.goto(-225,300)
                    point_up()

                if t1.xcor() <= b3_2.xcor() and t1.ycor() <= b3_2.ycor()+9 and t1.ycor() >= b3_2.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar12 = 0
                    b3_2.ht()
                    b3_2.goto(-225,300)
                    point_up()

                if t1.ycor() >= b3_2.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar12 = 0
                    b3_2.ht()
                    b3_2.goto(-225,300)
                    point_up()

        if ar13 == 1:
            if t1.xcor() >= b3_3.xcor()-11 and t1.xcor() <= b3_3.xcor()+11 and t1.ycor() >= b3_3.ycor()-11 and t1.ycor() <= b3_3.ycor()+11:
                if t1.ycor() <= b3_3.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar13 = 0
                    b3_3.ht()
                    b3_3.goto(-225,300)
                    point_up()

                if t1.xcor() >= b3_3.xcor() and t1.ycor() <= b3_3.ycor()+9 and t1.ycor() >= b3_3.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar13 = 0
                    b3_3.ht()
                    b3_3.goto(-225,300)
                    point_up()

                if t1.xcor() <= b3_3.xcor() and t1.ycor() <= b3_3.ycor()+9 and t1.ycor() >= b3_3.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar13 = 0
                    b3_3.ht()
                    b3_3.goto(-225,300)
                    point_up()

                if t1.ycor() >= b3_3.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar13 = 0
                    b3_3.ht()
                    b3_3.goto(-225,300)
                    point_up()

        if ar14 == 1:
            if t1.xcor() >= b3_4.xcor()-11 and t1.xcor() <= b3_4.xcor()+11 and t1.ycor() >= b3_4.ycor()-11 and t1.ycor() <= b3_4.ycor()+11:
                if t1.ycor() <= b3_4.ycor()-9 :
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar14 = 0
                    b3_4.ht()
                    b3_4.goto(-225,300)
                    point_up()

                if t1.xcor() >= b3_4.xcor() and t1.ycor() <= b3_4.ycor()+9 and t1.ycor() >= b3_4.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar14 = 0
                    b3_4.ht()
                    b3_4.goto(-225,300)
                    point_up()

                if t1.xcor() <= b3_4.xcor() and t1.ycor() <= b3_4.ycor()+9 and t1.ycor() >= b3_4.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar14 = 0
                    b3_4.ht()
                    b3_4.goto(-225,300)
                    point_up()

                if t1.ycor() >= b3_4.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar14 = 0
                    b3_4.ht()
                    b3_4.goto(-225,300)
                    point_up()

        if ar15 == 1:
            if t1.xcor() >= b3_5.xcor()-11 and t1.xcor() <= b3_5.xcor()+11 and t1.ycor() >= b3_5.ycor()-11 and t1.ycor() <= b3_5.ycor()+11:
                if t1.ycor() <= b3_5.ycor()-9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar15 = 0
                    b3_5.ht()
                    b3_5.goto(-225,300)
                    point_up()

                if t1.xcor() >= b3_5.xcor() and t1.ycor() <= b3_5.ycor()+9 and t1.ycor() >= b3_5.ycor()-9:
                    if r <= 180:
                        t1.rt((r-90)*2)
                        r = r - 2*(r-90)
                    else:
                        t1.lt((270-r)*2)
                        r = r + 2*(270-r)
                    ar15 = 0
                    b3_5.ht()
                    b3_5.goto(-225,300)
                    point_up()

                if t1.xcor() <= b3_5.xcor() and t1.ycor() <= b3_5.ycor()+9 and t1.ycor() >= b3_5.ycor()-9:
                    if r <= 180:
                        t1.lt((90-r)*2)
                        r = r + 2*(90-r)
                    else:
                        t1.rt((r-270)*2)
                        r = r - (r-270)*2
                    ar15 = 0
                    b3_5.ht()
                    b3_5.goto(-225,300)
                    point_up()

                if t1.ycor() >= b3_5.ycor()+9:
                    if r <= 180 and r >= 90:
                        t1.lt(2*(180-r))
                        r = r + 2*(180-r)
                    else:
                        t1.rt(2*r)
                        r = 360-r
                    ar15 = 0
                    b3_5.ht()
                    b3_5.goto(-225,300)
                    point_up()


            
        if t1.xcor() >= -302 and t1.xcor() <= -297:
            if r <= 180:
                t1.rt((r-90)*2)
                r = r - 2*(r-90)
            else:
                t1.lt((270-r)*2)
                r = r + 2*(270-r)


        elif t1.xcor() >= -153 and t1.xcor() <= -148:
            if r <= 180:
                t1.lt((90-r)*2)
                r = r + 2*(90-r)

            else:
                t1.rt((r-270)*2)
                r = r - (r-270)*2
                
        elif t1.ycor() >= 300:
            if r <= 180 and r >= 90:
                t1.lt(2*(180-r))
                r = r + 2*(180-r)
            else:
                t1.rt(2*r)
                r = 360-r
            

        elif t1.ycor() <= 3 :
            break
#턴 진행 
    reset()
    if point <= 99:
        box()
        
    elif point >= 100 and point <= 399:
        G = random.randint(0,100)
        if G <= 39:
            box()
        if G >= 40 and G <= 96:
            for i in range(2):
                box()
        if G >= 97:
            for i in range(3):
                box()

    elif point >= 400:
        G = random.randint(0,100)
        if G <=80:
            for i in range(2):
                box()
        if G >= 90:
            for i in range(3):
                box()


    #데스라인 판별 및 최고점수 설정
    if b1_1.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b1_2.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b1_3.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b1_4.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b1_5.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b2_1.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b2_2.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b2_3.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b2_4.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b2_5.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b3_1.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b3_2.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b3_3.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b3_4.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))

    if b3_5.ycor() <= 50:
        pen.undo()
        pen.goto(200,230)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.rt(90)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
        pen.end_fill()
        if point >= bestpoint:
            pen.write(point, font=("Arial",15, "normal"))
            bestpoint = point
        if point <= bestpoint:
            pen.write(bestpoint, font=("Arial",15, "normal"))
        pen.goto(100,170)
        pen.write("game over!! 다시시작은 R키", font=("Arial",15, "normal"))
        
#################배치함수##########################
def box():
    global ar1
    global ar2
    global ar3
    global ar4
    global ar5
    global ar6
    global ar7
    global ar8
    global ar9
    global ar10
    global ar11
    global ar12
    global ar13
    global ar14
    global ar15

    line1 = random.randint(1,2)
    line2 = random.randint(1,2)
    line3 = random.randint(1,2)

    if line1 == 1:
        if ar1 == 1:
            b1_1.goto(-280,b1_1.ycor()-25)
            if ar2 == 1:
                b1_2.goto(-280, b1_2.ycor()-25)
                if ar3 == 1:
                    b1_3.goto(-280, b1_3.ycor()-25)
                    if ar4 == 1:
                        b1_4.goto(-280, b1_4.ycor()-25)
                        b1_5.goto(-280,b1_5.ycor()-25)
                        b1_5.st()
                        ar5 = 1
                    else:
                        b1_4.goto(-280, b1_4.ycor()-25)
                        b1_4.st()
                        ar4 = 1
                else:
                    b1_3.goto(-280, b1_3.ycor()-25)
                    b1_3.st()
                    ar3 = 1
            else:
                b1_2.goto(-280, b1_2.ycor()-25)
                b1_2.st()
                ar2 = 1
        else:
            b1_1.goto(-280, b1_1.ycor()-25)
            b1_1.st()
            ar1 = 1

    if line1 == 2:
        if ar1 == 1:
            b1_1.goto(-265,b1_1.ycor()-25)
            if ar2 == 1:
                b1_2.goto(-265, b1_2.ycor()-25)
                if ar3 == 1:
                    b1_3.goto(-265, b1_3.ycor()-25)
                    if ar4 == 1:
                        b1_4.goto(-265, b1_4.ycor()-25)
                        b1_5.goto(-265,b1_5.ycor()-25)
                        b1_5.st()
                        ar5 = 1
                    else:
                        b1_4.goto(-265, b1_4.ycor()-25)
                        b1_4.st()
                        ar4 = 1
                else:
                    b1_3.goto(-265, b1_3.ycor()-25)
                    b1_3.st()
                    ar3 = 1
            else:
                b1_2.goto(-265, b1_2.ycor()-25)
                b1_2.st()
                ar2 = 1
        else:
            b1_1.goto(-265, b1_1.ycor()-25)
            b1_1.st()
            ar1 = 1

    if line2 == 1:
        if ar6 == 1:
            b2_1.goto(-240,b2_1.ycor()-25)
            if ar7 == 1:
                b2_2.goto(-240, b2_2.ycor()-25)
                if ar8 == 1:
                    b2_3.goto(-240, b2_3.ycor()-25)
                    if ar9 == 1:
                        b2_4.goto(-240, b2_4.ycor()-25)
                        b2_5.goto(-240,b2_5.ycor()-25)
                        b2_5.st()
                        ar10 = 1
                    else:
                        b2_4.goto(-240, b2_4.ycor()-25)
                        b2_4.st()
                        ar9 = 1
                else:
                    b2_3.goto(-240, b2_3.ycor()-25)
                    b2_3.st()
                    ar8 = 1
            else:
                b2_2.goto(-240, b2_2.ycor()-25)
                b2_2.st()
                ar7 = 1
        else:
            b2_1.goto(-240, b2_1.ycor()-25)
            b2_1.st()
            ar6 = 1

    if line2 == 2:
        if ar6 == 1:
            b2_1.goto(-215,b2_1.ycor()-25)
            if ar7 == 1:
                b2_2.goto(-215, b2_2.ycor()-25)
                if ar8 == 1:
                    b2_3.goto(-215, b2_3.ycor()-25)
                    if ar9 == 1:
                        b2_4.goto(-215, b2_4.ycor()-25)
                        b2_5.goto(-215, b2_5.ycor()-25)
                        b2_5.st()
                        ar10 = 1
                    else:
                        b2_4.goto(-215, b2_4.ycor()-25)
                        b2_4.st()
                        ar9 = 1
                else:
                    b2_3.goto(-215, b2_3.ycor()-25)
                    b2_3.st()
                    ar8 = 1
            else:
                b2_2.goto(-215, b2_2.ycor()-25)
                b2_2.st()
                ar7 = 1
        else:
            b2_1.goto(-215, b2_1.ycor()-25)
            b2_1.st()
            ar6 = 1
            
    if line3 == 1:
        if ar11 == 1:
            b3_1.goto(-190,b3_1.ycor()-25)
            if ar12 == 1:
                b3_2.goto(-190, b3_2.ycor()-25)
                if ar13 == 1:
                    b3_3.goto(-190, b3_3.ycor()-25)
                    if ar14 == 1:
                        b3_4.goto(-190, b3_4.ycor()-25)
                        b3_5.goto(-190,b3_5.ycor()-25)
                        b3_5.st()
                        ar15 = 1
                    else:
                        b3_4.goto(-190, b3_4.ycor()-25)
                        b3_4.st()
                        ar14 = 1
                else:
                    b3_3.goto(-190, b3_3.ycor()-25)
                    b3_3.st()
                    ar13 = 1
            else:
                b3_2.goto(-190, b3_2.ycor()-25)
                b3_2.st()
                ar12 = 1
        else:
            b3_1.goto(-190, b3_1.ycor()-25)
            b3_1.st()
            ar11 = 1


    if line3 == 2:
        if ar11 == 1:
            b3_1.goto(-170, b3_1.ycor()-25)
            if ar12 == 1:
                b3_2.goto(-170, b3_2.ycor()-25)
                if ar13 == 1:
                    b3_3.goto(-170, b3_3.ycor()-25)
                    if ar14 == 1:
                        b3_4.goto(-170, b3_4.ycor()-25)
                        b3_5.goto(-170,b3_5.ycor()-25)
                        b3_5.st()
                        ar15 = 1
                    else:
                        b3_4.goto(-170, b3_4.ycor()-25)
                        b3_4.st()
                        ar14 = 1
                else:
                    b3_3.goto(-170, b3_3.ycor()-25)
                    b3_3.st()
                    ar13 = 1
            else:
                b3_2.goto(-170, b3_2.ycor()-25)
                b3_2.st()
                ar12 = 1
        else:
            b3_1.goto(-170, b3_1.ycor()-25)
            b3_1.st()
            ar11 = 1

################맵##################### 

#플레이 판
t1.up()
t1.rt(180)
t1.fd(300)
t1.down()
t1.pensize(3)
t1.fillcolor("yellow")
t1.begin_fill()
for i in range(2):
     t1.rt(90)
     t1.fd(300)
     t1.rt(90)
     t1.fd(150)
t1.end_fill()
t1.pensize(1)
t1.rt(180)
t1.fd(50)
t1.rt(90)
t1.fillcolor("red")
t1.begin_fill()
t1.circle(25)
t1.end_fill()
t1.color("black")
t1.rt(270)
t1.up()
t1.fd(25)
t1.seth(90)
t1.shape("circle")
t1.stamp()
t1.shape("classic")
t1.up()
t1.goto(-150,50)
t1.write("  death line ", font=("Arial",10, "normal"))
t1.down()
t1.goto(-300,50)
t1.up()
t1.goto(-200,0)

#세부 작업


point = 0
pen.ht()
pen.lt(90)
pen.up()
pen.bk(200)
pen.penup()
pen.lt(90)
pen.fd(290)
pen.write("LINE WAR: ALLOW ", font=("Arial",50, "normal"))
pen.goto(100,200)
pen.write("현재 점수:", font=("Arial",15, "normal"))
pen.goto(100,230)
pen.write("최고 점수:", font=("Arial",15, "normal"))

#설명서
pen.goto(100,115)
pen.write("########################", font=("Arial",13, "normal"))
pen.goto(100,85)
pen.write("*화살 각도 조절키: 조작키 좌,우", font=("Arial",13, "normal"))
pen.goto(100,70)
pen.write("*화살 발사키: 조작키 상", font=("Arial",13, "normal"))
pen.goto(100,55)
pen.write("*화살 돌아오기키: 조작키 하", font=("Arial",13, "normal"))
pen.goto(100,40)
pen.write("*다시 시작하기: R키", font=("Arial",13, "normal"))
pen.goto(100,10)
pen.write("########################", font=("Arial",13, "normal"))
pen.goto(200,200)
pen.write(point, font=("Arial",15, "normal"))


b1_1.goto(-280, b1_1.ycor()-20)
b1_1.st()
ar1 = 1

b2_1.goto(-215, b2_1.ycor()-20)
b2_1.st()
ar6 = 1

b3_1.goto(-180, b3_1.ycor()-20)
b3_1.st()
ar11 = 1



screen.onkeypress(leftkey, "Right")
screen.onkeypress(rightkey, "Left")
screen.onkeypress(go, "Up")
screen.onkeypress(reset, "Down")
screen.onkeypress(replay, "r")

screen.listen()
