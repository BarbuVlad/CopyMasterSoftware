import tkinter as tk
from tkinter import filedialog
from os import getcwd
from tkinter.messagebox import showinfo
#from tkinter.ttk import Progressbar

from copyData import copyData
from CopyImage import copyImage
from CopyVideo import copyVideo
class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N + tk.S + tk.E + tk.W)
        self.createWidgets()
        

    #---file path methods--------------------
    def setSource(self):
        dirPath = tk.filedialog.askdirectory(initialdir=getcwd())
        self._sourceLocation.set(dirPath)
    def setTarget(self):
        dirPath = tk.filedialog.askdirectory(initialdir=getcwd())
        self._targetLocation.set(dirPath)
    #----------------------------------------

    #---Check buttons methods----------------
    def setSuffix(self):
        if self.entrySuffix.cget("state") == "disabled":
            self.entrySuffix.config(state=tk.NORMAL)
        elif self.entrySuffix.cget("state") == "normal":
            self.entrySuffix.config(state=tk.DISABLED)

    def setPrefix(self):
        if self.entryPrefix.cget("state") == "disabled":
            self.entryPrefix.config(state=tk.NORMAL)
        elif self.entryPrefix.cget("state") == "normal":
            self.entryPrefix.config(state=tk.DISABLED)

    def setDateMod(self):
        if self.entryDateMod.cget("state") == "disabled":
            self.entryDateMod.config(state=tk.NORMAL)
        elif self.entryDateMod.cget("state") == "normal":
            self.entryDateMod.config(state=tk.DISABLED)

    def setDateCre(self):
        if self.entryDateCre.cget("state") == "disabled":
            self.entryDateCre.config(state=tk.NORMAL)
        elif self.entryDateCre.cget("state") == "normal":
            self.entryDateCre.config(state=tk.DISABLED)

    def setFileSize(self):
        if self.entryFileSize.cget("state") == "disabled":
            self.entryFileSize.config(state=tk.NORMAL)
        elif self.entryFileSize.cget("state") == "normal":
            self.entryFileSize.config(state=tk.DISABLED)

    #-----------------------------------------
    #---Drop menu size methods
    def setKB(self):
        self.sizeString.set("KB")
    def setMB(self):
        self.sizeString.set("MB")
    def setGB(self):
        self.sizeString.set("GB")

    #-----------------------------------------
    #---Selective options methods-------------
    #---disable the rest functions
    def _disableImage(self):
        self.entryImageSize.delete(0,len(self.entryImageSize.get()))
        self.entryImageSize.config(state=tk.DISABLED)
        self.checkImageSizePix.deselect()
        self.checkImageSizePix.config(state=tk.DISABLED)
        self.checkImage.deselect()
        self.checkImage.config(state=tk.DISABLED)
    def _enableImage(self):
        self.checkImage.config(state=tk.NORMAL)

    def _disableVideo(self):
        self.entryVideoLength.delete(0,len(self.entryVideoLength.get()))
        self.entryVideoLength.config(state=tk.DISABLED)
        self.checkVideoLength.deselect()
        self.checkVideoLength.config(state=tk.DISABLED)
        self.checkVideo.deselect()
        self.checkVideo.config(state=tk.DISABLED)
    def _enableVideo(self):
        self.checkVideo.config(state=tk.NORMAL)
    #--------
    def setImageSize(self):
        if self.checkImageSizePix.cget("state") == "disabled":
            self.checkImageSizePix.config(state=tk.NORMAL)
            self._disableVideo()#copy ONLY images
        elif self.checkImageSizePix.cget("state") == "normal":
            self.checkImageSizePix.config(state=tk.DISABLED)
            self.checkImageSizePix.deselect()
            self.entryImageSize.config(state=tk.DISABLED)
            self._enableVideo()#make copy ONLY video possible

    def setImageSizePix(self):
        if self.entryImageSize.cget("state") == "disabled":
            self.entryImageSize.config(state=tk.NORMAL)
        elif self.entryImageSize.cget("state") == "normal":
            self.entryImageSize.delete(0,len(self.entryImageSize.get()))
            self.entryImageSize.config(state=tk.DISABLED)
            
    def setVideo(self):
        if self.checkVideoLength.cget("state") == "disabled":
            self.checkVideoLength.config(state=tk.NORMAL)
            self._disableImage()#copy ONLY video
        elif self.checkVideoLength.cget("state") == "normal":
            self.checkVideoLength.config(state=tk.DISABLED)
            self.checkVideoLength.deselect()
            self.entryVideoLength.config(state=tk.DISABLED)
            self._enableImage()#make copy ONLY image possible

    def setVideoLength(self):
        if self.entryVideoLength.cget("state") == "disabled":
            self.entryVideoLength.config(state=tk.NORMAL)
        elif self.entryVideoLength.cget("state") == "normal":
            self.entryVideoLength.delete(0,len(self.entryVideoLength.get()))
            self.entryVideoLength.config(state=tk.DISABLED)
    #-----------------------------------------
    #---Advanced options methods--------------
    def setFileLog(self):
        if self.LogFileLocButton.cget("state") == "disabled":
            self.LogFileLocButton.config(state=tk.NORMAL)
        elif self.LogFileLocButton.cget("state") == "normal":
            self.LogFileLocButton.config(state=tk.DISABLED)
    #-----------------------------------------

    #---Copy process methods------------------
    def startCopy(self):
        #instantiate an copy object
        if self._intImage.get() == 1:
            copyObject = copyImage()#copy only images
        elif self._intVideo.get() == 1:
            copyObject = copyVideo()
        else:
            copyObject = copyData()

        #Assign values to copyObject atributes
            #Assign source and destination 
        if self._sourceLocation.get() == "":
            showinfo('Source error', 'No source location was given!')
            return
        if self._targetLocation.get() == "":
            showinfo('Target error', 'No target location was given!')
            return

        copyObject.source = self._sourceLocation.get()
        copyObject.target = self._targetLocation.get()

            #Assign General options##################################
        if self._intSuffix.get() == 1 and self.entrySuffix.get()!="":
            copyObject.suffix = self.entrySuffix.get()
        if self._intPrefix.get() == 1 and self.entryPrefix.get()!="":
            copyObject.prefix = self.entryPrefix.get()

        if self._intDateMod.get() == 1 and self.entryDateMod.get()!="":
            #verify date format is corect 
            dateFormated = self._verifyDateFormat(self.entryDateMod.get())
            if dateFormated != False:
                copyObject.dateCreated = dateFormated
            else:
                showinfo('Date format error', 'Date must be in format: DD MM YYYY or DD-MM-YYYY or DD/MM/YYYY')
                return
        if self._intDateCre.get() == 1 and self.entryDateCre.get()!="":
            #verify date format is corect 
            if self._verifyDateFormat(self.entryDateCre.get()) == True:
                copyObject.dateModified = self.entryDateCre.get()
            else:
                showinfo('Date format error', 'Date must be in format: DD MM YYYY or DD-MM-YYYY or DD/MM/YYYY')
                return

        if self._intFileSize.get() == 1 and self.entryFileSize.get()!="":
            #change to bytes
            sizeStr = self.entryFileSize.get()
            try:
                sizeInt=int(sizeStr)
                if self.sizeString.get()=='KB':
                   copyObject.fileSize = sizeInt*1000
                elif self.sizeString.get()=='MB':
                    copyObject.fileSize = sizeInt*1000*1000
                elif self.sizeString.get()=='GB':
                    copyObject.fileSize = sizeInt*1000*1000*1000
                print(copyObject.fileSize)
            except ValueError:
                showinfo("Value error","File size must be a number!")
                return
            
            #Assign Selective options################################
        if self._intImageSize.get()==1 and self.entryImageSize.get()!="":
            #check image size format:
            sizeFormated = self._verifyImageSize(self.entryImageSize.get())# False or (width, height)
            if sizeFormated !=False:
                copyObject.imageSize = sizeFormated

        if self._intVideoLength.get()==1 and self.entryVideoLength.get()!="":
            time_seconds = self._verifyVideoTime(self.entryVideoLength.get())# False or no_of_seconds
            if time_seconds !=False:
                copyObject.videoTime = time_seconds
            else:
                showinfo("Value error","Video time must be in format: hours:minutes:seconds\nFor exemple: 00:05:30 = 5 minutes and 30 seconds")
            #Assign Advanced options#################################
             #Overwrite
        if self._intOverwrite.get()==1:
            copyObject.overwrite=True
        else:
            copyObject.overwrite=False

        #Copy with/without folder structure
        if self._intFolderStructure.get() == 1: 
            try:
                copyObject.copyWithout()
            except Exception as e:
                print(e)
                showinfo("Error", "Error at copy!")
        else:
            try:
                copyObject.copyWithStructure()
            except Exception as e:
                print(e)
                showinfo("Error", "Error at copy!")



