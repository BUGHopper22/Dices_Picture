import yaml
from PIL import Image, ImageChops
import diceUtils as bu


def read_yaml():
    with open('config/application.yaml', "r") as f:
        return yaml.load(f, yaml.FullLoader)


def create_image():
    image_copy_adaptive = image.copy()
    image_copy_rgb_gap = image.copy()
    img_count = 0

    for y in range(0, imageHeight, diceSize):
        for x in range(0, imageWidth, diceSize):
            box = (x, y, x + diceSize, y + diceSize)
            cropped_image = image.crop(box)

            cropped_color = cropped_image.convert('P', palette=Image.ADAPTIVE, colors=1).convert('RGB')
            r, g, b = cropped_color.getpixel((1, 1))

            image_found_adaptive = bu.get_closest_image(cropped_color, img_array_adaptive)
            image_found_rgb_gap = bu.get_closest_image(cropped_color, img_array_rgb_gap)

            position = (x, y)
            image_copy_adaptive.paste(image_found_adaptive.resize((diceSize, diceSize)), position)
            image_copy_rgb_gap.paste(image_found_rgb_gap.resize((diceSize, diceSize)), position)

            print("image anlyzed: {}".format(img_count))
            img_count += 1

    image_copy_rgb_gap.show()
    image_copy_rgb_gap.save("output/{}.jpg".format(image_name + "1"))
    image_copy_adaptive.show()
    image_copy_adaptive.save("output/{}.jpg".format(image_name + "2"))


if __name__ == '__main__':
    props = read_yaml()

    min_dice_size = props["MIN_DICE_SIZE"]
    image_occurence_in_shortest_side = props['IMAGE_OCCURENCE_IN_SHORTEST_SIDE']
    image_name = props['IMAGE_NAME']
    path = props['PATH']
    image = Image.open(r"{}{}".format(path, image_name))

    imageWidth, imageHeight = image.size
    diceSize = bu.get_dice_size(imageWidth, imageHeight, image_occurence_in_shortest_side, min_dice_size)

    img_array_adaptive = bu.build_dice_array_with_adaptive_color()
    img_array_rgb_gap = bu.build_dice_array_rgb_gap()

    create_image()
