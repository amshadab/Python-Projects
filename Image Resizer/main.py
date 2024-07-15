import cv2

#Enter your image path
image=cv2.imread("image.png") 

shape_percent=50


width=int(image.shape[1]*shape_percent/100)
height=int(image.shape[0]*shape_percent/100)

dsize=(width,height)

resize=cv2.resize(image,dsize)
cv2.imshow("Display image",resize)

cv2.waitKey(0)


cv2.destroyAllWindows()