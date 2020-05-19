import turtle, random
colors = ["red","green", "blue", "orange", "purple", "pink", "yellow"]
painter = turtle.Turtle()
painter.pensize(3)
for i in range ( 10):
    color  = random.choice(colors)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.retposition(0, 0)
    
    
    
