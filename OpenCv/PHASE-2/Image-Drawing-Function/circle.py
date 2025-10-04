import cv2

image = cv2.imread("G_2.jpg")

if image is None:
    print("oops image not found")
else:
    print("image loaded successfully")

    radius = 50
    color = (255,267,297)
    thickness = 4

    cv2.circle(image,(260,200),50,color,thickness)

    cv2.imshow("circle image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

