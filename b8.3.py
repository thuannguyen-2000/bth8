import turtle,random
window = turtle.Screen()
painter = turtle.Turtle()
colors = ["red","green", "blue", "orange", "purple", "pink", "yellow"]
painter = turtle.Turtle()
painter.pensize(3)
for i in range ( 12):
    color  = random.choice(colors)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
def drawsq(t, s, colors):
    for i in range(4):
        t.forward(s)
        t.left(90)
    
