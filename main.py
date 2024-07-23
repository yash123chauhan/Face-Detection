                                            ###-------------------------------------------------------###
                                           #####   REAL   TIME   HUMAN   FACE   DETECTION   SYSTEM   #####
                                            ###-------------------------------------------------------###


## 5  Simple  Steps ##
#--------------------#
#                              [1] -> getting an image

#                                   [2] -> convert it into black and white

#                                       [3] -> getting the cordinates of image via pre-defined algorithm

#                                   [4] -> with the help of cordinates we will draw rectangle

#                              [5] -> and display image



import cv2

from random import randrange as r

#start the webcam

cap = cv2.VideoCapture(0) #rt

# Create the haar cascade

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
    
	# To capture frame-by-frame

	sucess , frame = cap.read() #return true
	
	#Chose an image
	
	#frame=cv2.imread('2.webp')

	# Converting our frame into graying image
	# Because our algorithm can detect only gray image
	
	graying = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Here we are detecting coordinates of the graying image i.e.[x,y,w,h]
	
	facecoordinates = faceCascade.detectMultiScale(
		graying
	)

	# printing number of faces found

	print("Found {0} faces!".format(len(facecoordinates)))

	# Here we draw a rectangle around the faces
	
	for (x, y, w, h) in facecoordinates:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (r(0,256), r(0,256), r(0,256)), 5)


	# Display the resulting frame
	cv2.imshow('face detection', frame)

	key = cv2.waitKey(1)      #to stay frame 
	
	if(key==81 or key==113):
	    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
