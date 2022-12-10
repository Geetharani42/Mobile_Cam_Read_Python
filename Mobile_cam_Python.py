import cv2

cam = cv2.VideoCapture(0)
address = #"IP address from IP webcam in mobile app(ex:http://192.168.42.220:8080/video)"
cam.open(address)

while True:
    ret,frame = cam.read()
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1)&0xff==ord('q'):
        break
cv2.destroyAllWindows()
cam.release()
