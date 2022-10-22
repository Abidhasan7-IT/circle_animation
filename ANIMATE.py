from turtle import *
bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
   color('green')
   circle(i)
   color('red')
   circle(i*0.6)
   right(10)
   forward(10)
done()
