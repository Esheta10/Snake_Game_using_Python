import turtle
import time
import random
delay = 0.1

#score
score=0
high_score=0
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score:0 high score:0",align="center",font=("Courier",24,"normal"))

#set up the screen
wn=turtle.Screen()
wn.title("Snake game")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)#turns off the animation on screen/screen updates

#snake head
head=turtle.Turtle()
head.speed(0)#animation speed of turtle module
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)#to be on center of the screen
head.direction="stop"#when it starts,its gonna sit there in the middle

#snake food
food=turtle.Turtle()
food.speed(0)#animation speed of turtle module
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


#functions
def go_up():
    if head.direction !="down":
        head.direction = "up"
def go_down():
    if head.direction !="up":
        head.direction = "down"
def go_left():
    if head.direction !="right":
        head.direction="left"
def go_right():
    if head.direction !="left":
        head.direction="right"
def move():
    if head.direction=="up":
        y = head.ycor()
        head.sety(y+20)#moves up by 20 co-ordinates each time
    if head.direction=="down":
        y = head.ycor()
        head.sety(y-20)#moves down by 20 co-ordinates each time    
    if head.direction=="left":
        x = head.xcor()
        head.setx(x-20)#moves left by 20 co-ordinates each time
    if head.direction=="right":
        x = head.xcor()
        head.setx(x+20)#moves right by 20 co-ordinates each time

#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

segments = []

#main game loop
while True:
    wn.update()#everytime through this loop,it updates the screen
    #check for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction= "stop"

        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)
        #clear the segments list
        segments.clear()
        #reset score
        score=0
        #reset the delay
        delay=0.1
        #update the score display
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal")),
        
    #check for collison with food
    if head.distance(food) < 20:
        #move the food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)#animation speed
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #shorten time delay
        delay -= 0.001

        #increase the score
        score += 10

        if score > high_score:
            high_score=score
            
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal")),
        

       # Move the end segments first in reverse order
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    for index in range(len(segments)-1, 0, -1):
         x = segments[index-1].xcor()
         y = segments[index-1].ycor()
         segments[index].goto(x, y)
    move()
    #check for head collision with body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            
            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)
                
            #clear the segments list
            segments.clear()
            #reset score
            score=0
            #reset the delay
            delay=0.1
            #update the score display
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal")),
    time.sleep(delay)
wn.mainloop()

