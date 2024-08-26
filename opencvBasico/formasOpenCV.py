import cv2

video = cv2.VideoCapture("runners.mp4")

while True:
    check,img= video.read()
    cv2.rectangle(img,(50,50),(200,200),(255,0,0),5)
    cv2.circle(img,(300,300),50,(0,0,255),-1)
    cv2.line(img,(300,400),(500,300),(0,255,255),2)

    texto = "Piramides do Egito"

    cv2.putText(img,texto,(200,200),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)

    cv2.imshow("Imagem", img)
    cv2.waitKey(10)









# img = cv2.imread("piramide.jpg")

# cv2.rectangle(img,(50,50),(200,200),(255,0,0),5)
# cv2.circle(img,(300,300),50,(0,0,255),-1)
# cv2.line(img,(300,400),(500,300),(0,255,255),2)

# texto = "Piramides do Egito"

# cv2.putText(img,texto,(200,200),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)

# cv2.imshow("Imagem", img)
# cv2.waitKey(0)