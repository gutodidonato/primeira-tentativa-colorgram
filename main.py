from turtle import *
import colorgram

timot = Turtle()
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g 
    b = color.rgb.b
    color = (r,g,b)
    rgb_colors.append(color)
    
screen = Screen()
screen.colormode(255)
    
    
print(len(rgb_colors))
def create_dot():
    for k in range(3):
        for i in range(10):
            timot.pendown()
            timot.dot(20,rgb_colors[k*10 + i])
            timot.penup()
            timot.forward(50)
        timot.home()
        timot.left(90)
        timot.forward(50*(k + 1))
        timot.right(90)
        
create_dot()

print(rgb_colors)


screen.exitonclick()