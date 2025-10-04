import cv2

image = cv2.imread("G_2.jpg")

if image is None:
    print("oops! image not found")
else:
    text = "hllo python programmers"
    font = cv2.FONT_HERSHEY_COMPLEX
    place = (50,550)
    scale = 1.0
    color = (255,0,0)
    thickness = 3

    cv2.putText(image,text,place,font,scale,color,thickness)

    cv2.imshow("putText",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

