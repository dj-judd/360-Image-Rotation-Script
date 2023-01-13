# 360-Image-Rotation-Script

## Description

This script is useful for rotating a lot of images based on a single 360° rotation. For example, the tripod was uneven when a group of 360° photos was taken. You can also use it to manipulate just 1 image at a time as well.

## How to run
### With the menu

You can just call the script and put the values in 1 by 1.

`python3 360imageRotator.py`


### Everything from the terminal
If you want to enter all the values in the terminal though:

python3 360imageRotator.py "/path/to/image directory/" "file extention of original images" "/path/to/destination directory/" YAW PITCH ROLL

Example:

`python3 360imageRotator.py "/path/to/images/" ".jpg" "/path/to/destination/" 90 0 1`
