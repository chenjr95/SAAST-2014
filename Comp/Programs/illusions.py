from drawingpanel import*

panel=DrawingPanel(500,500)

panel.set_background('green')

def square(x,y,z):
    panel.canvas.create_rectangle(x,y,z+x,y+z, outline = 'black', fill = 'cyan')

def diamond(x,y,z):
    panel.canvas.create_line(x,((z+y)+y)*0.5,((z+x)+x)*0.5,y, fill='black')
    panel.canvas.create_line(((z+x)+x)*0.5,y,z+x,((z+y)+y)*0.5, fill='black')
    panel.canvas.create_line((((z+x)+x)*0.5),z+y,x,((z+y)+y)*0.5, fill='black')
    panel.canvas.create_line((((z+x)+x)*0.5),z+y,z+x,((z+y)+y)*0.5, fill='black')

def circles_with(x,y,z,c):
    square(x,y,z)
    for i in range(0,c,1):
            panel.canvas.create_oval(x+i*(0.5*z/c), y+i*(0.5*z/c), (z+x)-i*(0.5*z/c),
                                     (z+y)-i*(0.5*z/c), outline = 'black', fill='yellow')
    diamond(x,y,z)

def grid_with(x,y,z,c,l=1,w=1):
    a=x
    for i in range(1,w+1):
        x=a
        for j in range(1,l+1):
            circles_with(x,y,z,c)
            x=x+z
        y=y+z

def circles_without(x,y,z,c):
    for i in range(0,c,1):
            panel.canvas.create_oval(x+i*(0.5*z/c), y+i*(0.5*z/c), (z+x)-i*(0.5*z/c),
                                     (z+y)-i*(0.5*z/c), outline = 'black', fill='yellow')

def grid_without(x,y,z,c,l=1,w=1):
    a=x
    for i in range(1,w+1):
        x=a
        for j in range(1,l+1):
            circles_without(x,y,z,c)
            x=x+z
        y=y+z
        
grid_with(0,0,75,6)
grid_with(105,15,50,10,7,1)
grid_with(10,100,70,3,2,5)
grid_with(175,115,100,8,3,3)
grid_without(200,430,25,4,10,2)
