import cv2
import pickle
import cvzone
import numpy as np

#video
cap = cv2.VideoCapture("Park_BirdEye.mp4")


with open('CarParkPosition_v2', 'rb') as f:
    positionList = pickle.load(f)
width, height = 54, 27

def checkParkAvailablility(imgProcessed):

    availability = 0

    for position in positionList:
        x, y = position
        imgCrop = imgProcessed[y:y+height, x:x+width]
#        cv2.imshow(str(x*y), imgCrop)

        count = cv2.countNonZero(imgCrop)

        if count < 220:
            color = (0,255,0)
            thickness = 3
            availability += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, position, (position[0] + width, position[1] + height), color, thickness)
        cvzone.putTextRect(img, None, (x,y+height-3), scale=1, thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f'Available: {availability}/{len(positionList)}', (50, 50), scale=2, thickness=2, offset=5, colorR=(0, 200, 0))


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3,3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3,3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)


    checkParkAvailablility(imgDilate)
    #for position in positionList:
    #    cv2.rectangle(img, position, (position[0] + width, position[1] + height), (255, 0, 255), 2)

    cv2.imshow("Parking Status", img)
#    cv2.imshow("ImgBlur", imgBlur)
#    cv2.imshow("ImgThreshold", imgThreshold)
#    cv2.imshow("ImgMedian", imgMedian)
    i = cv2.waitKey(15) & 0xff  # Press 'ESC' for exiting video
    if i == 27:
        break
