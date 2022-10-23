import cv2
import pickle



width, height = 54, 27

try:
    with open('CarParkPosition_v2', 'rb') as f:
        positionList = pickle.load(f)
except:
    positionList = []


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        positionList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, postion in enumerate(positionList):
            x1, y1 = position
            if x1 < x < x1+width and y1 < y < y1 + height:
                positionList.pop(i)

    with open('CarParkPosition_v2', 'wb') as f:
        pickle.dump(positionList, f)

while True:
    #cv2.rectangle(img, (50,192), (157,240), (255,0,255), 2)
    img = cv2.imread('ParkingLot_BirdEye.png')
    for position in positionList:
        cv2.rectangle(img, position, (position[0] + width, position[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)