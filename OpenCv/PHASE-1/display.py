import cv2 

image = cv2.imread("G_2.jpg")

if image is not None:
    cv2.imshow("title",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("some problem ocure")

