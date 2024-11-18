import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(360,400)
polygon = turtle.Turtle() 
num_side = 4
side_length = 100
angle = 90 
for i in range(num_side):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()