import cv2
import datetime

def zoom(frame, zoom_factor):
    h, w, _ = frame.shape
    new_h, new_w = int(h / zoom_factor), int(w / zoom_factor)

    # Calculated the center to crop the frame
    x = w//2 - new_w//2
    y = h//2 - new_h//2

    zoomed = frame[y:y+new_h, x:x+new_w]

    # Resized the cropped frame to the original size
    return cv2.resize(zoomed, (w, h))

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam")
    exit()

# window to attach the trackbar
cv2.namedWindow('Camera')

# rackbar for zooming. 1 = no zoom, 2 = 2x zoom, so on.
cv2.createTrackbar('Zoom', 'Camera', 1, 10, lambda x: None)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
recording = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Geting the zoom value from the trackbar
    zoom_factor = cv2.getTrackbarPos('Zoom', 'Camera')
    if zoom_factor < 1:
        zoom_factor = 1

    if zoom_factor > 1:
        frame = zoom(frame, zoom_factor)

    dt_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, dt_string, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 0, 255), 2)

    cv2.imshow('Camera', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        img_name = f"captured_{dt_string}.jpg".replace(":", "_")
        cv2.imwrite(img_name, frame)
        print(f"Image saved as {img_name}")

    elif key == ord('v'):
        if recording:
            recording = False
            out.release()
            print("Video recording stopped")
        else:
            recording = True
            out = cv2.VideoWriter(f"recorded_{dt_string}.avi".replace(":", "_"),
                                  fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
            print("Video recording started")

    if recording and out is not None:
        out.write(frame)

    elif key == 27:
        break

cap.release()
if out:
    out.release()
cv2.destroyAllWindows()
