import cv2
import datetime
import numpy as np
from matplotlib import pyplot as plt


def zoom(frame, zoom_factor):
    h, w, _ = frame.shape
    new_h, new_w = int(h / zoom_factor), int(w / zoom_factor)

    x = w//2 - new_w//2
    y = h//2 - new_h//2

    zoomed = frame[y:y+new_h, x:x+new_w]
    return cv2.resize(zoomed, (w, h))

def custom_sobel_x(image):
    kernel = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    return cv2.filter2D(image, -1, kernel)

def custom_sobel_y(image):
    kernel = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])
    return cv2.filter2D(image, -1, kernel)

def custom_laplacian(image):
    kernel = np.array([
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ])
    return cv2.filter2D(image, -1, kernel)


# def custom_sobel_x(image):
#     height, width = image.shape
#     sobel_x_image = np.zeros((height, width))
    
#     for i in range(1, height - 1):
#         for j in range(1, width - 1):
#             Gx = ((image[i+1, j-1] + 2*image[i+1, j] + image[i+1, j+1]) -
#                   (image[i-1, j-1] + 2*image[i-1, j] + image[i-1, j+1]))
#             sobel_x_image[i, j] = Gx
            
#     return sobel_x_image

# def custom_sobel_y(image):
#     height, width = image.shape
#     sobel_y_image = np.zeros((height, width))
    
#     for i in range(1, height - 1):
#         for j in range(1, width - 1):
#             Gy = ((image[i-1, j+1] + 2*image[i, j+1] + image[i+1, j+1]) -
#                   (image[i-1, j-1] + 2*image[i, j-1] + image[i+1, j-1]))
#             sobel_y_image[i, j] = Gy
            
#     return sobel_y_image

# def custom_laplacian(image):
#     height, width = image.shape
#     laplacian_image = np.zeros((height, width))
    
#     for i in range(1, height - 1):
#         for j in range(1, width - 1):
#             laplacian_pixel = (4 * image[i, j] - image[i-1, j] - image[i+1, j] - image[i, j-1] - image[i, j+1])
#             laplacian_image[i, j] = laplacian_pixel
            
#     return laplacian_image



cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam")
    exit()

# GUI setup - camera and trackbar 'Zoom' value = 1-10
cv2.namedWindow('Camera')
#cv2.createTrackbar('Zoom', 'Camera', 1, 10, lambda x: None)
cv2.waitKey(1) 

# Create Trackbars for Gaussian Blur
# cv2.createTrackbar('Sigma X', 'Camera', 5, 30, lambda x: None)
# cv2.createTrackbar('Sigma Y', 'Camera', 5, 30, lambda x: None)

# Video Recording
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
recording = False

# Load the OpenCV logo.
opencv_logo = cv2.imread('opencv_1.png')
h_logo, w_logo, _ = opencv_logo.shape

# angle = 0  # to store the cumulative rotation angle

# sharp_kernel = np.array([
#     [-1, -1, -1],
#     [-1,  9, -1],
#     [-1, -1, -1]
# ])

sobel_x = False
sobel_y = False
canny_edge = False

cv2.createTrackbar('Kernel Size', 'Camera', 5, 30, lambda x: None)  # for Sobel X and Y
cv2.createTrackbar('Threshold 1', 'Camera', 1, 5000, lambda x: None)  # for Canny
cv2.createTrackbar('Threshold 2', 'Camera', 1, 5000, lambda x: None)  # for Canny

state = None

# Flags for showing the windows
show_windows = False