#******Verify methods*********************************************
    def _verifyDateFormat(self, dateString):
        #must be in format dd-mm-yyyy or dd/mm/yyyy or dd mm yyyy
        dateString=dateString.replace('-', ' ')
        dateString=dateString.replace('/', ' ')
        
        from re import compile
        pattern = compile(r'\d\d\s\d\d\s\d\d\d\d(\s*)')#xx xx xxxx 
        if pattern.match(dateString) !=None:
            return True#dateString
        else:
            return False

    def _verifyImageSize(self, sizeImageString):
        sizeImageString = sizeImageString.replace(' ', '')#erase white space
        sizeImageString = sizeImageString.split('x')#['number', 'number']
        try:
            if len(sizeImageString)>2:
                raise Exception('Invalid format')
            sizeTuple = (int(sizeImageString[0]), int(sizeImageString[1]))#(number, number)=(width, height)
            return sizeTuple
        except:
            showinfo("Invalid format", "The format for image size must be: pixels x pixels")
            return False

    def _verifyVideoTime(self, videoTimeString):
        videoTimeString = videoTimeString.replace(' ','')#erase whitespace
        #regex
        from re import compile
        pattern = compile(r'\d\d:\d\d:\d\d')
        if pattern.match(videoTimeString) != None:
            #calculate the no. of seconds
            videoTimeString=videoTimeString.split(':')#['hours', 'minutes', 'seconds']
            return int(videoTimeString[0])*3600 + int(videoTimeString[1])*60 + int(videoTimeString[2])
        else:
            return False

    #-----------------------------------------
    def createWidgets(self):
        #-----Resizeable global-----#
        top = self.winfo_toplevel()#“top levelwindow” child al Application, si parant al tuturor widget-urilor
        top.config(background='#1a1a1a')
        top.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17), weight=1)#linia 0 1 2 3... a aplicatiei este resizeable
        top.columnconfigure((0,1,2,3), weight=1)#coloana 0 1 2 3 a aplicatiei este resizeable
        #S-----Resizeable global-----#
        

        #-----Resizeable pe linii/coloane-----#
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17), weight=1)#linia 0,1,2.... a aplicatiei este resizeable
        self.columnconfigure((0,1,2,3), weight=1)#coloana 0,1,2 a aplicatiei este resizeable
        #S-----Resizeable pe linii/coloane-----#

        #Source Frame-----------------------------------------------------------------------
        self.sourceFrame = tk.Frame(top, background='#1a1a1a', height = 100, width=100)
        self.sourceFrame.grid(row=0, column=0,  columnspan=2,rowspan=2, sticky=tk.W+ tk.E+ tk.N + tk.S)

        self.sourceButton = tk.Button(top, text='Set source location', background='#598585', command = self.setSource)# #476b6b
        self.sourceButton.grid(row=0, column=0,  columnspan=2, sticky=tk.W+ tk.E+ tk.N + tk.S)
        self.sourceButton.config(font=("Courier", 15,"bold"),activebackground='#486b6b')
        #Location Text
        self._sourceLocation = tk.StringVar()
        self._sourceLocation.set("")
        self.sourceLabel = tk.Label(top, textvariable=self._sourceLocation,background='#000000', fg='#ffffff', height =5,wraplength=200)
        self.sourceLabel.grid(row=1, column=0,  columnspan=2, sticky=tk.W+ tk.E+ tk.N, padx=2, pady=2)

        #Target Frame-----------------------------------------------------------------------
        self.targetFrame = tk.Frame(top, background='#1a1a1a', height = 100, width=100)
        self.targetFrame.grid(row=0, column=2,  columnspan=2,rowspan=2, sticky=tk.W+ tk.E+ tk.N + tk.S)
        
        self.targetButton = tk.Button(top, text='Set target location',background='#598585', command =self.setTarget)
        self.targetButton.grid(row=0, column=2,  columnspan=2, sticky=tk.W+ tk.E+ tk.N+tk.S)
        self.targetButton.config(font=("Courier", 15,"bold"),activebackground='#486b6b')
        #Location Text
        self._targetLocation = tk.StringVar()
        self._targetLocation.set("")
        self.targetLabel = tk.Label(top, textvariable=self._targetLocation,background='#000000', fg='#ffffff', height =5,wraplength=200)
        self.targetLabel.grid(row=1, column=2,  columnspan=2, sticky=tk.W+ tk.E+ tk.N, padx=2, pady=2)

        #General Options Frame----------------------------------------------------------------------------
        self.optionsFrame = tk.Frame(top, background='#1a1a1a', height = 100, width=100)
        self.optionsFrame.grid(row=2, column=0,  columnspan=4,rowspan=2, sticky=tk.W+ tk.E+ tk.N + tk.S)

        #Opetions text
        self.optionsLabel = tk.Label(top, text="General options",background='#000000', fg='#ffffff')
        self.optionsLabel.grid(row=2, column=0,  columnspan=4, sticky=tk.W+ tk.E+ tk.N+tk.S)
        self.optionsLabel.config(font=("Courier", 15))

        #widgets for options
        #Check suffix
        self._intSuffix = tk.IntVar()
        self.checkSuffix = tk.Checkbutton(top, text='Copy files with suffix: ',command=self.setSuffix, variable=self._intSuffix)
        self.checkSuffix.grid(row=3, column=0,  columnspan=1, sticky=tk.W+ tk.E+ tk.N+tk.S)
        self.checkSuffix.config(font=("", 10),background='#ffffff')
        #Entry suffix
        self.entrySuffix = tk.Entry(top, font=('Times', '10', 'italic'), state=tk.DISABLED,justify='center')
        self.entrySuffix.grid(row=4, column=0,sticky=tk.W+ tk.E+ tk.N+tk.S)

        #Check Prefix
        self._intPrefix = tk.IntVar()
        self.checkPrefix = tk.Checkbutton(top, text='Copy files with prefix: ',command=self.setPrefix, variable=self._intPrefix)#command = 
        self.checkPrefix.grid(row=3, column=1,  columnspan=1, sticky=tk.W+ tk.E+ tk.N+tk.S)
        self.checkPrefix.config(font=("", 10),background='#ffffff')
        #Entry prefix
        self.entryPrefix = tk.Entry(top, font=('Times', '10', 'italic'), state=tk.DISABLED,justify='center')
        self.entryPrefix.grid(row=4, column=1, sticky=tk.W+ tk.E+ tk.N+tk.S)
        
        #Check Date modified of file
        self._intDateMod = tk.IntVar()
        self.checkDateMod = tk.Checkbutton(top, text='Copy files modified at date:',command=self.setDateMod, variable=self._intDateMod)
        self.checkDateMod.grid(row=3, column=2, sticky=tk.W+ tk.E+ tk.N+tk.S)
        self.checkDateMod.config(font=("", 10),background='#ffffff')
        #Entry date modified of file
        self.entryDateMod = tk.Entry(top,  font=('Times', '10', 'italic'), state=tk.DISABLED,justify='center')
        self.entryDateMod.grid(row=4, column=2, sticky=tk.W+ tk.E+ tk.N+tk.S)

        #Check Date creation of file
        self._intDateCre = tk.IntVar()
        self.checkDateCre = tk.Checkbutton(top, text='Copy files created at date:',command=self.setDateCre, variable=self._intDateCre)
        self.checkDateCre.grid(row=3, column=3, sticky=tk.W+tk.E+tk.N+tk.S)
        self.checkDateCre.config(font=("", 10),background='#ffffff')
        #Entry date creation of file
        self.entryDateCre = tk.Entry(top, font=('Times', '10', 'italic'), state=tk.DISABLED,justify='center')
        self.entryDateCre.grid(row=4, column=3, sticky=tk.W+ tk.E+ tk.N+tk.S)

        #Check file size in KB MB GB 
        self._intFileSize = tk.IntVar()
        self.checkFileSize = tk.Checkbutton(top, text='Copy files with sizes less than:',command=self.setFileSize, variable=self._intFileSize)
        self.checkFileSize.grid(row=5, column=0,  sticky=tk.W+ tk.E+ tk.N+tk.S)
        self.checkFileSize.config(font=("", 10),background='#ffffff')
        #Entry file size
        self.entryFileSize = tk.Entry(top, font=('Times', '10', 'italic'), state=tk.DISABLED,justify='center')
        self.entryFileSize.grid(row=5, column=1, sticky=tk.W+ tk.E+ tk.N+tk.S)
        #drop-down menu 
        self.sizeString = tk.StringVar()
        self.sizeString.set("MB")

        self.menuFileSize = tk.Menubutton(top, textvariable=self.sizeString)
        self.menuFileSize.grid(row=5, column=2,  sticky=tk.W+ tk.E+ tk.N+tk.S)
        self.menuFileSize.menu = tk.Menu(self.menuFileSize,tearoff=0)
        self.menuFileSize["menu"] = self.menuFileSize.menu

        self.menuFileSize.menu.add_command(label="KB", command= self.setKB)#commands to change self.sizeString to KB MB GB
        self.menuFileSize.menu.add_command(label="MB", command= self.setMB)
        self.menuFileSize.menu.add_command(label="GB", command= self.setGB)
        #-----------------------------------------------------------------------------------------
        #---Selective options---------------------------------------------------------------------
        self.SelectiveOptFrame = tk.Frame(top, background='#1a1a1a', height = 100, width=100)
        self.SelectiveOptFrame.grid(row=6, column=0,  columnspan=4,rowspan=3, sticky=tk.W+ tk.E+ tk.N + tk.S)

        #Options text
        self.optionsLabel = tk.Label(top, text="Selective options",background='#000000', fg='#ffffff', height=1)
        self.optionsLabel.grid(row=6, column=0,  columnspan=4, sticky=tk.W+ tk.E+ tk.N+tk.S)
        self.optionsLabel.config(font=("Courier", 15))

        #Checkbutton to copy only images
        self._intImage = tk.IntVar()
        self.checkImage = tk.Checkbutton(top, text = 'Copy only image files', command = self.setImageSize, variable=self._intImage)
        self.checkImage.grid(row=7, column=0, sticky=tk.W+ tk.E+ tk.N+tk.S)
        self.checkImage.config(font=("", 10),background='#ffffff')
        
        self._intImageSize = tk.IntVar()
        self.checkImageSizePix = tk.Checkbutton(top, text='Image size(pixel x pixel):', state=tk.DISABLED, command = self.setImageSizePix, variable=self._intImageSize)
        self.checkImageSizePix.grid(row=7, column =1, sticky=tk.W+tk.E+tk.N+tk.S)
        self.checkImageSizePix.config(font=("", 8),background='#ffffff')

        self.entryImageSize = tk.Entry(top, font=('Times', '12', 'italic'), state=tk.DISABLED,justify='center')
        self.entryImageSize.grid(row=7, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=10)

        #Checkbutton to copy only video files
        self._intVideo = tk.IntVar()
        self.checkVideo = tk.Checkbutton(top, text = 'Copy only video files', command = self.setVideo, variable=self._intVideo)
        self.checkVideo.grid(row=8, column=0, sticky=tk.W+ tk.E+ tk.N+tk.S)
        self.checkVideo.config(font=("", 10),background='#ffffff')

        self._intVideoLength = tk.IntVar()
        self.checkVideoLength = tk.Checkbutton(top, text = 'Video length:(HH : MM : SS)', state=tk.DISABLED, command = self.setVideoLength, variable=self._intVideoLength)
        self.checkVideoLength.grid(row=8, column=1, sticky=tk.W+tk.E+tk.N+tk.S)
        self.checkVideoLength.config(font=("", 8),background='#ffffff')

        self.entryVideoLength = tk.Entry(top, font=('Times', '12', 'italic'), state=tk.DISABLED,justify='center')
        self.entryVideoLength.grid(row=8, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=10)

        #-----------------------------------------------------------------------------------------
        #---Adveanced options---------------------------------------------------------------------
        self.AdveancedOptFrame = tk.Frame(top, background='#1a1a1a', height = 100, width=100)
        self.AdveancedOptFrame.grid(row=9, column=0,  columnspan=4,rowspan=6, sticky=tk.W+ tk.E+ tk.N + tk.S)
        #Adveanced options text
        self.optionsLabel = tk.Label(top, text="Advanced options",background='#000000', fg='#ffffff', height=1)
        self.optionsLabel.grid(row=9, column=0,  columnspan=4, sticky=tk.W+ tk.E+ tk.N+tk.S)
        self.optionsLabel.config(font=("Courier", 15))

        self._intFolderStructure = tk.IntVar()
        self.checkFolderStructure = tk.Checkbutton(top, text = 'Copy files without folder structure', variable=self._intFolderStructure)
        self.checkFolderStructure.grid(row=10, column=0, columnspan=4, sticky=tk.W+ tk.E+ tk.N+tk.S, pady=5)
        self.checkFolderStructure.config(font=("Helvetica", 17),background='#ffffff')
        
        self._intOverwrite = tk.IntVar()
        self.checkOverwrite = tk.Checkbutton(top, text = 'Overwrite existing files', variable=self._intOverwrite)
        self.checkOverwrite.grid(row=11, column=0, columnspan=4, sticky=tk.W+ tk.E+ tk.N+tk.S, pady=5)
        self.checkOverwrite.config(font=("Helvetica", 17),background='#ffffff')

        ##Check log file
        #self._intLogFile = tk.IntVar()
        #self.checkLogFile = tk.Checkbutton(top, text = 'Create a LogFile with details of copied files', command = self.setFileLog, variable=self._intLogFile, state=tk.DISABLED)
        #self.checkLogFile.grid(row=12, column=0, columnspan=3, sticky=tk.W+ tk.E+ tk.N+tk.S, pady=5)
        #self.checkLogFile.config(font=("Helvetica", 17),background='#ffffff')
        ##Log file location
        #self.LogFileLocButton = tk.Button(top, text='Set location', state=tk.DISABLED)
        #self.LogFileLocButton.grid(row=12, column=3, sticky=tk.W+ tk.E+ tk.N+tk.S, padx=5, pady = 5)
        #self.LogFileLocButton.config(font=("Courier", 10))

        #----------------------------------------------------------------------------------------- 
        #---Start copy process Button-------------------------------------------------------------
        self.startCopyButton = tk.Button(top, text="START COPY PROCESS", background = '#deb694', command = self.startCopy)#  #631515
        self.startCopyButton.grid(row=13, column=0, columnspan=4,sticky=tk.W+ tk.E+ tk.N+tk.S)
        self.startCopyButton.config(font=("Courier", 18, "bold"),activebackground='#c4a284')
