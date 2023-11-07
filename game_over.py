from turtle import Turtle


class Lost(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(-500, -100)
        self.write("GAME OVER", move=False, align="left", font=("Arial", 160, "normal"))


class Won(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(-500, -100)
        self.write("YOU HAVE WON!", move=False, align="left", font=("Arial", 160, "normal"))
