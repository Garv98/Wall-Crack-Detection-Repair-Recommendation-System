import cv2

url = "http://192.168.1.x:8080/video"  

cap = cv2.VideoCapture(url)

frame_width, frame_height = 640, 480
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('crack_detection_output.avi', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.resize(frame, (frame_width, frame_height))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    crack_highlight = frame.copy()
    crack_highlight[edges > 0] = [0, 0, 255] 

    cv2.imshow("Live Crack Detection", crack_highlight)

    out.write(crack_highlight)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()