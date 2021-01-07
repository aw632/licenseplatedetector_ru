import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1920)  # width
cap.set(4, 1080)  # height
cap.set(10, 100)  # brightness
########################
frameWidth = 640
frameHeight = 480
numPlatesCascade = cv2.CascadeClassifier("Resources/haarcascade_licence_plate_rus_16stages.xml")
color = (255, 0, 255)
count = 0
########################

assert cap.isOpened(), "file/camera could not be opened!"
while cap.isOpened():
    success, img = cap.read()
    if not success: break
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numPlates = numPlatesCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numPlates:
        area = w * h  # only choose number plates greater than a certain size
        if area > 500:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
            imgRoi = img[y:y+h, x:x+w]

    cv2.imshow("Video", img)
    if (cv2.waitKey(1) & 0xFF ==ord('s')):
        cv2.imwrite("Resources/Scanned/NmPlate_" +str(count)+".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Saved image successfully", (150, 265), cv2.FONT_HERSHEY_COMPLEX, 2, color, 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1