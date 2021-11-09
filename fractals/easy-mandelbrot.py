from PIL import Image

x1 = -2.0
x2 = 2.0
y1 = -2.0
y2 = 2.0

n = 100
w = 1080
h = 1080

image = Image.new("RGB", (w, h))

for x in range(w):
    for y in range(h):
        
        a = x * (x2 - x1) / w  + x1
        b = y * (y2 - y1) / h  + y1
        
        c = a + 1j * b
        z = c
        
        i = 0
        
        while i < n :
            
            if abs(z) > 2.0: break 
            z = z * z + c
            i += 1
            
        image.putpixel((x, y), (i % 10 * 25, i % 10 * 25, i % 10 * 25))

image.show()
