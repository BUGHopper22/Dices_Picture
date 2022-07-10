import numpy as np
from PIL import Image, ImageChops


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
        # r_a, g_a, b_a = img_array[element].get("color").getpixel((1, 1))
        r_a, g_a, b_a = img_array[element].get("color")
        color_element_code = np.array((r_a, g_a, b_a))
        actual_element_distance = get_actual_element_distance(original_color_code, color_element_code)
        if closest_distance > actual_element_distance:
            closest_element = element
            closest_distance = actual_element_distance

    img_increment_occurrence(img_array, closest_element)
    return img_array.get(closest_element).get("img")


def get_dice_size(image_width, image_height, image_occurence_in_shortest_side, min_dice_size):
    if image_width < image_height:
        dice_size = int(image_width / image_occurence_in_shortest_side)
    else:
        dice_size = int(image_height / image_occurence_in_shortest_side)

    if dice_size < min_dice_size:
        dice_size = min_dice_size

    return dice_size


# def build_img_palette_array():
#     onlyfiles = [f for f in listdir("input/img_pixel") if isfile(join("input/img_pixel", f))]
#     img_pixel_array = None
#     for img in onlyfiles:
#         img_pixel_array = Image.open(r"input/dices/black/0.jpg"),
#     s = "s"

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
            "color": Image.open(r"input/dices/black/{}.jpg".format(i)).convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB').getpixel((1, 1)),
            "count": 0
        }

    for i in range(0, 7):
        key = "white_{}".format(i)
        img_array[key] = {
            "img": Image.open(r"input/dices/white/{}.jpg".format(i)),
            "color": Image.open(r"input/dices/white/{}.jpg".format(i)).convert('P', palette=Image.ADAPTIVE, colors=1).convert(
                    'RGB').getpixel((1, 1)),
            "count": 0
        }
    return img_array


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


def print_created_image(image_copy, img_array):
    print_img_occurrence(img_array)
    image_copy.show()
    image_copy.save("output/{}.jpg".format(image_name))


if __name__ == '__main__':

    # CONSTANTS
    min_dice_size = 10
    image_occurence_in_shortest_side = 200
    image_name = "alberto_elena_7"
    image = Image.open(r"input/original_photos/{}.jpg".format(image_name))

    imageWidth, imageHeight = image.size
    diceSize = get_dice_size(imageWidth, imageHeight, image_occurence_in_shortest_side, min_dice_size)

    img_array_adaptive = build_dice_array_with_adaptive_color()
    img_array_rgb_gap = build_dice_array_rgb_gap()

    image_copy_adaptive = image.copy()
    image_copy_rgb_gap = image.copy()
    img_count = 0

    for y in range(0, imageHeight, diceSize):
        for x in range(0, imageWidth, diceSize):
            box = (x, y, x + diceSize, y + diceSize)
            cropped_image = image.crop(box)

            cropped_color = cropped_image.convert('P', palette=Image.ADAPTIVE, colors=1).convert('RGB')
            r, g, b = cropped_color.getpixel((1, 1))

            image_found_adaptive = get_closest_image(cropped_color, img_array_adaptive)
            image_found_rgb_gap = get_closest_image(cropped_color, img_array_rgb_gap)

            position = (x, y)
            image_copy_adaptive.paste(image_found_adaptive.resize((diceSize, diceSize)), position)
            # image_copy_rgb_gap.paste(image_found_rgb_gap.resize((diceSize, diceSize)), position)

            print("image anlyzed: {}".format(img_count))
            img_count += 1

    # print_created_image(image_copy_adaptive, image_found_adaptive)
    # print_created_image(image_copy_rgb_gap, image_found_rgb_gap)
    image_copy_adaptive.show()
    image_copy_adaptive.save("output/{}.jpg".format(image_name))
