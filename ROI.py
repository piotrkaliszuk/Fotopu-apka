
def wykrywacz_ruchu():
    import cv2
    import datetime
    import os

    img_counter = 1
    path = '/home/piotrek/PycharmProjects/pythonProject2/Zrzuty'

    def takePhoto():
        format = now.strftime("%m%d%Y%H%M%S")
        frame = cam.read()[1]
        dt = now.strftime("%m/%d/%Y %H:%M:%S")
        cv2.putText(frame, "{}".format(dt), (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        img = f"SKW{format}.png"
        print(f'Zapisano zrzut ekranu: {img}')
        cv2.imwrite(os.path.join(path, img), frame)
        print(f'Zapisano {img_counter} zrzut!')

    def frameDiff(It0, It1, It2):
        dI1 = cv2.absdiff(It2, It1)
        dI2 = cv2.absdiff(It1, It0)
        return cv2.bitwise_and(dI1, dI2)

    def regionOfInterest():
        x1 = 50
        y1 = 80
        x2 = 600
        y2 = 400
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'Pole wykrywania ruchu', (x1 + 5, y1 - 10), font, 1, (0, 255, 0), 3)
        return x1, y1, x2, y2

    cam = cv2.VideoCapture(0)
    cam.set(3, 800)
    cam.set(4, 600)
    cv2.flip
    nazwa_okna = "Wykrywacz ruchu"
    motionCounter = 0
    lastUploaded = datetime.datetime.now()
    t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    while True:
        ruch = False
        now = datetime.datetime.now()
        t_minus = t
        t = t_plus
        frame = cam.read()[1]
        t_plus = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        #threshhld = cv2.threshold(frameDiff(t_minus,t,t_plus),10,255,cv2.THRESH_BINARY)[1]
        threshhld = cv2.threshold(frameDiff(t_minus, t, t_plus), 10, 255, cv2.THRESH_BINARY)[1]
        threshhld = cv2.dilate(threshhld, None, iterations=2)
        (cnts, _) = cv2.findContours(threshhld.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        x1, y1, x2, y2 = regionOfInterest()

        for x in cnts:
            if cv2.contourArea(x) < 800:
                continue
            (x, y, w, h) = cv2.boundingRect(x)
            if (y > y1 and y < y2) and (x > x1 and x < x2):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
                ruch = True
        format = now.strftime("%m/%d/%Y %H:%M:%S")
        cv2.putText(frame, "{}".format(format), (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        if ruch == True:
            if (now - lastUploaded).seconds >= 5.0:
                motionCounter += 1
                if motionCounter >= 5:
                    takePhoto()
                    lastUploaded = now
                    motionCounter = 0
                    img_counter += 1
        else:
            motionCounter = 0

        cv2.imshow(nazwa_okna, frame)

        if cv2.waitKey(10) == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
