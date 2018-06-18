# Document-scanner
This program used some basic function of Opencv to detect a rectangular document and scan it from image. 
The idea of this program is simple. We will look for all the contours in the image and find the largest one which is the boundary of the page in this case. Then we use some transformations to crop the defined document and turn it to desired scanned page
