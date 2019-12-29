import turtle
from tkinter import *

window = Tk()
window.title("안내판")
####################ball 중력 알고리즘

    
####################pen 이동 함수


def go():
    pen.fd(10)

def right():
    global angle
    pen.rt(30)
    angle = angle + 1

def left():
    global angle
    pen.lt(30)
    angle = angle - 1
####################pen 집가는 함수
def go_home():
    pen.goto(0,0)
####################pen 그림 함수
def drawline():
    global real_length
    global ingk
    if ingk - real_length >= 0:
        pen.pendown()
        pen.color("black")
        pen.fd(real_length)
        pen.bk(real_length * 2)
        pen.fd(real_length)
        pen.penup()
        ingk = ingk - real_length
        nope = Label(window, text=(">>방금 잉크를",real_length,"만큼 써서 잉크가",ingk,"만큼 남았습니다."))
        nope.grid(row = 2, column = 0)
    else:
        nope = Label(window, text="           >>잉크가 모자랍니다. 길이를 조절해보세요.              ")
        nope.grid(row = 2, column = 0)
        
    
####################Mpen 그림 함수

def make_map():####################아주 중요한 Mpen의 맵 처리 함수
    if start == "설명":
        Mpen.up()
        Mpen.goto(-370,200)
        Mpen.write("#공을 구멍에 안전하게 넣기 위해 펜을 이용해 길을 그리세요.", font=("Arial",20, "normal"))
        Mpen.goto(-370,100)
        Mpen.write("#길을 다 만들면 키보드에서 Z키를 누르세요.", font=("Arial",20, "normal"))
        Mpen.goto(-370,0)
        Mpen.write("#길의 길이는 '길이조절' 버튼을 눌러 원하는 길이를 입력하세요.", font=("Arial",20, "normal"))
        Mpen.goto(-370,-100)
        Mpen.write("#공이 빨간색에 닿으면 리셋되니 조심하세요.", font=("Arial",20, "normal"))
        Mpen.goto(300,-250)
        Mpen.write("시작", font=("Arial",30, "normal"))
        Mpen.pencolor("black")
        Mpen.down()
        for i in range(2):
            Mpen.fd(80)
            Mpen.lt(90)
            Mpen.fd(50)
            Mpen.lt(90)
        
    if start == "맵1_1":
        global real_length
        global ingk
        real_length = 10
        ingk = 50
        #맵 세팅
        Mpen.goto(-350,200)

        #버튼
        Mpen.goto(230,-350)
        Mpen.write("길이 조절", font=("Arial",30, "normal"))
        Mpen.down()
        for i in range(2):
            Mpen.fd(170)
            Mpen.lt(90)
            Mpen.fd(50)
            Mpen.lt(90)
        Mpen.up()
        Mpen.goto(140,-350)
        Mpen.write("리셋", font=("Arial",30, "normal"))
        Mpen.down()
        for i in range(2):
            Mpen.fd(80)
            Mpen.lt(90)
            Mpen.fd(50)
            Mpen.lt(90)
        Mpen.up()
        ball.shape("circle")
        ball.goto(-300,200)
        ball.st()
        pen.goto(0,0)
        nope = Label(window, text="맵1_1, 주어진 잉크 : 50")
        nope.grid(row = 0, column = 0)
        nope = Label(window, text="기본 설정 잉크값 : 10")
        nope.grid(row = 1, column = 0)
        pen.st()

        
        

def eraser_map():
    Mpen.up()
    Mpen.goto(-400,-300)
    Mpen.down()
    Mpen.setheading(0)
    Mpen.pencolor("red")
    Mpen.width(5)
    Mpen.fillcolor("white")
    Mpen.begin_fill()
    for i in range(2):
        Mpen.fd(800)
        Mpen.lt(90)
        Mpen.fd(600)
        Mpen.lt(90)
    Mpen.end_fill()
    Mpen.up()
    Mpen.pencolor("black")
    Mpen.width(1)
####################click 함수

def click_begin(x,y):
    click.goto(x,y)
    click_next()


def click_next():
    global start
    global length
    global ingk
    global real_length
    if start == "시작" and click.xcor() >= -50 and click.xcor() <= 30 and click.ycor() >= 0 and click.ycor() <= 50:
        start = "설명"
        nope = Label(window, text="시작, 절대 이 창을 끄지 마시오.")
        nope.grid(row = 0, column = 0)
        eraser_map()
        make_map()

    if start == "설명" and click.xcor() >= 300 and click.xcor() <= 380 and click.ycor() >= -250 and click.ycor() <= -200:
        start = "맵1_1"
        eraser_map()
        make_map()

    if start == "맵1_1" and click.xcor() >= 230 and click.xcor() <= 400 and click.ycor() >= -350 and click.ycor() <= -300:
        length = int(turtle.textinput("","길이를 입력하시오(5단위로 입력):"))
        if length <= ingk:
            real_length = length
            nope = Label(window, text=("                >>가능합니다. 남은 잉크:",ingk, "                  "))
            nope.grid(row = 2, column = 0)
        else:
            nope = Label(window, text="                        >>잉크가 부족합니다                           ")
            nope.grid(row = 2, column = 0)

    if start == "맵1_1" and click.xcor() >= 140 and click.xcor() <= 220 and click.ycor() >= -350 and click.ycor() <= -300:
        eraser_map()
        make_map()
        ball.st()
        pen.st()
        pen.setheading(0)
        nope = Label(window, text="          >>리셋되었습니다. 잉크가 충전되었습니다.             ")
        nope.grid(row = 2, column = 0)
        
    
####################시작화면
start = "시작"
pen = turtle.Turtle()
Mpen = turtle.Turtle()
click = turtle.Turtle()
ball = turtle.Turtle()

Mpen.speed(10)
click.speed(10)

pen.width(2)

Mpen.up()
click.up()
ball.up()
pen.up()

pen.goto(0,0)
pen.setheading(0)
angle = 0

pen.ht()
click.ht()
ball.ht()

#시작버튼
Mpen.goto(-50,0)
Mpen.write("시작", font=("Arial",30, "normal"))
Mpen.down()
for i in range(2):
    Mpen.fd(80)
    Mpen.lt(90)
    Mpen.fd(50)
    Mpen.lt(90)

#클릭하기
screen = Mpen.getscreen()
screen.onscreenclick(click_begin)
#화살표 움직이기
screen1 = pen.getscreen()
screen1.onkeypress(go, "Up")
screen1.onkeypress(right, "Right")
screen1.onkeypress(left, "Left")
screen1.onkeypress(drawline, "space")
screen1.onkeypress(go_home, "Down")

screen1.listen()
screen.listen()




####################메모

# 맵에서 Tk공지는 row 0,1
# 상황 메세지는 row 2,3

