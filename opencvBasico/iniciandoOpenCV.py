import cv2

### cortar uma imagem utilizando paint do windows

img = cv2.imread('farol.jpg')
dim = cv2.selectROI("Selecione a area de recorte", img, False)
cv2.destroyWindow("Selecione a area de recorte")
#print(dim)
v1 = int(dim[0])
v2 = int(dim[1])
v3 = int(dim[2])
v4 = int(dim[3])
recorte = img[v2:v2+v4,v1:v1+v3]
caminho = "recortes/"
nome_arquivo = input("Digite o nome do arquivo")

cv2.imwrite(f"{caminho}{nome_arquivo}.jpg",recorte)

# cv2.imshow('Imagem', img)
# cv2.imshow('Recorte', recorte)

cv2.waitKey(0)


# Reproduzir um video

# video = cv2.VideoCapture("runners.mp4")

# while True:
#     check,img = video.read()
#     imgRedim = cv2.resize(img, (640,420))
#     cv2.imshow("video",imgRedim)
#     cv2.waitKey(10)




# Abrindo uma imagem

#img = cv2.imread('farol.jpg')
#imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#print(imgCinza.shape)

#cv2.imshow('Imagem', img)
#cv2.imshow("ImagemCinza", imgCinza)
#cv2.waitKey(0)