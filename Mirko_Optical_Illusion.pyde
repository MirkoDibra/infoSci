offset = 50
def mouseClicked():
    global offset
    offset= offset+1

def setup():
    size(500,500)
    background(255)

def draw():
    stroke(0)
    
    for y in range(50):
        line(0,50*y,500,50*y)
    
    y=0    
    for rows in range (5):
        x=0
        for rep in range (5):
            fill(0)
            stroke(255)
            square(x,y,50)
            x=x+100
        y=y+100
    
    y = 50
    global offset
    for rows in range (5):
        x=0 + offset
        for rep in range (5):
            fill(0)
            stroke(255)
            square(x,y,50)
            x=x+100
        y=y+100
        
    
