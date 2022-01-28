import os
from PIL import Image
import PIL
image ="Icon_Image\\"
def icon():
    filename = input("Enter the image name ")
    img = Image.open(filename)
    FileName_Save = input("Enter the save file Name ") 
    print("png","jpg","ico","and move ")
    type = input("Enter the type of image ") 
    Save_Image_Path = image + FileName_Save + "." + type 
    icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (255, 255)]
    img.save(Save_Image_Path, sizes=icon_sizes)
if(os.path.isdir(image)==True):
    icon()
else:
    print("Not Found dir")
    try:
        os.mkdir(image)
        icon()
    except (RuntimeError, TypeError, NameError)as e:
        print("Error ")
        print("Error ")
        print("Error ")
        print("Error ")
        print(e)
        print("Exit code ")
        exit()