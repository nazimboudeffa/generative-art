squareSize = 40
gridSize = 10

size(1080, 1080)
background(0, 0, 0)
blendMode(ADD)

i = 0
while i < 11 : 
  i += 1
  j = 0
  while j < 11 :
    j += 1
    posX = i * 80
    posY = j * 80
    dist = 10
    col = 255
    sqSz = random(60)
    fill(col, 0, 0)
    rect(posX, posY, sqSz, sqSz);
    fill(0, col, 0)
    rect(posX + 10, posY + dist, sqSz, sqSz);
    fill(0, 0, col)
    rect(posX + 20, posY + dist * 2, sqSz, sqSz)

save("D:/generativeart/img.png")
