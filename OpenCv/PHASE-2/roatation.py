import cv2

image = cv2.imread("G_2.jpg")

if image is None:
    print("Image not defined")
else:
    (h,w) = image.shape[:2]
    center = (h//2 , w//2)


    M = cv2.getRotationMatrix2D(center,90,1.0)
    rotate = cv2.warpAffine(image , M , (w,h))

    cv2.imshow("ORIGINALN_IMAGE",image)
    cv2.imshow("Roatate_image",rotate)

    cv2.imwrite("roate.png",rotate)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


