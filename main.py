import turtle
t=turtle.Turtle()
screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('lightblue')
t.clear()
t.speed(0)


#intro screen
t.penup()
t.goto(0, 150)
t.pendown()
t.write('My',font=("arial",30,"italic"),align="center")

t.penup()
t.goto(0, -150)
t.pendown()
t.write('Favorite Things',font=("arial",30,"italic"),align="center")

t.penup()
t.goto(0, -300)
t.pendown()
t.write('Press enter to continue',font=("arial",20,"italic"),align="center")

t.pensize(5)
t.penup()
t.goto(-200,200)
t.pencolor("yellow")
t.pendown()
t.fillcolor("cyan")
t.begin_fill()
t.circle(35)
t.end_fill()

t.penup()
t.goto(380, -230)
t.pendown()
screen.addshape("heart1.gif")
t.shape("heart1.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(200,200)
t.pendown()
screen.addshape("star.gif")
t.shape("star.gif")
t.stamp()
t.shape("classic")



round = input("Press Enter to Continue: ")

t.clear()
#screen 2

screen.bgcolor('pink')
t.pencolor("black")
t.penup()
t.goto(0, 200)
t.pendown()
t.write('Favorite Foods',font=("arial",30,"italic"),align="center")


t.penup()
t.goto(200,-100)
t.pendown()
screen.addshape("pizza1.gif")
t.shape("pizza1.gif")
t.stamp()
t.shape("classic")

t.pencolor("black")
t.penup()
t.goto(200, -200)
t.pendown()
t.write('Pizza',font=("arial",30,"italic"),align="center")

t.penup()
t.goto(0,100)
t.pendown()
screen.addshape("popcorn1.gif")
t.shape("popcorn1.gif")
t.stamp()
t.shape("classic")

t.pencolor("black")
t.penup()
t.goto(0, 0)
t.pendown()
t.write('Popcorn',font=("arial",30,"italic"),align="center")


t.penup()
t.goto(-200,-100)
t.pendown()
screen.addshape("fries4.gif")
t.shape("fries4.gif")
t.stamp()
t.shape("classic")


t.pencolor("black")
t.penup()
t.goto(-200, -250)
t.pendown()
t.write('French Fries',font=("arial",30,"italic"),align="center")



t.penup()
t.goto(-200,100)
t.fillcolor("red")
t.pendown()
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()

t.penup()
t.goto(0, -300)
t.pendown()
t.write('Press enter to continue',font=("arial",20,"italic"),align="center")

round = input("Press Enter to Continue: ")

t.clear()

# screen 3

screen.bgcolor('yellow')
t.pencolor("black")
t.penup()
t.goto(0, 200)
t.pendown()
t.write('Hobbies',font=("arial",30,"italic"),align="center")



t.penup()
t.goto(-200,-60)
t.pendown()
screen.addshape("baking2.gif")
t.shape("baking2.gif")
t.stamp()
t.shape("classic")


t.pencolor("black")
t.penup()
t.goto(-200, -170)
t.pendown()
t.write('Baking',font=("arial",30,"italic"),align="center")

t.penup()
t.goto(0,100)
t.pendown()
screen.addshape("travel2.gif")
t.shape("travel2.gif")
t.stamp()
t.shape("classic")


t.pencolor("black")
t.penup()
t.goto(0,-25)
t.pendown()
t.write('Traveling',font=("arial",30,"italic"),align="center")



t.penup()
t.goto(0,-180)
t.pendown()
screen.addshape("shopping2.gif")
t.shape("shopping2.gif")
t.stamp()
t.shape("classic")

t.pencolor("black")
t.penup()
t.goto(0, -300)
t.pendown()
t.write('Shopping',font=("arial",30,"italic"),align="center")



t.penup()
t.goto(200,-60)
t.pendown()
screen.addshape("tanning2.gif")
t.shape("tanning2.gif")
t.stamp()
t.shape("classic")

t.pencolor("black")
t.penup()
t.goto(200, -190)
t.pendown()
t.write('Tanning',font=("arial",30,"italic"),align="center")

t.penup()
t.goto(0, -350)
t.pendown()
t.write('Press enter to continue',font=("arial",20,"italic"),align="center")

t.fillcolor("pink")
t.begin_fill()
t.penup()
t.setheading(45)
t.goto(-200,200)
t.pendown()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()
t.penup()
t.goto(0,0)

round = input("Press Enter to Continue: ")

t.clear()

# screen 4

screen.bgcolor('lightgreen')
t.pencolor("black")
t.penup()
t.goto(0, 200)
t.pendown()
t.write('Favorite Movies',font=("arial",30,"italic"),align="center")

t.penup()
t.goto(-200,0)
t.pendown()
screen.addshape("movie2.gif")
t.shape("movie2.gif")
t.stamp()
t.shape("classic")

t.pencolor("black")
t.penup()
t.goto(-160, -250)
t.pendown()
t.write('Pirates of the Caribbean',font=("arial",20,"italic"),align="center")

t.penup()
t.goto(200,0)
t.pendown()
screen.addshape("movie3.gif")
t.shape("movie3.gif")
t.stamp()
t.shape("classic")

t.pencolor("black")
t.penup()
t.goto(200, -250)
t.pendown()
t.write('Tangled',font=("arial",30,"italic"),align="center")



t.penup()
t.goto(-50,0)
t.pendown()
t.pencolor("black")
t.fillcolor("blue")
t.begin_fill()
t.goto(0,50)
t.goto(50,0)
t.goto(-50,0)
t.end_fill()


t.penup()
t.goto(0, -350)
t.pendown()
t.write('Press enter to continue',font=("arial",20,"italic"),align="center")

round = input("Press Enter to Continue: ")

t.clear()

# screen 5

screen.bgcolor("DarkOrchid1")
t.pencolor("black")
t.penup()
t.goto(0, 200)
t.pendown()
t.write('Favorite Sports',font=("arial",30,"italic"),align="center")

t.penup()
t.goto(150,0)
t.pendown()
screen.addshape("dance2.gif")
t.shape("dance2.gif")
t.stamp()
t.shape("classic")

t.pencolor("black")
t.penup()
t.goto(180, -140)
t.pendown()
t.write('Competitive Dance',font=("arial",20,"italic"),align="center")

t.penup()
t.goto(-150,0)
t.pendown()
screen.addshape("cheer2.gif")
t.shape("cheer2.gif")
t.stamp()
t.shape("classic")


t.pencolor("black")
t.penup()
t.goto(-180, -140)
t.pendown()
t.write('Competitive Cheer',font=("arial",20,"italic"),align="center")


t.penup()
t.goto(0,-50)
t.pendown()
t.setheading(0)
t.penup()
t.forward(100)
t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor("green")
t.goto(0,-250)
t.pensize(5)
t.goto(0,-150)
t.pensize(1)
t.penup()

#circle - radius
t.pencolor("pink")
t.fillcolor("pink")
t.begin_fill()
t.circle(25)
t.setheading(270)
t.circle(25)
t.setheading(90)
t.circle(25)
t.setheading(180)
t.circle(25)
t.end_fill()

t.penup()
t.goto(0,-165)
t.pendown()
t.setheading(0)
t.fillcolor("yellow")
t.begin_fill()
t.circle(15)
t.end_fill()


turtle.done()