import cv2 as cv
import math


def put_text(frame, text):
    return cv.putText(
        frame, text, (100, 100), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3, bottomLeftOrigin=False)


def get_center_point(image_shape):
    return (math.ceil(float(image_shape[0] / 2)), math.ceil(float(image_shape[1] / 2)))


def generate_square_cords(square_size, center_point):
    rectangle_from = (
        int(center_point[1] - square_size / 2),
        int(center_point[0] - square_size / 2)
    )

    rectangle_to = (
        int(center_point[1] + square_size / 2),
        int(center_point[0] + square_size / 2)
    )

    return (rectangle_from, rectangle_to)


def place_square_at_center(image, square_size):
    center_point = get_center_point(image.shape)

    rectangle_from, rectangle_to = generate_square_cords(
        square_size, center_point)

    return cv.rectangle(
        image, rectangle_from, rectangle_to, (0, 0, 255), 2)


def take_pixels_from_square(image, square_size):
    center_point = get_center_point(image.shape)

    rectangle_from, rectangle_to = generate_square_cords(
        square_size, center_point)

    return image[rectangle_from[1] + 2:rectangle_to[1] - 2, rectangle_from[0] + 2:rectangle_to[0] - 2]
