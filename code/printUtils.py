def print_created_image(image_copy, img_array):
    print_img_occurrence(img_array)
    image_copy.show()
    image_copy.save("output/{}.jpg".format(image_name))


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
