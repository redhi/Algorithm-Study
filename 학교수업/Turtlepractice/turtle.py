import turtle
import random

num1 = random.randint(1,13)
num2 = random.randint(1,13)

win = turtle.Screen()
t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.penup()
t2.penup()

win.addshape("ace_of_spades.gif")
win.addshape("2_of_spades.gif")
win.addshape("3_of_spades.gif")
win.addshape("4_of_spades.gif")
win.addshape("5_of_spades.gif")
win.addshape("6_of_spades.gif")
win.addshape("7_of_spades.gif")
win.addshape("8_of_spades.gif")
win.addshape("9_of_spades.gif")
win.addshape("10_of_spades.gif")
win.addshape("jack_of_spades.gif")
win.addshape("queen_of_spades.gif")
win.addshape("king_of_spades.gif")

if(num1==1):
    t1.shape("ace_of_spades.gif")
    t1.fd(-140)
if(num1==2):
    t1.shape("2_of_spades.gif")
    t1.fd(-140)
if(num1==3):
    t1.shape("3_of_spades.gif")
    t1.fd(-140)
if(num1==4):
    t1.shape("4_of_spades.gif")
    t1.fd(-140)
if(num1==5):
    t1.shape("5_of_spades.gif")
    t1.fd(-140)
if(num1==6):
    t1.shape("6_of_spades.gif")
    t1.fd(-140)
if(num1==7):
    t1.shape("7_of_spades.gif")
    t1.fd(-140)
if(num1==8):
    t1.shape("8_of_spades.gif")
    t1.fd(-140)
if(num1==9):
    t1.shape("9_of_spades.gif")
    t1.fd(-140)
if(num1==10):
    t1.shape("10_of_spades.gif")
    t1.fd(-140)
if(num1==11):
    t1.shape("jack_of_spades.gif")
    t1.fd(-140)
if(num1==12):
    t1.shape("queen_of_spades.gif")
    t1.fd(-140)
if(num1==13):
    t1.shape("king_of_spades.gif")
    t1.fd(-140)
    
if(num2==1):
    t2.shape("ace_of_spades.gif")
    t2.fd(140)
if(num2==2):
    t2.shape("2_of_spades.gif")
    t2.fd(140)
if(num2==3):
    t2.shape("3_of_spades.gif")
    t2.fd(140)
if(num2==4):
    t2.shape("4_of_spades.gif")
    t2.fd(140)
if(num2==5):
    t2.shape("5_of_spades.gif")
    t2.fd(140)
if(num2==6):
    t2.shape("6_of_spades.gif")
    t2.fd(140)
if(num2==7):
    t2.shape("7_of_spades.gif")
    t2.fd(140)
if(num2==8):
    t2.shape("8_of_spades.gif")
    t2.fd(140)
if(num2==9):
    t2.shape("9_of_spades.gif")
    t2.fd(140)
if(num2==10):
    t2.shape("10_of_spades.gif")
    t2.fd(140)
if(num2==11):
    t2.shape("jack_of_spades.gif")
    t2.fd(140)
if(num2==12):
    t2.shape("queen_of_spades.gif")
    t2.fd(140)
if(num2==13):
    t2.shape("king_of_spades.gif")
    t2.fd(140)

if(num1>num2):
    print("왼쪽 번호가 더 높습니다.")
if(num1<num2):
    print("오른쪽 번호가 더 높습니다.")
if(num1==num2):
    print("두 번호가 같습니다.")
