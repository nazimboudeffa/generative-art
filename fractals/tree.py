# Random Spiral Fractals
# FB36 - 20130914
import math
import random
from collections import deque
from PIL import Image
imgx = 1024; imgy = 1024
image = Image.new("RGB", (imgx, imgy))
pixels = image.load()
xa = -1.5; xb = 1.5
ya = -1.5; yb = 1.5
n = random.randint(2, 9)  # of spiral arms
m = random.randint(6, 12) # of spirals in each arm
a = 2.0 * math.pi / n     # angle between arms
b = 2.0 * math.pi * random.random() # max rotation (bending) angle for each arm
rmax = 0.1 * random.random() + 0.1 # max spiral radius on each arm
maxIt = 8 # max number of iterations allowed
# create random color palette
rd = []; gr = []; bl = []
for c in range(maxIt):
    rd.append(random.randint(0, 255))
    gr.append(random.randint(0, 255))
    bl.append(random.randint(0, 255))

for ky in range(imgy):
    #print str(100 * ky / (imgy - 1)).zfill(3) + "%"
    for kx in range(imgx):
        x = float(kx) / (imgx - 1) * (xb - xa) + xa
        y = float(ky) / (imgy - 1) * (yb - ya) + ya
        queue = deque([])
        queue.append((x, y, 0))
        while len(queue) > 0: # iterate points until none left
            (x, y, i) = queue.popleft()
            # apply all (inverse) IFS transformations
            for k in range(n): # of arm
                for j in range(m): # of a spiral on the arm
                    c = k * a + b * (j + 1.0) / m # angle of the spiral in the arm
                    d = (j + 1.0) / m # distance of the spiral to the center
                    r = d * rmax # radius of the spiral in the arm
                    if r != 0.0:
                        xnew = (x - math.sin(c) * d) / r
                        ynew = (y - math.cos(c) * d) / r
                        if xnew >= xa and xnew <= xb and ynew >= ya and ynew <= yb:
                            if i + 1 == maxIt: break
                            queue.append((xnew, ynew, i + 1))
        pixels[kx, ky] = (rd[i], gr[i], bl[i])
image.save("d:/generativeart/RandomSpiralFractal_" + str(n) + "_" + str(m) + ".png", "PNG")