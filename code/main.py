from PIL import Image, ImageChops, ImageOps
import numpy as np
from os import listdir
from os.path import isfile, join


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_actual_element_distance(original_color_code, color_element_code):
    return np.sqrt(np.sum(np.square(original_color_code - color_element_code)))


def img_increment_occurrence(img_array, closest_element):
    img_array[closest_element]["count"] += 1


def print_img_occurrence(img_array):
    print("B0:{}, B1:{}, B2:{}, B3:{}, B4:{}, B5:{}, B6:{}, W0:{}, W1:{}, W2:{}, W3:{}, W4:{}, W5:{}, W6:{},"
        .format(
        img_array["black_0"]["count"],
        img_array["black_1"]["count"],
        img_array["black_2"]["count"],
        img_array["black_3"]["count"],
        img_array["black_4"]["count"],
        img_array["black_5"]["count"],
        img_array["black_6"]["count"],
        img_array["white_0"]["count"],
        img_array["white_1"]["count"],
        img_array["white_2"]["count"],
        img_array["white_3"]["count"],
        img_array["white_4"]["count"],
        img_array["white_5"]["count"],
        img_array["white_6"]["count"],
    ))


def get_closest_image(original_color, img_array):
    original_color_code = np.array((original_color.getpixel((1, 1))))
    closest_distance = 10000000
    closest_element = None

    for element in img_array:
        r_a, g_a, b_a = img_array[element].get("color").getpixel((1, 1))
        color_element_code = np.array((r_a, g_a, b_a))
        actual_element_distance = get_actual_element_distance(original_color_code, color_element_code)
        if closest_distance > actual_element_distance:
            closest_element = element
            closest_distance = actual_element_distance

    img_increment_occurrence(img_array, closest_element)
    return img_array.get(closest_element).get("img")


def dice_size(image_width, image_height, image_occurence_in_shortest_side, min_dice_size):

    dice_size = min_dice_size
    if image_width < image_height:
        dice_size = int(image_width / image_occurence_in_shortest_side)
    else:
        dice_size = int(image_height / image_occurence_in_shortest_side)

    return dice_size


# def build_img_palette_array():
#     onlyfiles = [f for f in listdir("input/img_pixel") if isfile(join("input/img_pixel", f))]
#     img_pixel_array = None
#     for img in onlyfiles:
#         img_pixel_array = Image.open(r"input/dices/black/0.jpg"),
#     s = "s"

def build_img_array():
    return {
        "black_0":
            {
                "img": Image.open(r"input/dices/black/0.jpg"),
                "color": Image.open(r"input/dices/black/0.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
        "black_1":
            {
                "img": Image.open(r"input/dices/black/1.jpg"),
                "color": Image.open(r"input/dices/black/1.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
        "black_2":
            {
                "img": Image.open(r"input/dices/black/2.jpg"),
                "color": Image.open(r"input/dices/black/3.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
        "black_3":
            {
                "img": Image.open(r"input/dices/black/3.jpg"),
                "color": Image.open(r"input/dices/black/4.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
        "black_4":
            {
                "img": Image.open(r"input/dices/black/4.jpg"),
                "color": Image.open(r"input/dices/black/4.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
        "black_5":
            {
                "img": Image.open(r"input/dices/black/5.jpg"),
                "color": Image.open(r"input/dices/black/5.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
        "black_6":
            {
                "img": Image.open(r"input/dices/black/6.jpg"),
                "color": Image.open(r"input/dices/black/6.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
        "white_0":
            {
                "img": Image.open(r"input/dices/white/0.jpg"),
                "color": Image.open(r"input/dices/white/0.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
        "white_1":
            {
                "img": Image.open(r"input/dices/white/1.jpg"),
                "color": Image.open(r"input/dices/white/1.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
        "white_2":
            {
                "img": Image.open(r"input/dices/white/2.jpg"),
                "color": Image.open(r"input/dices/white/2.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
        "white_3":
            {
                "img": Image.open(r"input/dices/white/3.jpg"),
                "color": Image.open(r"input/dices/white/3.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
        "white_4":
            {
                "img": Image.open(r"input/dices/white/4.jpg"),
                "color": Image.open(r"input/dices/white/4.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
        "white_5":
            {
                "img": Image.open(r"input/dices/white/5.jpg"),
                "color": Image.open(r"input/dices/white/5.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
        "white_6":
            {
                "img": Image.open(r"input/dices/white/6.jpg"),
                "color": Image.open(r"input/dices/white/6.jpg").convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB'),
                "count": 0
            },
    }


def convert_with_palette():
    palette = [
        46, 46, 45,
        77, 77, 76,
        110, 110, 109,
        161, 161, 161,
    ]

    img = Image.open(r"input/mccurry_afghan_girl.jpg")

    p_img = Image.new('P', (16, 16))
    p_img.putpalette(palette * 64)

    conv = img.quantize(palette=p_img, dither=0)
    conv.show()


def x():
    ImageChops.invert(Image.open(r"input/dices/black/0.jpg")).convert('RGB').save(r"input/dices/white/0.jpg")
    ImageChops.invert(Image.open(r"input/dices/black/1.jpg")).convert('RGB').save(r"input/dices/white/1.jpg")
    ImageChops.invert(Image.open(r"input/dices/black/2.jpg")).convert('RGB').save(r"input/dices/white/2.jpg")
    ImageChops.invert(Image.open(r"input/dices/black/3.jpg")).convert('RGB').save(r"input/dices/white/3.jpg")
    ImageChops.invert(Image.open(r"input/dices/black/4.jpg")).convert('RGB').save(r"input/dices/white/4.jpg")
    ImageChops.invert(Image.open(r"input/dices/black/5.jpg")).convert('RGB').save(r"input/dices/white/5.jpg")
    ImageChops.invert(Image.open(r"input/dices/black/6.jpg")).convert('RGB').save(r"input/dices/white/6.jpg")


if __name__ == '__main__':
    # build_img_palette_array()

    min_dice_size = 14
    image_occurence_in_shortest_side = 100
    image_name = "elena"

    image = Image.open(r"input/{}.jpg".format(image_name))
    # gray_image = ImageOps.grayscale(image)
    imageWidth, imageHeight = image.size
    image_copy = image.copy()

    diceSize = dice_size(imageWidth, imageHeight, image_occurence_in_shortest_side, min_dice_size)
    img_array = build_img_array()

    img_count = 0
    for y in range(0, imageHeight, diceSize):
        for x in range(0, imageWidth, diceSize):
            box = (x, y, x + diceSize, y + diceSize)
            cropped_image = image.crop(box)

            cropped_color = cropped_image.convert('P', palette=Image.ADAPTIVE, colors=1).convert('RGB')
            r, g, b = cropped_color.getpixel((1, 1))
            image_found = get_closest_image(cropped_color, img_array)

            position = (x, y)
            image_copy.paste(image_found.resize((diceSize, diceSize)), position)

            print("image anlyzed: {}".format(img_count))
            img_count += 1

    print_img_occurrence(img_array)
    image_copy.show()
    image_copy.save("output/{}.jpg".format(image_name))
    # Image.open(r"input/dices/5.png").convert('P', palette=Image.ADAPTIVE, colors=1).convert('RGB').show()

    # box = (0, 0, 500, 500)
    # cropped_image = image.crop(box)
    # cropped_image.save(r"output/cropped_image.jpg")
    # result = cropped_image.convert('P', palette=Image.ADAPTIVE, colors=2)
    # result.show()
