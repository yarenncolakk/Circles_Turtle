import turtle
pencere=turtle.Screen()
tt=turtle.Turtle()
tt.shape("turtle")
tt.color("orange","pink")
tt.pensize(3)
tt.speed(1)
tt.begin_fill()
for i in range(8):
    tt.right(45)
    tt.circle(50)
tt.end_fill()    
pencere.exitonclick()    
