import turtle
turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(360,400)
my_pen = turtle.Turtle()
size = 0
while True: 
    for i in range(5):
        my_pen.fd(size+1)
        my_pen.left(75)
        size = size - 5
    size = size + 1
