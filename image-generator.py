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

def hex_rgb(hex_color: str):
    if hex_color.startswith('#'):
        hex_color = hex_color[1:]
    elif hex_color.startswith('0x'):
        hex_color = hex_color[2:]
    
    assert 6 == len(hex_color)

    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return (r, g, b)

assert hex_rgb('FF0033') == (255, 0, 51)

def hexarr_rgbarr(arr: list):
    return list(map(lambda c: hex_rgb(c), arr))

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

    retro_palette = [ black, gray, white, red, green, blue, cyan, magenta, yellow ]

    sunset_palette = hexarr_rgbarr(['442c1b', '542715', '712f13', '8f3a14', '090504', 'c67b3f', 'e34410', 'e46418', 'f19329', 'f5b145', 'fcf0a3'])
    forrest_palette = hexarr_rgbarr([ '2b3443', '343446', '343c4a', '545b5c', '59665b', '5d666d', '646b60', '687763', '78846a', '7c9469', '879670', '97a578' ])

    colors = forrest_palette

    raster_width = 40
    raster_heigth = 40

    block_width = 20
    block_heigth = 20

    image_width = raster_width * block_width
    image_heigth = raster_heigth * block_heigth

    image = create_white_image(image_width, image_heigth)
    draw = ImageDraw.Draw(image)

    for x in range(0, raster_width):
        for y in range(0, raster_heigth):
            corruption = 5
            random = np.random.randint(0, corruption)
            color = colors[(
                (x) + (y)
            ) % len(colors) - random]
            draw.rectangle(
                (x * block_width,
                y * block_heigth,
                (x + 1) * block_width,
                (y + 1) * block_heigth),
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