import random
import uuid

from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

image = Image.new('RGB', (2000, 2000))
width, height = image.size

rectangle_width = 100
rectangle_height = 100

number_of_squares = random.randint(10, 550)

draw_image = ImageDraw.Draw(image)
for i in range(number_of_squares):
    rectangle_x = random.randint(0, width)
    rectangle_y = random.randint(0, height)

    rectangle_color = [(254,218,117),(250,126,30),(214,41,118),(150,47,191),(79,91,213)]
    rectangle_shape = [
        (rectangle_x, rectangle_y),
        (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
    draw_image.rectangle(
        rectangle_shape,
        fill=(rectangle_color(random.randint(0,3)))
        #fill=(
            #random.randint(0, 255),
            #random.randint(0, 255),
            #random.randint(0, 255)
        #)
    )

image.save(f'D:/opensea-nft/{run_id}.png')