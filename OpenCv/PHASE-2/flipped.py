import cv2

image = cv2.imread("G_2.jpg")

if image is None:
    print("image not defined")
else:
    flipped_horizontal = cv2.flip(image,1)
    flipped_vertical = cv2.flip(image,0)
    flipped_both = cv2.flip(image,-1)

    cv2.imshow("horizontal",flipped_horizontal)
    cv2.imshow("vertical",flipped_vertical)
    cv2.imshow("both",flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

