from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time


resX = 500
resY = 300
avg = None
es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 4))

# Start the camera and get it ready
camera = PiCamera()
camera.resolution = (resX, resY)
camera.framerate = 30

# Convert the output format
rawCapture = PiRGBArray(camera, size=(resX, resY))
time.sleep(5)
rawCapture.truncate(0)

for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame = f.array
    # Adjust the frame size, convert the image to a grayscale image and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    # Initialize it if the average frame is None
    if avg is None:
        print ("[INFO] starting background model...")
        avg = gray.copy().astype("float")
        rawCapture.truncate(0)
        continue
    
    cv2.accumulateWeighted(gray, avg, 0.5)
    
    # Calculate difference between current frame and background
    diff = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
    diff = cv2.threshold(diff, 5, 255, cv2.THRESH_BINARY)[1] # Implement threshold binarization
    diff = cv2.dilate(diff, None, iterations=2) # Dilate the morphology
    
    # Display the rectangle
    (contours, _) = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        if cv2.contourArea(c) < 5000: # Only show rectangles larger than threshold
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print(f"x= {x} y= {y} w= {w} h= {h}")
    
    cv2.imshow('contours', frame)
    cv2.imshow('dis', diff)
    
    key = cv2.waitKey(1) & 0xFF
    # Press 'q' to exit the loop
    if key == ord('q'):
        break
    rawCapture.truncate(0)

# Release the camera resource
camera.release()
cv2.destroyAllWindows()