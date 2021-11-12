z = 0 
n = 0
h = 100
s = 100
v = 100
a = 0
b = 0
b2 = 0 #new b
a2 = 0 #new a
b3 = 0 #original b
a3 = 0 #original a
bright = 255 
zoom = 5
xoff = -1.5
speedup = 0
speedTarget = 2
 
#f(z) = z^2 + c
#a^2-b^2 + 2abi
 
def setup() : 
    size(1080, 1080) 
    smooth()
    frameRate(60)
    background(200,100,100)
    colorMode(HSB, 100)
 
def draw() :
    #zoom = zoom/((speedup/100)+1)
    #speedup = ((speedup*10)+speedTarget)/11
    loadPixels();
    
    for x in range(width):
        for y in range(height):
            
            a = map(x,0,width,-2,2)
            b = map(y,0,height,-2,2)
            
            n = 0
            z = 0
            a3 = a
            b3 = b
            
            while n < 100 :
                aa = (a*a) - (b*b)
                bb = 2*a*b
                a = aa + a3
                b = bb + b3
                if(abs(aa + bb) > 16):
                    break     
                n += 1
                
            bright = map(n,0,100,0,1)
            bright = map((sqrt(bright)+(bright*20))/21,0,1,0,255) 
            if n == 100 :
                bright = 0 
            
            
            h = bright
            s = 250-bright
            v = bright
            pixels[x + (y*width)] = color(h,s,v)
        
    
    updatePixels()
    #noloop()
