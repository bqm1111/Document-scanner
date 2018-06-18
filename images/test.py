import cv2
img=cv2.imread("F:\Python\test.bmp",0)
cv2.namedWindow("winname",0)
cv2.imshow("winname",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
