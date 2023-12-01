import cv2
import requests
import threading

def sendImage(frame, name):
    err, image = cv2.imencode(".jpg", frame)
    
    r = requests.post("http://212.237.15.81:8900/send_image/", files={"Images": (str(name)+".jpg", image.tobytes(), "image/jpeg")})
    print(r.status_code)

cap = cv2.VideoCapture(0)

multiThreadUpload = True if input("Multi thread upload? ") in ["y", "yes", "Yes", "Y"] else False

name = 0
while(True):
    ret, frame = cap.read(0)
    if multiThreadUpload:
        thr = threading.Thread(target=sendImage, args=(frame, name), kwargs={})
        thr.start()
    else:
        sendImage(frame, name)
    name += 1
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

