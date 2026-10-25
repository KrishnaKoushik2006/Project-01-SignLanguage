import cv2


class Camera:

    def __init__(self):
        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            raise Exception("Could not open camera.")

    def get_frame(self):
        success, frame = self.camera.read()

        if not success:
            return None

        return frame

    def release(self):
        self.camera.release()
        cv2.destroyAllWindows()