from GUI import *

import os
import shutil

import copyData
from PIL import Image
from imghdr import what

from moviepy.editor import VideoFileClip
from filetype import guess

import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo
#from tkinter.ttk import Progressbar
if __name__ == '__main__':
    print("Start\n")
    app = App() 
    app.master.title('CopyMasterSoftware 1.0')
    app.mainloop()

    #from CopyVideo import *
    #copyObj = copyVideo("C:\\Users\\barbv\\Downloads\\videos free", "C:\\Users\\barbv\\Desktop\\TESTING FOR PI")
    #copyObj.videoTime = 200
    #copyObj.copyWithout()
    #from CopyAudio import *
    #copyObj  = copyAudio("C:\\Users\\barbv\\Downloads\\audio free","C:\\Users\\barbv\\Desktop\\TESTING FOR PI")
    #copyObj.audioTime=50
    #copyObj.copyWithout()

    #import filetype
    #from moviepy.editor import VideoFileClip
    #try:
    #    kind = filetype.guess("C:\\Users\\barbv\\Downloads\\videos free\\Sunset On A Snowy Day.mp4")
    #    print(kind)
    #    if kind != None:
    #        print(kind.extension)
    #    else:
    #        print("None")
    #        raise Exception ('None')
    #    if kind.extension not in ['mp4','m4v','mkv','webm','mov','avi','wmv','mpg','flv']:
    #        print("not in ext")
    #        raise Exception ('OUT')
    #    video = VideoFileClip ("C:\\Users\\barbv\\Downloads\\videos free\\Sunset On A Snowy Day.mp4")#test.txt Pexels Videos 1414757.mp4
    #    print(video.duration)
    #except:
    #    print("Not a video! EXCEPT")

    