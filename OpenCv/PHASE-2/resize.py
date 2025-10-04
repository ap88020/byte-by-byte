import cv2

image = cv2.imread("G_2.jpg")

if image is None:
    print("Image not found")
else:
    resized = cv2.resize(image,(300,300))
    cv2.imshow("Original_image",image)
    cv2.imshow("resize_output",resized)
    cv2.imwrite("resize.png",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