# main loop
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # zoom_factor = cv2.getTrackbarPos('Zoom', 'Camera')
    # if zoom_factor < 1:
    #     zoom_factor = 1

    # if zoom_factor > 1:
    #     frame = zoom(frame, zoom_factor)

    if sobel_x:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale
        kernel_size = cv2.getTrackbarPos('Kernel Size', 'Camera')
        sobelx = cv2.Sobel(gray_frame, cv2.CV_64F, 1, 0, ksize=kernel_size)
        sobelx_abs = cv2.convertScaleAbs(sobelx)
        frame = cv2.cvtColor(sobelx_abs, cv2.COLOR_GRAY2BGR)
        cv2.imshow('Sobel X', frame)
        
    elif sobel_y:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale
        kernel_size = cv2.getTrackbarPos('Kernel Size', 'Camera')
        sobely = cv2.Sobel(gray_frame, cv2.CV_64F, 0, 1, ksize=kernel_size)
        sobely_abs = cv2.convertScaleAbs(sobely)
        frame = cv2.cvtColor(sobely_abs, cv2.COLOR_GRAY2BGR)
        cv2.imshow('Sobel Y', frame)

        
    elif canny_edge:
        threshold1 = cv2.getTrackbarPos('Threshold 1', 'Camera')
        threshold2 = cv2.getTrackbarPos('Threshold 2', 'Camera')
        edges = cv2.Canny(frame, threshold1, threshold2)
        frame = cv2.merge([edges, edges, edges])
        cv2.imshow('Canny_Edge', frame)



    elif show_windows:
        # Compute the custom Sobel and Laplacian results
        sobel_x_img = custom_sobel_x(frame)
        sobel_y_img = custom_sobel_y(frame)
        laplacian_img = custom_laplacian(frame)

        # Show the windows
        cv2.imshow('Original', frame)
        cv2.imshow('Laplacian', laplacian_img)
        cv2.imshow('Sobel X', sobel_x_img)
        cv2.imshow('Sobel Y', sobel_y_img)


#     # Add a red constant border.
    border_size = 10
    frame = cv2.copyMakeBorder(frame, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=(0, 0, 255))

