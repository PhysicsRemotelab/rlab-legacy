import cv2

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break