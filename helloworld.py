import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret, frame = cap.read()

    _, black = cv2.threshold(frame, 255, 255, cv2.THRESH_BINARY)

    cv2.putText(black, 'OpenCV', (frame.shape[1] // 2 ,frame.shape[0] // 2),cv2.FONT_HERSHEY_SIMPLEX  , 1, (255,255,255), 2)

    cv2.imshow("hello world", black)

    if cv2.waitKey(1) == 27:
        break

cap.release()
