import uuid
import random
from PIL import Image, ImageDraw


def sum_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return x1 + x2, y1 + y2


run_id = uuid.uuid1()
print(f'Processing run_id: {run_id}')

canvas_size = (5000, 5000)
canvas_color = (240, 240, 240)
line_color = (10, 10, 10)
hor_side_offset = 700
ver_side_offset = 700
circle_count = 6000
min_circle_size = 500
max_circle_size = 5 * min_circle_size

image = Image.new('RGB', canvas_size, color=canvas_color)
width, height = image.size
draw = ImageDraw.Draw(image, 'RGBA')

for i in range(circle_count):
    circle_size = random.uniform(min_circle_size, max_circle_size)
    circle_upper_left = (random.uniform(-circle_size, width), random.uniform(-circle_size, height))
    circle_lower_right = sum_points(circle_upper_left, (circle_size, circle_size))

    draw.ellipse((circle_upper_left, circle_lower_right), outline=line_color, width=4)

image_mask = Image.new('RGBA', (width, height), color=canvas_color)
draw_mask = ImageDraw.Draw(image_mask)

draw_mask.rectangle((hor_side_offset, ver_side_offset, width - hor_side_offset, height - ver_side_offset), fill=0)
image.paste(image_mask, (0, 0), image_mask)

image.show()
image.save(f'./output/{run_id}.png')
