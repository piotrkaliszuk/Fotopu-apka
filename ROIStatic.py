def wykrywacz_ruchu_statyczny():
    import cv2
    import datetime
    from time import sleep
    import os
    from smstest import wyslijsms
    import serial
    from smstest import send_at


    ser = serial.Serial("/dev/ttyS0",
                        baudrate=115200,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=1
                        )


    cam = cv2.VideoCapture(0)
    cam1 = cam
    cam.set(3, 800)
    cam.set(4, 600)
    cam1.set(3, 800)
    cam1.set(4, 600)
    cam.set(5, 30)
    cam1.set(5, 30)
    cv2.flip
    nazwa_okna = "Wykrywacz ruchu"

    motionCounter = 0
    lastUploaded = datetime.datetime.now()

    tło = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    img_counter = 1
    licznik = 0
    path = '/home/piotrek/PycharmProjects/pythonProject2/Zrzuty'

    def takePhoto():
        format = now.strftime("%m%d%Y%H%M%S")
        frame = cam.read()[1]
        dt = now.strftime("%m/%d/%Y %H:%M:%S")
        cv2.putText(frame, "{}".format(dt), (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        img = f"Praktyki{format}.png"
        print(f'Zapisano zrzut ekranu: {img}')
        cv2.imwrite(os.path.join(path, img), frame)
        print(f'Zapisano {img_counter} zrzut!')

    def regionOfInterest():
        x1 = 50
        y1 = 80
        x2 = 600
        y2 = 400
        cv2.rectangle(frame0, (x1, y1), (x2, y2), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame0, 'Pole wykrywania ruchu', (x1 + 5, y1 - 10), font, 1, (0, 255, 0), 3)
        return x1, y1, x2, y2

    sms = True
    while True:
        ruch = False

        now = datetime.datetime.now()
        ret0, frame0 = cam.read()
        ret1, frame1 = cam1.read()
        t_plus = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
        t_plus = cv2.GaussianBlur(t_plus, (21, 21), 0)
        cv2.imshow('WykrywaczS', t_plus)

        odejmowanie = cv2.absdiff(tło, t_plus)

        threshhld = cv2.threshold(odejmowanie, 70, 255, cv2.THRESH_BINARY)[1]
        threshhld = cv2.dilate(threshhld, None, iterations=2)
        cv2.imshow("odejmowanie", odejmowanie)
        cv2.imshow("threshhld", threshhld)
        cnts = cv2.findContours(threshhld.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        x1, y1, x2, y2 = regionOfInterest()
        for x in cnts:
            if cv2.contourArea(x) < 1000:
                continue
            (x, y, w, h) = cv2.boundingRect(x)
            if (y > y1 and y < y2) and (x > x1 and x < x2):
                cv2.rectangle(frame0, (x, y), (x + w, y + h), (0, 0, 255), 3)
                ruch = True

        format = now.strftime("%m/%d/%Y %H:%M:%S")
        cv2.putText(frame0, "{}".format(format), (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        if ruch == True:
            if (now - lastUploaded).seconds >= 3.0:
                motionCounter += 1
                if motionCounter >= 1:
                    takePhoto()
                    lastUploaded = now
                    motionCounter = 0
                    img_counter += 1

            if sms == True:
                wyslijsms(512241743, "Wykryto ruch!", ser)
                sms == False

        else:
            motionCounter = 0

        cv2.putText(frame0, 'Entries:'"{}".format(licznik), (x2 - 70, y2 + 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        if ruch == True:
            if (now - lastUploaded).seconds >= 3.0:
                motionCounter += 1
                if motionCounter >= 1:
                    licznik += 1
                    lastUploaded = now
                    motionCounter = 0
        else:
            motionCounter = 0

        cv2.imshow(nazwa_okna, frame0)

        if cv2.waitKey(10) == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
wykrywacz_ruchu_statyczny()
