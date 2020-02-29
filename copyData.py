import os
import shutil
class copyData():
    def __init__(self, source="", target=""):
        ''' '''
        self.source = os.path.normpath(source)
        self.target=os.path.normpath(target)
        #restrictions for copy 
        #name of file 
        self.suffix = None
        self.prefix = None
        #file
        self.fileSize = None # if less then this amount, in bytes 
        #date info
        #string in format: "day month year"
        self.dateCreated = None
        self.dateModified = None

        #overwrite
        self.overwrite = False
        #create a log file with all details?
        self.logData = False 

    def _createFolderBaseName(self):
        '''Method to be called only inside the class! 
        The method modifies the target atribute to be the target + the name of the folder from which we copy, it also creates that folder 
        '''
        self.target = os.path.join(self.target,os.path.basename(self.source))
        try:
            os.makedirs(self.target)
            #return self.target
        except:
            #print("Error at file creation")
            return
    
    def _verifyRestrictions(self, pathToFile):
        '''Method to be called only inside the class! 
        This method verifies all existing restrictions for the file to be copied '''
        #if it is file
        if os.path.isfile(pathToFile) == False:
            #print("Path to file is not a file! Exit with False")
            return False

        nameOfFile = os.path.basename(pathToFile)# the actual name of the file from the path to file
        if self.suffix != None:
            suffixOfFile = nameOfFile[-len(self.suffix): ]# last n characters
            if suffixOfFile != self.suffix:
                return False # suffix is not right 

        if self.prefix != None:
            prefixOfFile = nameOfFile[:len(self.prefix)] # first n characters
            if prefixOfFile != self.prefix:
                return False # prefix is not right

        if self.fileSize != None:
            size = os.path.getsize(pathToFile)
            if size > self.fileSize:
                return False

        if self.dateCreated != None:
            from time import gmtime
            modTime =os.path.getctime(pathToFile)
            modTime = gmtime(modTime)#(tm_year=2018, tm_mon=12, tm_mday=28, tm_hour=8, tm_min=44, tm_sec=4, tm_wday=4, tm_yday=362, tm_isdst=0)
            stringTime = (str)(modTime.tm_mday) +' '+ (str)(modTime.tm_mon) +' '+ (str)(modTime.tm_year)#day month year
            if stringTime != self.dateCreated:
                return False
            
        if self.dateModified != None:
            from time import gmtime
            modTime =os.path.getmtime(pathToFile)
            modTime = gmtime(modTime)#(tm_year=2018, tm_mon=12, tm_mday=28, tm_hour=8, tm_min=44, tm_sec=4, tm_wday=4, tm_yday=362, tm_isdst=0)
            stringTime = (str)(modTime.tm_mday) +' '+ (str)(modTime.tm_mon) +' '+ (str)(modTime.tm_year)#day month year
            if stringTime != self.dateModified:
                return False

        return True # all tests passed 

    def _copyFileToLocation(self, pathSource, pathDest):
        '''Method to be called only inside the class! 
        This method copies a file from pathSource to pathDest and it overwrites that file it the atribute self.overwrite is True, otherwise it dose not'''
        if self.overwrite == True:
            try:
                shutil.copy2(pathSource, pathDest)
            except Exception as e:
                #print("Error at copy: {}  {}".format(e, pathSource))
                return
        else:#if file exists at destination don't copy
            if os.path.exists(pathDest+'\\'+os.path.basename(pathSource)):
                #print("File exists, {}".format(pathDest+'\\'+os.path.basename(pathSource)))
                return
            else:
                try:
                    shutil.copy2(pathSource, pathDest)
                except Exception as e:
                    #print("Error at copy.{}  {}".format(e,pathSource))
                    return
    #copy methods:
    def copyWithStructure (self):
        '''Copies all files (with respect to the restrictions set) and the folder structure from self.source to self.destination'''
        self._createFolderBaseName() # create folder to copy data in 

        fileCrawler = os.walk(self.source)
        for dirpath, dirnames, filenames in fileCrawler:#copy the folder structure
            if(len(dirnames) == 0):#we are in the last folder 
                folderStructure = dirpath.replace(self.source, '')#keep basename of structure
                folderStructure = os.path.normpath(folderStructure)
                try:
                    os.makedirs(self.target+folderStructure)
                except FileExistsError:
                    #print("FileExistsError\n")
                    return
                except:
                    #print("Error\n")
                    return
        #copy files:
        fileCrawler = os.walk(self.source) # reset file crawler
        for dirpath, dirnames, filenames in fileCrawler:
            for i in filenames:
                if(self._verifyRestrictions(dirpath+'\\'+i) == True):
                    #calculete file destination
                    #print(dirpath+'\\'+i)
                    destination = dirpath.replace(self.source, self.target)
                    self._copyFileToLocation(dirpath+'\\'+i, destination)

                        

    def copyWithout(self):
        self._createFolderBaseName()
        fileCrawler = os.walk(self.source)
        for dirpath, dirnames, filenames in fileCrawler:
            for i in filenames:
                if(self._verifyRestrictions(dirpath+'\\'+i) == True):
                    #print(dirpath+'\\'+i)
                    self._copyFileToLocation(dirpath+'\\'+i, self.target)