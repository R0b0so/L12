import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(360,400)
polygon = turtle.Turtle() 
num_side = 6
side_length = 70
angle = 360 / num_side
for i in range(num_side):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()