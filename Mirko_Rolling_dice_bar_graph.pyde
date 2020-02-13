#definition of variable 
one_c= 0
two_c= 0
three_c= 0
four_c= 0
five_c= 0
six_c= 0

def setup():
    size(700,700)
    dice=0
    textSize(30)

def draw():
    circle(0,0,0)
    mouseClicked()
    delay(10)
    barGraph()


def mouseClicked():
    global  one_c, two_c, three_c, four_c,five_c, six_c
    fill(255,255,255)
    stroke(0)
    strokeWeight(10)
    rect(100,100,500,500,55)
    
    fill(255,0,0)
    
    dice=random(0,6)
    if 0<=dice<1:
        circle(350,350,50)
        one_c= one_c + 1
        print ("Number of rolls for number one",one_c)
    if 1<=dice<2:
        circle(500,200,50)
        circle(200,500,50)
        two_c += 1
        print ("Number of rolls for number two",two_c)
    if 2<=dice<3:
        circle(350,350,50)
        circle(200,200,50)
        circle(500,500,50)
        three_c += 1
        print ("Number of rolls for number three",three_c)
    if 3<=dice<4:
        circle(200,200,50)
        circle(500,500,50)
        circle(500,200,50)
        circle(200,500,50)
        four_c += 1
        print ("Number of rolls for number four",four_c)
    if 4<=dice<5:
        circle(200,200,50)
        circle(500,500,50)
        circle(500,200,50)
        circle(200,500,50)
        circle(350,350,50)
        five_c += 1
        print ("Number of rolls for number five",five_c)
    if 5<=dice<6:
        circle(200,200,50)
        circle(500,500,50)
        circle(500,200,50)
        circle(200,500,50)
        circle(200,350,50)
        circle(500,350,50) 
        six_c += 1 
        print ("Number of rolls for number six",six_c) 

def barGraph():
    fill(0)
    for x in range(6):
        text(x+1,50+ 50*x,590)
    stroke(100,200,240)
    rect(50, 560 - one_c,20,one_c)
    stroke(200,50,140)
    rect(100, 560 - two_c,20,two_c)
    stroke(110,230,40)
    rect(150, 560 - three_c,20,three_c)
    stroke(90,150,180)
    rect(200, 560 - four_c,20,four_c)
    stroke(220,150,100)
    rect(250, 560 - five_c,20,five_c)
    stroke(111,166,222)
    rect(300, 560 - six_c,20,six_c)
    text("Rolls:",350,590)
    total=one_c+two_c+three_c+four_c+five_c+six_c
    text(total,450,590)
     
