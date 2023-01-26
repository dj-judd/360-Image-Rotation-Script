import os
import sys
import cv2
import glob

from pathlib import Path
from equirectRotate import EquirectRotate, pointRotate


def rotateMagic(src_path: str, originalFileName:str, dest_dir: str, pitch: int, yaw: int, roll:int):

    startingMsg = "Rotation Starting on: {}".format(originalFileName)
    largeFileNoticeMsg = "*Larger files will take a long time"
    
    if len(startingMsg) > len(largeFileNoticeMsg):
        lineSeperatorLength = len(startingMsg)
    else:
        lineSeperatorLength = len(largeFileNoticeMsg)
    
    print()
    print("~" * lineSeperatorLength)
    print(startingMsg)
    print(largeFileNoticeMsg)
    print("~" * lineSeperatorLength)


    src_image = cv2.imread(src_path)    
    h, w, c = src_image.shape

    
    # rotate source image
    equirectRot1 = EquirectRotate(h, w, (pitch, yaw, roll))
    rotated_image = equirectRot1.rotate(src_image)
    

    imageSaveSuccess = cv2.imwrite(dest_dir, rotated_image)
    
    if imageSaveSuccess:
        print("\nSuccess!\n\nRotation complete. New image saved to:\n" + dest_dir + "\n")


def pathIsAFile (src_path: str) -> bool:

    # Check if the source path is a file or a folder
    src_path = Path(src_path)
    if src_path.is_file():
        return True

    elif src_path.is_dir():
        return False

    else:
        errorMessage = f"\"{src_path}\" is not a valid file or directory"
        print()
        print("!" * len(errorMessage))
        print(errorMessage)
        print("!" * len(errorMessage))
        print()
        exit()


def folderProcessing(src_path: str, fileExtentionTarget: str, original_dest_dir: str, pitch: int, yaw: int, roll:int):

    processingNoticeMsg = "Processing all images with the {} extention.".format(fileExtentionTarget)
    
    print(("\n" + "*" * len(processingNoticeMsg)) * 2)
    print("Folder detected")
    print(processingNoticeMsg)
    print("*" * len(processingNoticeMsg) + "\n" + "*" * len(processingNoticeMsg))
    
    
    dest_dir = original_dest_dir
    
    for filePath in glob.glob(src_path + "*" + fileExtentionTarget):
        
        originalFileName = filePath.replace(src_path, "")
        
        print()
        print(originalFileName)
        print()
        
        dest_dir = original_dest_dir + originalFileName
        rotateMagic(filePath, originalFileName, dest_dir, pitch, yaw, roll)
        
        dest_dir = original_dest_dir
    
    
    finishingUpMsg = "All files saved to {}".format(original_dest_dir)
    
    print(("\n" + "*" * len(finishingUpMsg)) * 2)
    print("\nBatch Rotation complete.")
    print(finishingUpMsg)
    print(("\n" + "*" * len(finishingUpMsg)) * 2)
    print()

#def getOriginalFilename(

# Checking for arguments passed from command line / terminal
if len(sys.argv) > 1:
    src_path = str(sys.argv[1])
    fileExtentionTarget = str(sys.argv[2])
    dest_dir = str(sys.argv[3])
    pitch = int(sys.argv[4])
    yaw = int(sys.argv[5])
    roll = int(sys.argv[6])
    
    if pathIsAFile(src_path):
    
        originalFileName = os.path.basename(src_path)
        
        print("Debug Mode:")
        print()
        print(src_path)
        print()
        print(fileExtentionTarget)
        print()
        print(originalFileName)
        print()
        print(dest_dir)
        print()
        print("Pitch: {}, Yaw: {}, Roll: {}".format(pitch, yaw, roll))
        print()
        print()
        
        rotateMagic(src_path, originalFileName, dest_dir, pitch, yaw, roll)
    
    else:
        folderProcessing(src_path, fileExtentionTarget, dest_dir, pitch, yaw, roll)

# User Input Menu
else:
    # Ask the user for the path to the source and destination image or folder
    src_path = str(input("Enter the path to the source image or folder: "))
    fileExtentionTarget = str(input("Enter the file extention you are targeting: "))
    dest_dir = str(input("Enter the path to the destination folder: "))

    # Ask the user for the rotation angle in degrees
    pitch = int(input("Enter the change in pitch rotation angle in degrees: "))
    yaw = int(input("Enter the change in yaw rotation angle in degrees: "))
    roll = int(input("Enter the change in roll rotation angle in degrees: "))
   
    originalFileName = os.path.basename(src_path)
   
    if pathIsAFile(src_path):
        rotateMagic(src_path, originalFileName, dest_dir, pitch, yaw, roll)
    
    else:
        folderProcessing(src_path, fileExtentionTarget, dest_dir, pitch, yaw, roll)