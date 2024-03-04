import os
import random

path = '/home/gratus/Downloads/dataset'
dirs = os.listdir(path)

with open('/media/gratus/HDD/TRS/paddlecustom/label.txt', 'a') as file:
    for dir in dirs:
        picdirpath = os.path.join(path, dir)
        pics = os.listdir(picdirpath)
        for pic in pics:
            pic_path = os.path.join(picdirpath, pic)
            file.write(pic_path + '\t' + dir + '\n')

# Read the lines from the file
with open('/media/gratus/HDD/TRS/paddlecustom/label.txt', 'r') as file:
    lines = file.readlines()

# Shuffle the lines
random.shuffle(lines)

# Write the shuffled lines back to the file
with open('/media/gratus/HDD/TRS/paddlecustom/label.txt', 'w') as file:
    file.writelines(lines)
