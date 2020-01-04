import random
from tkinter import *
window = Tk()
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0


#리셋함수

def reset():
        l1['text'] = '       '
        global n1
        n1 = 0
        l2['text'] = '       '
        global n2
        n2 = 0
        l3['text'] = '       '
        global n3
        n3 = 0
        l4['text'] = '       '
        global n4
        n4 = 0
        l5['text'] = '       '
        global n5
        n5 = 0
        l6['text'] = '       '
        global n6
        n6 = 0
        l7['text'] = '       '
        global n7
        n7 = 0
        l8['text'] = '       '
        global n8
        n8 = 0
        l9['text'] = '       '
        global n9
        n9 = 0
        l11['text'] = ' '

#버튼 함수
def a1():
        global n1
        if n1 == 0:
                l1['text'] = '  O   '
                n1 = 1
def a2():
        global n2
        if n2 == 0:
                l2['text'] = '  O   '
                n2 = 1
def a3():
        global n3
        if n3 == 0:
                l3['text'] = '  O   '
                n3 = 1
def a4():
        global n4
        if n4 == 0:
                l4['text'] = '  O   '
                n4 = 1
def a5():
        global n5
        if n5 == 0:
                l5['text'] = '  O   '
                n5 = 1
def a6():
        global n6
        if n6 == 0:
                l6['text'] = '  O   '
                n6 = 1
def a7():
        global n7
        if n7 == 0:
                l7['text'] = '  O   '
                n7 = 1
def a8():
        global n8
        if n8 == 0:
                l8['text'] = '  O   '
                n8 = 1
def a9():
        global n9
        if n9 == 0:
                l9['text'] = '  O   '
                n9 = 1

#인공지능 함수
def AI():
        x = random.randint(1,9)
        global n1
        global n2
        global n3
        global n4
        global n5
        global n6
        global n7
        global n8
        global n9
        
        if x == 1:
                if n1 == 0:
                        l1['text'] = '   X  '
                        n1 = 2
        elif x == 2:
                if n2 == 0:
                        l2['text'] = '   X  '
                        n2 = 2
        elif x == 3:
                if n3 == 0:
                        l3['text'] = '   X  '
                        n3 = 2
        elif x == 4:
                if n4 == 0:
                        l4['text'] = '   X  '
                        n4 = 2
        elif x == 5:
                if n5 == 0:
                        l5['text'] = '   X  '
                        n5 = 2
        elif x == 6:
                if n6 == 0:
                        l6['text'] = '   X  '
                        n6 = 2
        elif x == 7:
                if n7 == 0:
                        l7['text'] = '   X  '
                        n7= 2
        elif x == 8:
                if n8 == 0:
                        l8['text'] = '   X  '
                        n8 = 2
        elif x == 9:
                if n9 == 0:
                        l9['text'] = '   X  '
                        n9 = 2

#결과 함수
def bam():
        if n1 ==1 and n2 ==1 and n3 == 1:
                l11['text'] = '승리'
        elif n4 ==1 and n5 ==1 and n6 == 1:
                l11['text'] = '승리'
        elif n7 ==1 and n8 ==1 and n9 == 1:
                l11['text'] = '승리'
        elif n1 ==1 and n4 ==1 and n7 == 1:
                l11['text'] = '승리'
        elif n2 ==1 and n2 ==1 and n8 == 1:
                l11['text'] = '승리'
        elif n3 ==1 and n6 ==1 and n9 == 1:
                l11['text'] = '승리'
        elif n1 ==1 and n5 ==1 and n9 == 1:
                l11['text'] = '승리'
        elif n3 ==1 and n5 ==1 and n7 == 1:
                l11['text'] = '승리'

        if n1 ==2 and n2 ==2 and n3 == 2:
                l11['text'] = '패배'
        elif n4 ==2 and n5 ==2 and n6 == 2:
                l11['text'] = '패배'
        elif n7 ==2 and n8 ==2 and n9 == 2:
                l11['text'] = '패배'
        elif n1 ==2 and n4 ==2 and n7 == 2:
                l11['text'] = '패배'
        elif n2 ==2 and n2 ==2 and n8 == 2:
                l11['text'] = '패배'
        elif n3 ==2 and n6 ==2 and n9 == 2:
                l11['text'] = '패배'
        elif n1 ==2 and n5 ==2 and n9 == 2:
                l11['text'] = '패배'
        elif n3 ==2 and n5 ==2 and n7 == 2:
                l11['text'] = '패배'
        
        

                


#버튼
b1 = Button(window, text = " 1 ", command=a1)
b2 = Button(window, text = " 2 ", command=a2)
b3 = Button(window, text = " 3 ", command=a3)
b4 = Button(window, text = " 4 ", command=a4)
b5 = Button(window, text = " 5 ", command=a5)
b6 = Button(window, text = " 6 ", command=a6)
b7 = Button(window, text = " 7 ", command=a7)
b8 = Button(window, text = " 8 ", command=a8)
b9 = Button(window, text = " 9 ", command=a9)
b10 = Button(window, text = "리셋", command = reset)
b11 = Button(window, text = "AI", command = AI)
b12 = Button(window, text = "R", command = bam)
b1.grid(row = 1, column = 0)
b2.grid(row = 1, column = 1)
b3.grid(row = 1, column = 2)
b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)
b7.grid(row = 3, column = 0)
b8.grid(row = 3, column = 1)
b9.grid(row = 3, column = 2)
b10.grid(row = 4, column = 3)
b11.grid(row = 4, column = 1)
b12.grid(row = 4, column = 0)

#라벨 
l1 = Label(window, text = '       ', bg = "yellow")
l2 = Label(window, text = '       ', bg = "skyblue")
l3 = Label(window, text = '       ', bg = "yellow")
l4 = Label(window, text = '       ', bg = "skyblue")
l5 = Label(window, text = '       ', bg = "yellow")
l6 = Label(window, text = '       ', bg = "skyblue")
l7 = Label(window, text = '       ', bg = "yellow")
l8 = Label(window, text = '       ', bg = "skyblue")
l9 = Label(window, text = '       ', bg = "yellow")
l10 = Label(window, text = '결과')
l11 = Label(window, text = '')
l1.grid(row = 1, column = 3)
l2.grid(row = 1, column = 4)
l3.grid(row = 1, column = 5)
l4.grid(row = 2, column = 3)
l5.grid(row = 2, column = 4)
l6.grid(row = 2, column = 5)
l7.grid(row = 3, column = 3)
l8.grid(row = 3, column = 4)
l9.grid(row = 3, column = 5)
l10.grid(row = 4, column = 4)
l11.grid(row = 4, column = 5)


