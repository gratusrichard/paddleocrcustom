import os
import random
from PIL import Image
path = '/home/gratus/Downloads/dataset'

outputdir = '/media/gratus/HDD/TRS/paddlecustom/maindataset'


dirs = os.listdir(path)


textfile = '/media/gratus/HDD/TRS/paddlecustom/label.txt'

with open(textfile, 'a') as file:
    for dir in dirs:
        picdirpath = os.path.join(path, dir)
        pics = os.listdir(picdirpath)
        i =0
        for pic in pics:
            pic_path = os.path.join(picdirpath, pic)

            image = Image.open(pic_path)
            savepath  = os.path.join(outputdir,f'{i}'+dir+".jpeg")
            image.save(savepath,format="JPEG")
            file.write(savepath + '\t' + dir + '\n')
            i+=1

with open(textfile, 'r') as file:
    lines = file.readlines()

random.shuffle(lines)

with open(textfile, 'w') as file:
    file.writelines(lines)
