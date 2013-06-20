import os,shutil

class CopyFiles:
    def __init__(self,cpfile):
        print "\nCopying "+cpfile+"...\n"
        #Value needs to be edited.
        dropbox = "C:\Dropbox"
        #End edit
        tools = "Technician Toolbox\Service Bundles\TuneUp - Vispy"
        shutil.copy(cpfile,dropbox+'\\'+tools)
        print "Copying of "+cpfile+"completed\n"
