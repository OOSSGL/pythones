import turtle

window = turtle.Screen()
tortuga = turtle.Turtle()

tortuga.forward(100)
tortuga.right(90)

tortuga.forward(100)
tortuga.right(90)

tortuga.forward(100)
tortuga.right(90)

tortuga.forward(100)
tortuga.right(90)

for i in range(10):
    for i in range(50):
        tortuga.forward(10)
        tortuga.right(10)
    tortuga.forward(10)

window.mainloop()
