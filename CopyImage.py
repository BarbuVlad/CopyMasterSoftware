import copyData
from PIL import Image
from imghdr import what
import shutil
import os
class copyImage(copyData.copyData):
    def __init__(self, source="", target=""):
        super().__init__(source, target)
        self.imageSize = None #tuple (width, height)

    def _imageRestrictions(self, pathSource):
        try:
            if what(pathSource)!=None: #is this file an image?
                if self.imageSize != None: #there is a restriction on image size
                    img = Image.open(pathSource)
                    if img.size <= self.imageSize:
                        img.close()
                        return True
                    else:
                        img.close()
                        return False#image size not respected
                else:#no restriction on image size, but file is an image
                    return True
            else:#file is not an image
                #print("File not an image\n")
                return False
        except Exception as e:
            #print(e)
            return False

    def _copyFileToLocation(self, pathSource, pathDest):
        '''Method to be called only inside the class! 
        This method copies a file from pathSource to pathDest and it overwrites that file it the atribute self.overwrite is True, otherwise it dose not'''
        if self.overwrite == True:
            try:
                if self._imageRestrictions(pathSource) == True:
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
                    if self._imageRestrictions(pathSource) == True:
                        shutil.copy2(pathSource, pathDest)
                except Exception as e:
                   # print("Error at copy.{}  {}".format(e,pathSource))
                   return
                
