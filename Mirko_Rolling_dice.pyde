def setup():
    size(700,700)
    dice=0

def draw():
    circle(0,0,0)

def mouseClicked():
    global dice
    fill(255,255,255)
    
    square(100,100,500)
    
    fill(255,0,0)
    
    dice=int(random(1,10))
    if dice==1:
        circle(350,350,50)
    if dice==2:
        circle(500,200,50)
        circle(200,500,50)
    if dice==3:
        circle(350,350,50)
        circle(200,200,50)
        circle(500,500,50)
    if dice==4:
        circle(200,200,50)
        circle(500,500,50)
        circle(500,200,50)
        circle(200,500,50)
    if dice==5:
        circle(200,200,50)
        circle(500,500,50)
        circle(500,200,50)
        circle(200,500,50)
        circle(350,350,50)
    if dice==6:
        circle(200,200,50)
        circle(500,500,50)
        circle(500,200,50)
        circle(200,500,50)
        circle(200,350,50)
        circle(500,350,50)       
    if dice==7:
        circle(200,200,50)
        circle(200,350,50)
        circle(200,500,50)
        circle(350,350,50)
        circle(500,350,50)
        circle(500,500,50)
        circle(500,200,50)
    if dice==8:
        circle(200,200,50)
        circle(500,500,50)
        circle(500,200,50)
        circle(200,500,50)
        circle(200,350,50)
        circle(500,350,50)
        circle(350,200,50)
        circle(350,500,50)
    if dice==9:
        circle(200,200,50)
        circle(200,350,50)
        circle(200,500,50)
        circle(350,350,50)
        circle(500,350,50)
        circle(500,500,50)
        circle(500,200,50)
        circle(350,200,50)
        circle(350,500,50)
    
       
    
    
    
