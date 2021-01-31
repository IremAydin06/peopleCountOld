import cv2

vid = cv2.VideoCapture('C:\\Users\\Lenovo\\Desktop\\UZAKTAN EĞİTİM\\4.SINIF\\BİTİRME PROJESİ\\body.mp4')
body_cascade = cv2.CascadeClassifier('C:\\Users\\Lenovo\\Desktop\\haarcascade\\haarcascade_fullbody.xml')

while True:
    ret,frame = vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    bodies = body_cascade.detectMultiScale(gray,1.4,2)

    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(y + h, x + w),(0,0,255),3)

    cv2.imshow("video",frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
vid.release()
cv.destroyAllWindows()