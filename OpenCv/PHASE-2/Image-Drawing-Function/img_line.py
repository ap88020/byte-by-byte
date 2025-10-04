import cv2 

image = cv2.imread("G_2.jpg")

if image is None:
    print("oops! image not found")
else:
    print("Image loaded successfully")

    pt1 = (50,100)
    pt2 = (300,100)
    color = (245,9,0)
    thickness = 4

    cv2.line(image,pt1,pt2,color,thickness)

    cv2.imshow("line draw",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

