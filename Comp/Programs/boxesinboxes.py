from drawingpanel import*
panel=DrawingPanel(500,500)
for i in range(0,250,25):
    panel.canvas.create_rectangle(0 + i, 0 + i, 500 - i, 500 - i,
        outline = 'DarkOrchid4', fill = 'purple')
panel.canvas.create_line(0,500,250,250, fill='forestgreen')
panel.canvas.create_line(250,250,500,500, fill='forestgreen')
