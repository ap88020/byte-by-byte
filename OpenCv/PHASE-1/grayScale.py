import cv2

image = cv2.imread("PHASE-1/G_2.jpg")

if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray_image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("image could not found")

