import glob
from importlib.resources import path
import os

# mylist = [f for f in glob.glob("/home/hunter/Documents/Workspace/Python_code/Pymusic/music/*.webm")]
mylist  = []
path    =   "/home/hunter/Documents/Workspace/Python_code/Pymusic/music/*.webm"

for file in glob.glob(path): 
    filename = os.path.basename(file)
    mylist.append(filename)
    
with open("musicList.txt", 'w') as file:
        for row in mylist:
            s = " ".join(map(str, row))
            file.write(s+'\n')