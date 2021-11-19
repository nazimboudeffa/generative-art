def setup():
    size(1080,1080)
    noFill()

t = 0
NUM_TRIS = 90

def draw():
    global t
    background(255)
    translate(width/2, height/2)
    for i in range(NUM_TRIS):
        rotate(radians(360/NUM_TRIS))
        pushMatrix()
        translate(200,0)
        rotate(radians(t+2*i*360/NUM_TRIS))
    #rotate(radians(t))
        tri(100)
        popMatrix()
    t += 0.5
    
def tri(length):
    triangle(0,-length,-length*sqrt(3)/2,length/2,length*sqrt(3)/2,length/2)
