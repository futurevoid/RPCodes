import cv2

img = cv2.imread('hehua.jpeg')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('hehua',img)
cv2.imshow('grey',grey)
cv2.imwrite('gray.jpeg',grey)
cv2.waitKey(0)
cv2.destroyAllWindows()