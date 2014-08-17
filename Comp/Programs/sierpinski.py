from drawingpanel import *

def sierpinski(x1,y1,x2,y2,x3,y3,level,canvas):
    if level==0:
        canvas.create_polygon(x1,y1,x2,y2,x3,y3,outline='black',fill='gold')
    else:
        xa=(x1+x2)*0.5
        xb=(x2+x3)*0.5
        xc=(x3+x1)*0.5
        ya=(y1+y2)*0.5
        yb=(y2+y3)*0.5
        yc=(y3+y1)*0.5
        sierpinski(x1,y1,xa,ya,xc,yc,level-1,canvas)
        sierpinski(xa,ya,x2,y2,xb,yb,level-1,canvas)
        sierpinski(xc,yc,xb,yb,x3,y3,level-1,canvas)
    


panel=DrawingPanel(600,600)
sierpinski(50,550,300,117,550,550,3,panel.canvas)
