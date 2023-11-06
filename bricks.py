from turtle import Turtle


class Layer1:

    def __init__(self):
        super().__init__()

        self.layer_1 = []
        for i in range(12):
            self.layer_1.append(Turtle())

        location = -720
        append_num = 110
        for brick in self.layer_1:
            brick.shape("square")
            brick.shapesize(stretch_wid=1, stretch_len=5)
            brick.color("cyan")
            brick.penup()
            self.new_cor = location + append_num
            location += 110
            brick.goto((self.new_cor, 150))


class Layer2:

    def __init__(self):
        super().__init__()

        self.layer_2 = []
        for i in range(12):
            self.layer_2.append(Turtle())

        location = -720
        append_num = 110
        for brick in self.layer_2:
            brick.shape("square")
            brick.shapesize(stretch_wid=1, stretch_len=5)
            brick.color("purple")
            brick.penup()
            self.new_cor = location + append_num
            location += 110
            brick.goto((self.new_cor, 180))


class Layer3:

    def __init__(self):
        super().__init__()

        self.layer_3 = []
        for i in range(12):
            self.layer_3.append(Turtle())

        location = -720
        append_num = 110
        for brick in self.layer_3:
            brick.shape("square")
            brick.shapesize(stretch_wid=1, stretch_len=5)
            brick.color("blue")
            brick.penup()
            self.new_cor = location + append_num
            location += 110
            brick.goto((self.new_cor, 210))


class Layer4:

    def __init__(self):
        super().__init__()

        self.layer_4 = []
        for i in range(12):
            self.layer_4.append(Turtle())

        location = -720
        append_num = 110
        for brick in self.layer_4:
            brick.shape("square")
            brick.shapesize(stretch_wid=1, stretch_len=5)
            brick.color("green")
            brick.penup()
            self.new_cor = location + append_num
            location += 110
            brick.goto((self.new_cor, 240))


class Layer5:

    def __init__(self):
        super().__init__()

        self.layer_5 = []
        for i in range(12):
            self.layer_5.append(Turtle())

        location = -720
        append_num = 110
        for brick in self.layer_5:
            brick.shape("square")
            brick.shapesize(stretch_wid=1, stretch_len=5)
            brick.color("yellow")
            brick.penup()
            self.new_cor = location + append_num
            location += 110
            brick.goto((self.new_cor, 270))


class Layer6:

    def __init__(self):
        super().__init__()

        self.layer_6 = []
        for i in range(12):
            self.layer_6.append(Turtle())

        location = -720
        append_num = 110
        for brick in self.layer_6:
            brick.shape("square")
            brick.shapesize(stretch_wid=1, stretch_len=5)
            brick.color("orange")
            brick.penup()
            self.new_cor = location + append_num
            location += 110
            brick.goto((self.new_cor, 300))


class Layer7:

    def __init__(self):
        super().__init__()

        self.layer_7 = []
        for i in range(12):
            self.layer_7.append(Turtle())

        location = -720
        append_num = 110
        for brick in self.layer_7:
            brick.shape("square")
            brick.shapesize(stretch_wid=1, stretch_len=5)
            brick.color("red")
            brick.penup()
            self.new_cor = location + append_num
            location += 110
            brick.goto((self.new_cor, 330))