#    # Ensure the logo isn't larger than the frame. If it is, you might need to resize it.
    if h_logo > frame.shape[0] or w_logo > frame.shape[1]:
        # Calculate the scaling factor for height and width separately
        scale_h = frame.shape[0] / h_logo
        scale_w = frame.shape[1] / w_logo
        
        # Use the smaller scaling factor to ensure the logo fits both dimensions
        scale = min(scale_h, scale_w)
        
        # Resize the logo based on the scale
        new_h, new_w = int(h_logo * scale), int(w_logo * scale)
        opencv_logo = cv2.resize(opencv_logo, (new_w, new_h))
        h_logo, w_logo = new_h, new_w

    # Extract the top left corner ROI from the camera stream just inside the border
    roi = frame[border_size:border_size+h_logo, border_size:border_size+w_logo]


    # Ensure both the roi and the opencv_logo have the same number of channels
    if len(roi.shape) == 2:
        roi = cv2.cvtColor(roi, cv2.COLOR_GRAY2BGR)
    if len(opencv_logo.shape) == 2:
        opencv_logo = cv2.cvtColor(opencv_logo, cv2.COLOR_GRAY2BGR)

    # Blend the logo with the ROI
    blended = cv2.addWeighted(roi, 0.5, opencv_logo, 0.5, 0)
    # Place the blended ROI back into the frame
    frame[border_size:border_size+h_logo, border_size:border_size+w_logo] = blended

    #date/time stamp
    dt_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    y_position = frame.shape[0] - border_size 
    cv2.putText(frame, dt_string, (border_size + 10, y_position), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # Copy Date/Time stamp ROI to the top right corner.
    text_size = cv2.getTextSize(dt_string, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
    timestamp_roi = frame[frame.shape[0] - 10 - text_size[1]:frame.shape[0] - 10, 10:10+text_size[0]]
    x_start = frame.shape[1] - border_size - timestamp_roi.shape[1] - 10
    y_start = border_size 
    frame[y_start:y_start+timestamp_roi.shape[0], x_start:x_start+timestamp_roi.shape[1]] = timestamp_roi

    cv2.imshow('Camera', frame)

    key = cv2.waitKey(10) & 0xFF

    if key == ord('s'):
        state = 's'
        
    # If state is 's' and 'x' is pressed
    elif state == 's' and key == ord('x'):
        sobel_x, sobel_y, canny_edge = True, False, False
        state = None  # Reset state
        
    # If state is 's' and 'y' is pressed
    elif state == 's' and key == ord('y'):
        sobel_x, sobel_y, canny_edge = False, True, False
        state = None  # Reset state
    
    # Direct 'd' key press for Canny edge
    elif key == ord('d'):
        sobel_x, sobel_y, canny_edge = False, False, True

    if key == ord('4'):
        show_windows = not show_windows  # Toggle the state
        
    # if key == ord('c'):
    #     # Flash the screen white when capturing a photo.
    #     cv2.imshow('Camera', np.ones_like(frame) * 255)
    #     cv2.waitKey(100)  # Display white frame for 100ms.

    #     img_name_name = f"captured_{dt_string}.jpg".replace(":", "_")
    #     cv2.imwrite(img_name_name, frame)
    #     print(f"Image saved as {img_name_name}")

    # elif key == ord('e'):
    #      # Take each frame
    #     _, frame = cap.read()
    #     # Convert BGR to HSV
    #     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #     # define range of yellow color in HSV
    #     lower_yellow = np.array([20, 50, 50])   
    #     upper_yellow = np.array([40, 255, 255])
    #     # Threshold the HSV image to get only yellow colors
    #     mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    #     # Bitwise-AND mask and original image
    #     res = cv2.bitwise_and(frame,frame, mask= mask)
    #     cv2.imshow('frame',frame)
    #     cv2.imshow('mask',mask)
    #     cv2.imshow('res',res)
        
    # elif key == ord('r'):

    #     angle += 10  # Increment angle
    #     M = cv2.getRotationMatrix2D((frame.shape[1] / 2, frame.shape[0] / 2), angle, 1)
    #     rotate = cv2.warpAffine(frame, M, (frame.shape[1], frame.shape[0]))
    #     cv2.imshow('Rotated by 10 deg',rotate)
        
    # elif key == ord('t'):
    #      # Take each frame
    #     _, frame = cap.read()
    #     CamHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #     lower = np.array([0, 48, 100], dtype = 'uint8')
    #     upper = np.array([18, 255, 255], dtype = 'uint8')
    #     SkinTresholdHSV = cv2.inRange(CamHSV, lower, upper)
    #     blurredHSV = cv2.blur(SkinTresholdHSV, (3, 3))
    #     ret, thresh = cv2.threshold(blurredHSV, 0, 255, cv2.THRESH_BINARY)
    #     cv2.imshow('thresh', thresh)
    #     cv2.imshow('Cam', CamHSV)

    # elif key == ord('b'):
    #     _, frame = cap.read()
    #     sigmaX = cv2.getTrackbarPos('Sigma X', 'Camera')
    #     sigmaY = cv2.getTrackbarPos('Sigma Y', 'Camera')
    #     kernel_size_x = 2*sigmaX + 1  # Kernel size should be odd
    #     kernel_size_y = 2*sigmaY + 1
    #     blurred = cv2.GaussianBlur(frame, (kernel_size_x, kernel_size_y), sigmaX, sigmaY)
    #     cv2.imshow('Blurred', blurred)
    
    # elif key == ord('s'):

    #     sharpened = cv2.filter2D(frame, -1, sharp_kernel)
    #     cv2.imshow('Sharpened', sharpened)

    # if key == ord('s') + ord('x'):
    #     sobel_x = not sobel_x  # Toggle Sobel X
    #     sobel_y = False
    #     canny_edge = False

    # elif key == ord('s') + ord('y'):
    #     sobel_y = not sobel_y  # Toggle Sobel Y
    #     sobel_x = False
    #     canny_edge = False

    # elif key == ord('d'):
    #     canny_edge = not canny_edge  # Toggle Canny Edge Detection
    #     sobel_x = False
    #     sobel_y = False

    elif key == 27:
        break

cap.release()
if out:
    out.release()
cv2.destroyAllWindows()
