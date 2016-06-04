import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# video recorder
cam_w = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH);
cam_h = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT);

cap.set(cv2.cv.CV_CAP_PROP_FPS,30)

print('cam_w', cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
print('cam_h', cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
print('CAP_PROP_FOURCC', int(cap.get(cv2.cv.CV_CAP_PROP_FOURCC)))
print('CAP_PROP_FPS', cap.get(cv2.cv.CV_CAP_PROP_FPS))


fourcc = int(cap.get(cv2.cv.CV_CAP_PROP_FOURCC))
#fourcc = cv2.cv.FOURCC('m','p','4','v')
#fourcc = cv2.cv.CV_FOURCC('X','V','I','D')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,30,(int(cam_w),int(cam_h)))

print('is writer on',bool(out.isOpened))


while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    lower_green = np.array([50,50,50])
    upper_green = np.array([70,255,255])

    lower_red = np.array([0,100,100])
    upper_red = np.array([10,255,255])
     
    lower_yellow= np.array([10,100,100])
    upper_yellow = np.array([30,255,255])    

    # Threshold the HSV image to get only blue colors
##    mask = cv2.inRange(hsv, lower_blue, upper_blue)
##    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask = cv2.inRange(hsv, lower_red, upper_red)
##    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    # record video
    out.write(mask)
    # display video
    cv2.imshow('frame',frame) # the original frame
    cv2.imshow('res',res)     # fuses the detected color to mask         
    cv2.imshow('mask',mask)   # only shows the lower and upper color 

    
    k = cv2.waitKey(5) 
    if k == 27: #press escape key to exit
        break
cap.release() #turn off the cam
out.release()
cv2.destroyAllWindows()
