import cv2

image = cv2.imread("G_2.jpg")

if image is None:
    print("Image is not defined")
else:
    shape = str(input("Enter the name of shape : circle , rectangle , line or text : ")).lower()

    if shape == "line":
        pt1 = tuple(map(int,input("enter point-1 (x,y) : ").split(",")))
        pt2 = tuple(map(int,input("enter point-1 (x,y) : ").split(",")))
        color = tuple(map(int,input("enter the rgv color code : ").split(",")))
        thickness = int(input("enter the thickness of line : "))

        cv2.line(image,pt1,pt2,color,thickness)

        show = input("do u want to see the image type Yes either No : ").lower()

        if show == "yes":
            cv2.imshow("line_image",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            cv2.destroyAllWindows()
    elif shape == "rectangle":
        upper_left_point = tuple(map(int , input("enter the upper left point").split(",")))
        down_right_point = tuple(map(int , input("enter the down right point").split(",")))
        color = tuple(map(int,input("enter the rgb color : ").split(",")))
        scaler = int(input("enter the scale value : "))
        thickness = int(input("int thichness of rectangle :"))

        cv2.rectangle(image,upper_left_point,down_right_point,scaler,thickness)
        show = input("do un want to see the image type Yes either No : ").lower()

        if show == "yes":
            cv2.imshow("rectangle_image",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            cv2.destroyAllWindows()
    elif shape == "circle":
        center = tuple(map(int,input("enter the center point value : ").split(",")))
        radius = int(input("ente the radius value : "))
        color = tuple(map(int , input("the rgb color : ").split(",")))
        thickness = int(input("enter the thichkness : "))

        cv2.circle(image,center,radius,color,thickness)
        show = str(input("to see the image enter Yes either No : ").lower())

        if show == "yes":
            cv2.imshow("circle_img",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            cv2.destroyAllWindows()