import turtle as t
import random

tim = t.Turtle()

colors = ("CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen")
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fast")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))
