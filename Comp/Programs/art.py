'''WARNING THIS MAY CAUSE SEIZURES'''
## You can slow down speed by changing the value of 'bed'
## in the criss_cross function

from drawingpanel import *

panel = DrawingPanel(600,600)

def circle_fly_up1(i):
    if i<2500:
        panel.canvas.create_oval(100,(1600-i*0.7),200,(1600-i*0.7),outline = 'pink')

def circle_fly_up2(i):
    if i<2500:
        panel.canvas.create_oval(100,(1600-i*0.9),200,(1600-i*0.9),outline = 'red')

def circle_fly_up3(i):
    if i<2500:
        panel.canvas.create_oval(100,(1600-i),200,(1600-i),outline = 'orange')

def circle_fly_down1(i):
    if i>=3000 and i<=3270:
        panel.canvas.create_oval(400,(-2500+i*0.826),500,(-2500+i*0.826),outline = 'pink')

def circle_fly_down2(i):
    if i>=3000 and i<=3270:
        panel.canvas.create_oval(400,(-2500+i*0.9),500,(-2500+i*0.9),outline = 'red')

def circle_fly_down3(i):
    if i>=3000 and i<=3270:
        panel.canvas.create_oval(400,(-2500+i*.98),500,(-2500+i*.98),outline = 'orange')

def square_left1(i):
    if i<2500:
        for j in range(0, 10+i/100):
            panel.canvas.create_oval((1600-i*0.7),100,(1600-i*0.7), 200, outline = 'pink')

def square_left2(i):
    if i<2500:
        for j in range(0, 10+i/100):
            panel.canvas.create_oval((1600-i*0.9),100,(1600-i*0.9), 200, outline = 'red')

def square_left3(i):
    if i<2500:
        for j in range(0, 10+i/100):
            panel.canvas.create_oval((1600-i),100,(1600-i), 200, outline = 'orange')

def square_right1(i):
    if i>=3000 and i<=3270:
        for j in range(0, 10+i/100):
            panel.canvas.create_oval((-2500+i*0.826),400,(-2500+i*0.826), 500, outline = 'pink')

def square_right2(i):
    if i>=3000 and i<=3270:
        for j in range(0, 10+i/100):
            panel.canvas.create_oval((-2500+i*0.9),400,(-2500+i*0.9), 500, outline = 'red')

def square_right3(i):
    if i>=3000 and i<=3270:
        for j in range(0, 10+i/100):
            panel.canvas.create_oval((-2500+i*.98),400,(-2500+i*.98), 500, outline = 'orange')

def criss_cross():
    for i in range(1000,3270,10):
## Change speed of animation by changing the speed of 'bed'.
## Increasing the value will decrease the speed.
        bed=0
        panel.sleep(bed)
        circle_fly_down1(i)
        circle_fly_up1(i)
        square_left1(i)
        square_right1(i)
        panel.sleep(bed)
        panel.set_background('#' + str(i) + '9C')
        panel.sleep(bed)
        circle_fly_down2(i)
        circle_fly_up2(i)
        square_left2(i)
        square_right2(i)
        panel.sleep(bed)
        panel.set_background('#2F' + str(i))
        panel.sleep(bed)
        circle_fly_down3(i)
        circle_fly_up3(i)
        square_left3(i)
        square_right3(i)
        panel.sleep(bed)
        panel.set_background('#6C' + str(i))

def enlarge_square(x=0):
    if x>=600:
        return
    else:
        panel.canvas.create_rectangle(300-x,300-x,300+x,300+x, fill='#6c3270')
        x=x+10
        panel.sleep(5)
        enlarge_square(x)

def shrinking_square(x=0):
    if x==300:
        return
    else:
        y=x+100
        panel.sleep(10)
        panel.canvas.create_rectangle(x, x, 600-x, 600-x, fill='#1' + str(y) + 'E6')
        x=x+10
        shrinking_square(x)
        

criss_cross()
panel.sleep(1000)
enlarge_square()
shrinking_square()

## Chris Champagne is not liable for any injuries resulting from this program.
## View at your own risk.
