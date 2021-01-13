#snake game
#--------------------------<>-----------------------
#head -1
  #move up, down, left and right
  #moves at a normal pace- not fast or too slow 
#food - 2
  #food is moving everytime the snake eats it-random position
#snake body-3
  #increase the snake when it eats food
#score - 4
  #how much food you eat
  #how long the snake gets
#screen - 5
  #boundaries-border
  #screen color
  #play the game opens screen

import random
import turtle
import time
#library we will use

#we need a function to move the snake
def move():
    if head.direction == "up":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y + 20)#to go up, increase y axis
 
    if head.direction == "down":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y - 20)#to go down, decrease y axis
 
    if head.direction == "right":
        x = head.xcor() #y coordinate of the turtle
        head.setx(x + 20)#to go right, increase x axis
 
    if head.direction == "left":
        x = head.xcor() #y coordinate of the turtle
        head.setx(x - 20)#to go left, decrease x axis

def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"

#we need to create the food that the snake eats which is also a turtle
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(1.00, 1.00)
food.goto(0, 0)

#opens a new window
snakelist = [0]
delay = 0.1
window = turtle.Screen()
window.title("kolade's snake game") #title of your game's window
window.bgcolor("blue") #the window background color
window.setup(width=600,height=600)#width and height of your window
window.tracer(0) #turns off screen updates since background is the same 
window.listen()
window.onkey(go_up, "w")
window.onkey(go_down, "s")
window.onkey(go_right, "d")
window.onkey(go_left, "a")


#creating the head of the turtle
head= turtle.Turtle()
head.speed(0)#zero because we are just starting the game
head.shape("square")
head.color("black")
head.penup() #allows the snake to move without drawing anything
head.goto(0, 100) #starting position
head.direction = "stop" #allows the snake to stay in its goto position

segments = []
# Check for collision with
if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
  time.sleep(1)
  head.goto(0, 0)
  head.direction = "stop"

#add turtle score
#pen = turtle.Turtle()
#pen.speed(0)
#pen.shape("square")
#pen.color("white")
#pen.penup()
#pen.hideturtle()
#pen.goto(0, 260)
#pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))



def mainloop():
  global segments
  global delay
  while True:
      window.update()

      if head.distance(food) <  20: #the head of the snake and food touch
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
      
        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)


        #increase the snake speed
        delay -= 0.002
        #move the end segments first
        #goes from len of segments to 0 and decreases by one each time
      for index in range(len(segments)-1, 0, -1):
        #this statement moves the current turtle to the coordinates of the previous turtle
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
      

      #move segment zero to where the head is
      if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

      # Check for collision with walls
      if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        #reset snakes speed after it dies
        delay = 0.1
        print("GAME OVER")

        # Hide the segments when your snake dies
        for segment in segments:
           segment.goto(1000, 1000)
 
        # clear segment list
        segments = [] 
      #function call in loop so the snake can move
      move()

      # Check for head collision with the rest of the segments
      for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            delay = 0.1

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            # clear segment list
            segments = [] 

      #slow down the speed of the game
      time.sleep(delay)

mainloop()