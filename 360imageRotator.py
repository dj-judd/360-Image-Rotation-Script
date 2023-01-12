import os
import sys
import cv2

from equirectRotate import EquirectRotate, pointRotate


def rotateMagic(src_path: str, dest_path: str, pitch: int, yaw: int, roll:int):

    print("Rotation Starting\nLarger files will take a long time.")

    src_image = cv2.imread(src_path)
    
    # print("src_image is",type(src_image))
    
    h, w, c = src_image.shape
    
    # print("h is", type(h))
    # print("w is",type(w))
    # print("c is",type(c))
    
    # rotate source image
    equirectRot1 = EquirectRotate(h, w, (pitch, yaw, roll))
    rotated_image = equirectRot1.rotate(src_image)
    
    cv2.imwrite(dest_path, rotated_image)
    
    print("Rotation done and saved to:", dest_path)



# Checking for arguments passed from command line / terminal
if len(sys.argv) > 1:
    src_path = str(sys.argv[1])
    dest_path = str(sys.argv[2])
    pitch = int(sys.argv[3])
    yaw = int(sys.argv[4])
    roll = int(sys.argv[5])


    rotateMagic(src_path, dest_path, pitch, yaw, roll)



else:
    # Ask the user for the path to the source and destination image or folder
    src_path = str(input("Enter the path to the source image or folder: "))
    dest_path = str(input("Enter the path to the destination image or folder: "))
    

    # Ask the user for the rotation angle in degrees
    pitch = int(input("Enter the change in pitch rotation angle in degrees: "))
    yaw = int(input("Enter the change in yaw rotation angle in degrees: "))
    roll = int(input("Enter the change in roll rotation angle in degrees: "))
    
    rotateMagic(src_path, dest_path, pitch, yaw, roll)

    # # Check if the source path is a file or a folder
    # if src_path.is_file():
        # # Ask the user for the output path
        # output_path = input("Enter the path to the output image: ")
        # output_path = Path(output_path)

        # # Perform the rotation and reprojection
        # rotate_and_reproject_image(src_path, output_path, angle)
    # elif src_path.is_dir():
        # process_folder(src_path, angle)
    # else:
        # print(f"{src_path} is not a valid file or directory.")
        