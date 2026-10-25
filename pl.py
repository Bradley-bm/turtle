import turtle
turtle.Screen().bgcolor("white")
turtle.setup(300, 400)
polygon = turtle.Turtle()
num_sides = 3
side_length = 70
angle = 360.0 / num_sides
for _ in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()