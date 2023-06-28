import turtle
import random

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("AimLab")
score = 0
game_over = False
def create_score_turtle():
    score_turtle = turtle.Turtle()
    score_turtle.hideturtle()
    top_height = turtle_screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.penup()
    score_turtle.setpos(0, y)
    score_turtle.color("dark blue")
    return score_turtle

score_turtle = create_score_turtle()
Font = ("Arial", 20, "bold")
score_turtle.write(arg="Score: 0", move=False, align="center", font=Font)

grid_size = 10
Turtle_list = []

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=Font)

    t.onclick(handle_click)
    t.penup()
    t.shape("circle")
    t.shapesize(2, 2)
    t.color("white")
    t.goto(x * grid_size, y * grid_size)
    Turtle_list.append(t)

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]
countdown_turtle = turtle.Turtle()
def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in Turtle_list:
        t.hideturtle()

def show_turtle():
    if not game_over:
        hide_turtles()
        random.choice(Turtle_list).showturtle()
        turtle_screen.ontimer(show_turtle,500)

def countdown(time):
    global one_victory
    global game_over
    countdown_turtle.hideturtle()
    top_height = turtle_screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.penup()
    countdown_turtle.setpos(0, y - 30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=Font)
        turtle_screen.ontimer(lambda: countdown(time - 1), 1000)

    elif score > 19 and score < 29 and time < 1:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Victory", move=False, align="center", font=Font)

    elif score > 29 and time < 1:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Your Aim İs So Good", move=False, align="center", font=Font)

    elif score < 19 and time < 1:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="You Are So BAD", move=False, align="center", font=Font)



turtle.Screen().tracer(0)
setup_turtles()
hide_turtles()
show_turtle()
countdown(30)
turtle.Screen().tracer(1)

turtle.mainloop()
