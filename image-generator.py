from PIL import Image, ImageDraw
import numpy as np
import copy

def alpha_channel_slice(array: np):
    (width, heigth, channels) = np.shape()
    return array[1:2:5]

def create_white_image(width, height, rgba_color=None):
    rgba_array = np.zeros((height, width, 4))
    if rgba_color is not None:
        # Fill with color
        ()

    rgba_array = np.array(rgba_array, dtype=np.uint8)
    return Image.fromarray(rgba_array)

def main():

    black = (0,0,0)
    gray = (127,127,127)
    white = (255,255,255)
    red = (255,0,0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    cyan = (0, 255, 255)
    magenta = (255, 0, 255)
    yellow = (255, 255, 0)

    colors = [ black, gray, white, red, green, blue, cyan, magenta, yellow ]

    raster_width = 40
    raster_heigth = 40

    image = create_white_image(raster_width, raster_heigth)
    draw = ImageDraw.Draw(image)

    for cursor_x in range(0, raster_width):
        for cursor_y in range(0, raster_heigth):
            random = np.random.randint(cursor_x + 1, cursor_x + 2 + cursor_x * cursor_y)
            color = colors[((cursor_x + ((3 * cursor_x % (3 * cursor_y + 1)) *  cursor_x)) * (cursor_y + cursor_x)) % len(colors)]
            draw.rectangle(
                (cursor_x,
                cursor_y,
                (cursor_x + 1),
                (cursor_y + 1)),
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