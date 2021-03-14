from PIL import Image
import os
import cv2


def get_file_NamePathSuffix(fileUrl):
    filepath, tmpfilename = os.path.split(fileUrl)
    shotname, extension = os.path.splitext(tmpfilename)
    return filepath, shotname, extension


g = os.walk('C:/Users/lenovo/Desktop/Desktop')  # Path of the file
for path, d, filelist in g:
    for filename in filelist:
        if filename.endswith('jpg'):
            img_path = os.path.join(path, filename)
            filepath, fileshortname, filesuffix = get_file_NamePathSuffix(img_path)
            nxb_img = Image.open(img_path)
            nxb_label_img = nxb_img.resize((192, 256), Image.NEAREST)
            nxb_label_img.save('C:/Users/lenovo/Desktop/Desktop/' +  '1' + fileshortname  + '.jpg')
