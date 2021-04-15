import cv2
import logging
import numpy



def processImage(image,debug=False):
    
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # grayscale
    cv2.imwrite("grayed.jpg", gray)
    
    _,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) 
    cv2.imwrite("thresh.jpg",thresh)

    #threshold
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(23,39))
    dilated = cv2.dilate(thresh,kernel,iterations = 5) # dilate
    cv2.imwrite("dilated.jpg", dilated)

    # get contours
    contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 
    # for each contour found, draw a rectangle around it on original image
    idx = 0
    for contour in contours:
        # get rectangle bounding contour
        [x,y,w,h] = cv2.boundingRect(contour)
        if h>1000 and w>300:
            idx+=1
            new_img = image[y:y+h,x:x+w]
            cv2.imwrite(str(idx) + '.png', new_img)
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
  
    # write original image with added contours to disk  

    return image
