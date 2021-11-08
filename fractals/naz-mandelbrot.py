from PIL import Image
from PIL import ImageDraw

xa = -2.0
xb = 2.0
ya = -2.0
yb = 2.0

n = 100
imgx = 500
imgy = 500

image = Image.new("RGB", (imgx, imgy))

for x in range(imgx):
    for y in range(imgy):
        
        a = x * (xb - xa) / imgx  + xa
        b = y * (yb - ya) / imgy  + ya
        
        c = a + 1j * b
        z = c
        
        i = 0
        
        while i < n :
            
            if abs(z) > 2.0: break 
            z = z * z + c
            i += 1
            
        image.putpixel((x, y), (i % 16 * 255, i % 16 * 255, i % 16 * 255))

image.save("d:/generativeart/mandel.png", "PNG")
