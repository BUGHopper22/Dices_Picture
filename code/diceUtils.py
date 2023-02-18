from PIL import Image
import numpy as np


def build_dice_array_rgb_gap():
    skip_rgb_color_number = 18
    actual_color_number = 0
    img_array = {}
    for i in range(0, 7):
        key = "black_{}".format(i)
        img_array[key] = {
            "img": Image.open(r"input/dices/black/{}.jpg".format(i)),
            "color": (actual_color_number, actual_color_number, actual_color_number),
            "count": 0
        }
        actual_color_number = actual_color_number + skip_rgb_color_number

    for i in range(0, 7):
        key = "white_{}".format(i)
        img_array[key] = {
            "img": Image.open(r"input/dices/white/{}.jpg".format(i)),
            "color": (actual_color_number, actual_color_number, actual_color_number),
            "count": 0
        }
        actual_color_number = actual_color_number + skip_rgb_color_number
    return img_array


def build_dice_array_with_adaptive_color():
    img_array = {}
    for i in range(0, 7):
        key = "black_{}".format(i)
        img_array[key] = {
            "img": Image.open(r"input/dices/black/{}.jpg".format(i)),
            "color": Image.open(r"input/dices/black/{}.jpg".format(i)).convert('P', palette=Image.ADAPTIVE,
                                                                               colors=1).convert(
                'RGB').getpixel((1, 1)),
            "count": 0
        }

    for i in range(0, 7):
        key = "white_{}".format(i)
        img_array[key] = {
            "img": Image.open(r"input/dices/white/{}.jpg".format(i)),
            "color": Image.open(r"input/dices/white/{}.jpg".format(i)).convert('P', palette=Image.ADAPTIVE,
                                                                               colors=1).convert(
                'RGB').getpixel((1, 1)),
            "count": 0
        }
    return img_array


def get_dice_size(image_width, image_height, image_occurence_in_shortest_side, min_dice_size):
    if image_width < image_height:
        dice_size = int(image_width / image_occurence_in_shortest_side)
    else:
        dice_size = int(image_height / image_occurence_in_shortest_side)

    if dice_size < min_dice_size:
        dice_size = min_dice_size

    return dice_size


def get_actual_element_distance(original_color_code, color_element_code):
    return np.sqrt(np.sum(np.square(original_color_code - color_element_code)))


def img_increment_occurrence(img_array, closest_element):
    img_array[closest_element]["count"] += 1


def get_closest_image(original_color, img_array):
    original_color_code = np.array((original_color.getpixel((1, 1))))
    closest_distance = 10000000
    closest_element = None

    for element in img_array:
        r_a, g_a, b_a = img_array[element].get("color")
        color_element_code = np.array((r_a, g_a, b_a))
        actual_element_distance = get_actual_element_distance(original_color_code, color_element_code)
        if closest_distance > actual_element_distance:
            closest_element = element
            closest_distance = actual_element_distance

    img_increment_occurrence(img_array, closest_element)
    return img_array.get(closest_element).get("img")
