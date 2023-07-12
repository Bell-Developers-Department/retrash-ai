import cv2 as cv


class CameraController():
    def record_camera(self, camera_number: int):
        return cv.VideoCapture(camera_number)

    def read_frame(self, capture):
        return capture.read()

    def show_frame(self, title, frame):
        cv.imshow(title, frame)

    def wait_key(self):
        return cv.waitKey(25) & 0xFF
