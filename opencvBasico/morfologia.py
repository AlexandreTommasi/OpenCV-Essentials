import cv2

img = cv2.imread("piramide.jpg")
img = cv2.resize(img, (500,400))
imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgBlur = cv2.GaussianBlur(imgCinza,(7,7),0)
imgCanny = cv2.Canny(img,50,100)
imgDilat = cv2.dilate(imgCanny,(5,5),iterations=5)
imgErode = cv2.erode(imgCanny,(5,5),iterations=5)
imgOpening = cv2.morphologyEx(imgCanny,cv2.MORPH_OPEN,(5,5))
imgClosing = cv2.morphologyEx(imgCanny,cv2.MORPH_CLOSE,(5,5))
# cv2.imshow("Img original", img)
# cv2.imshow("Img cinza", imgCinza)
# cv2.imshow("Img Blur", imgBlur)
cv2.imshow("Img canny", imgCanny)
cv2.imshow("Img Open", imgOpening)
cv2.imshow("Img Closing", imgClosing)

cv2.waitKey(0)