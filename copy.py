import os,shutil



class CopyFiles:
    def __init__(self,cpfile):
##        if __name__ == "__main__":
##            config = {}
##            execfile("config.conf",config)
## 
##            dropbox = config["dropbox"]
##            tools = config["techtool"]
        print "\nCopying "+cpfile+"...\n"
        dropbox = "C:\Dropbox"
        tools = "Technician Toolbox\Service Bundles\TuneUp - Vispy"
        shutil.copy(cpfile,dropbox+'\\'+tools)
        print "Copying of"+cpfile+"completed\n"
