import random
from turtle import Turtle ,Screen
win=Screen()
win.title("octucode turtle race")
win.setup(width=880,height=800)
colors=("red","green","blue")
location=(-350,0,350)

user_bet=win.textinput(title="type your bet",prompt="chose the winner turtle red ,green or blue")

turtles=[]
for i in range(3):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-450,y=(location[i]))
    turtles.append(new_turtle)



def race_turtles():
    game_on=True
    while game_on:
        for turtle in turtles:
            if turtle.xcor()>=350:
                game_on=False
                winner=turtle.pencolor()
                display_result(winner)  
            else:                
                turtle.forward(random.randint(0,10))
       
def display_result(winning_color): #وهنا بتدي الدالة براميتر وتاخد قيمته من المتغير اللي فوق
    result_turtle=Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(0,0)
    result_turtle.pendown()
    #if winning_color:يعني لو القيمة بتاعته ترو ويتسلق لفوق لحد مايجيب قيمة التحقق من فوق 
    if user_bet== winning_color:
        win.bgcolor("dark green")
        result_turtle.color("white")
        result_turtle.write("You Win!", align="center", font=("Arial", 40, "bold"))
    else:
        win.bgcolor("medium violet red")
        result_turtle.color("white")
        result_turtle.write("you lose", align="center",font=("arial",40, "bold"))

race_turtles()
win.exitonclick()