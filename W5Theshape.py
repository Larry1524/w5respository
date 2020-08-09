wn = turtle.Screen()  
larry = turtle.Turtle()
 
sides = input ("Number of sides?"  )
length = input ("Length?" )
colorname = input ("Color?" )
fcolor = input ("Fill color?")
 
larry.color = (colorname)
larry.fillcolor = (fcolor)
 
for i in range(sides):
   larry.forward (length)
   larry.left (360 / sides)
