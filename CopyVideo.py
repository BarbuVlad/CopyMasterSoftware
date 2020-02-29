import copyData
import shutil
import os
from moviepy.editor import VideoFileClip
from filetype import guess
class copyVideo(copyData.copyData):
    def __init__(self, source="", target=""):
        super().__init__(source, target)
        self.videoTime = None

    def _videoRestrictions(self, pathSource):
        try:# if file is not a video it trows an error
            video_extensions = ['mp4','m4v','mkv','webm','mov','avi','wmv','mpg','flv']
            file_ext = guess(pathSource)
            if file_ext == None:
                raise Exception ("File is not a video. Cannot get extension")
            if  file_ext.extension not in video_extensions:
                raise Exception("File is not a video. Extension exists")

            #calculate video time length 
            if self.videoTime == None:#no restrictions on video length
                return True
            else:#self.videoTime = x seconds
                video = VideoFileClip (pathSource)
                if video.duration <= self.videoTime:
                    video.close()
                    return True
                else: #file is video, but dose not respect restrictions
                    video.close()
                    return False

        except Exception as e:
            return False #file is not video

    def _copyFileToLocation(self, pathSource, pathDest):
        '''Method to be called only inside the class! 
        This method copies a file from pathSource to pathDest and it overwrites that file it the atribute self.overwrite is True, otherwise it dose not'''
        if self.overwrite == True:
            try:
                if self._videoRestrictions(pathSource) == True:
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
                    if self._videoRestrictions(pathSource) == True:
                        shutil.copy2(pathSource, pathDest)
                except Exception as e:
                   # print("Error at copy.{}  {}".format(e,pathSource))
                   return












