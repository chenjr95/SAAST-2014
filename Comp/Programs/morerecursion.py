from drawingpanel import *

def cantor_set(x, y, width, level, canvas):
    if level==0:
        pass
    else:
        canvas.create_rectangle(x, y, x+width, y+10, outline='orange', fill='purple')
        diff = width/3
        cantor_set(x,y+25, diff, level-1, canvas)
        cantor_set(x +2 * diff, y +25, diff, level - 1, canvas)

panel=DrawingPanel(1200,600)
cantor_set(10,20, 1100, 20, panel.canvas)
