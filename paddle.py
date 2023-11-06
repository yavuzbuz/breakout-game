from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.speed("fastest")
        self.penup()
        self.goto(0, -390)
        self.MOVING, self.DRAGGING = range(2)
        self.state = self.MOVING
        self.screen = screen
        self.onmove(self.screen, self.move_handler)
        self.onclick(self.click_handler)
        self.x = 0

    def move_handler(self, x, y):
        if self.state != self.MOVING:
            return

        self.onmove(self.screen, None)
        self.penup()
        self.setheading(self.towards(x, -390))
        self.goto(x, -390)
        self.onmove(self.screen, self.move_handler)

    def click_handler(self):
        self.onclick(None)
        self.onmove(self.screen, None)

        self.onrelease(self.release_handler)
        self.ondrag(self.drag_handler)

        self.state = self.DRAGGING

    def release_handler(self):
        self.onrelease(None)
        self.ondrag(None)

        self.onclick(self.click_handler)
        self.onmove(self.screen, self.move_handler)

        self.state = self.DRAGGING

    def drag_handler(self, x):
        if self.state != self.DRAGGING:
            return

        self.ondrag(None)
        self.penup()
        self.setheading(self.towards(x, -390))
        self.goto(x, -390)
        self.ondrag(self.drag_handler)

    def onmove(self, s, fun, add=None):
        if fun is None:
            s.cv.unbind('<Motion>')
        else:
            def eventfun(event):
                fun(s.cv.canvasx(event.x) / s.xscale, -s.cv.canvasy(event.y) / s.yscale)
            s.cv.bind('<Motion>', eventfun, add)
