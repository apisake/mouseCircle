# this is a test for Git using github
# mouseCircle python code
def setup():
    size(600,600)    # set canvas to 600x600
    noStroke()       # draw circle with no stroke
    
def draw():
    # event-driven mouse pressed
    if mousePressed:
        fill(0)       # draw black
    else:
        fill(random(256),random(256),random(256),200)  # draw color in random
    cSize = random(20,80)    # set size of the circle
    ellipse(mouseX,mouseY,cSize,cSize)   # draw a circle in randomized fashion on size