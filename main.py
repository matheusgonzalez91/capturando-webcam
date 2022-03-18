import cv2 as cv

webcam = cv.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        cv.imshow('Matheus', frame)
        key = cv.waitKey(5)
        if key == 27: #esc
            break
    #Salvar imagem
    cv.imwrite('MatheusFoto.png', frame)


webcam.release()
cv.destroyAllWindows()