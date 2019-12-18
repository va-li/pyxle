from PIL import Image, ImageDraw
import numpy as np
import copy

def alpha_channel_slice(array: np):
    (width, heigth, channels) = np.shape()
    return array[1:2:5]

def create_white_image(width, height, rgba_color=None):
    rgba_array = np.zeros((width, height, 4))
    if rgba_color is None:
        # Fill white
        rgba_array.fill(255)

    rgba_array = np.array(rgba_array, dtype=np.uint8)
    return Image.fromarray(rgba_array)

def main():

    black = (0,0,0)
    gray = (127,127,127)
    white = (255,255,255)
    red = (255,0,0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    colors = [ black, gray, white, red, green, blue ]

    raster_width = 20
    raster_heigth = 40
    block_width = 10
    block_heigth = 10

    image_width = raster_width * block_width
    image_heigth = raster_heigth * block_heigth

    image = create_white_image(image_width, image_heigth)
    draw = ImageDraw.Draw(image)

    for cursor_x in range(0, raster_width):
        for cursor_y in range(0, raster_heigth):
            color = colors[(cursor_x + cursor_y) % len(colors)]
            draw.rectangle(
                (cursor_x * block_width,
                cursor_y * block_heigth,
                (cursor_x + 1) * block_width,
                (cursor_y + 1) * block_heigth),
                fill=color)

    image.save('./generated-image.png')

if __name__ == "__main__":
    main()
""" 
im = Image.open("hopper.jpg")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)

# write to stdout
im.save(sys.stdout, "PNG")


random_img('random.png', 300, 150) """