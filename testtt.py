
def kamera():
    import cv2
    import datetime
    import subprocess, sys
    import os

    img_counter = 1

    path = '/home/piotrek/PycharmProjects/pythonProject2/Zrzuty'

    def Zrzut_ekranu():
        img = f"SKW{format}.png"
        print(f'Zapisano zrzut ekranu: {img}')
        cv2.imwrite(os.path.join(path, img), frame)
        print(f'Zapisano {img_counter} zrzut!')

    vid = cv2.VideoCapture(0)

    while (True):
        ret, frame = vid.read()
        font = cv2.FONT_HERSHEY_DUPLEX

        now = datetime.datetime.now()
        dt = now.strftime("%m/%d/%Y %H:%M:%S")
        format = now.strftime("%m%d%Y%H%M%S")

        text = "Praktykant"
        ramka = cv2.rectangle(frame, (50, 50), (600, 400), (0, 0, 255), 3)
        frame = cv2.putText(frame, dt,
                            (00, 30),
                            font, 1,
                            (0, 255, 0),
                            2, cv2.LINE_AA)
        firma = cv2.putText(frame, text, (450, 450), font, 1,
                            (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Kamera', frame)
        k = cv2.waitKey(1)

        if k % 256 == 27:

            break

        if k % 256 == 32:
            Zrzut_ekranu()
            img_counter += 1

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
