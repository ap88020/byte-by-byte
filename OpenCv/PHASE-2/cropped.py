import cv2

image = cv2.imread("G_2.jpg")

if image is not None:
    cropped = image[100:200 , 50:150]

    cv2.imshow("original_image",image)
    cv2.imshow("croped_image",cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Image is not found")