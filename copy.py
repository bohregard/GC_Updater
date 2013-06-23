import os,shutil

class CopyFiles:
    def __init__(self,cpfile):
        print "\nCopying "+cpfile+"...\n"
        #Value needs to be edited.
        dropbox = "Downloads"
        #End edit
        tools = "TechToolbox"
        shutil.copy(cpfile,dropbox+'\\'+tools)
        os.remove(cpfile)
        print "Copying of "+cpfile+" completed\n"
