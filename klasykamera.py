
import cv2

class Kamera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
    def uruchom(self):
        while True:
            #frame = cam.read()[1]
            frame = self.camera.read()[1]
            cv2.imshow('OKNO', frame)
            if cv2.waitKey(10) == ord('q'):
                break

    @staticmethod
    def test():
        print("Test")


Kamera().camera
Kamera().uruchom()
Kamera().test()