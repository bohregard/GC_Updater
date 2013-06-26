import os,shutil,base64

class CopyFiles:
    def __init__(self,cpfile):
        
        #Value needs to be edited.
        APPDATA = os.environ['APPDATA']
        dropdb = open(APPDATA + '\\Dropbox\\host.db', 'r+')
        coded_string = dropdb.read()
        dropbox = coded_string.lstrip('0')
        dropdb.close()
        dropbox = base64.b64decode(dropbox)
        tools = "Technician Toolbox\Service Bundles\TuneUp - Vispy"
        virus = "\Technician Toolbox\Virus and Spyware Removal"
        #End edit

        #Copying File into tuneup folder
        print "\nCopying "+cpfile+"...\n"
        shutil.copy(cpfile,dropbox+'\\'+tools)
        print "Copying of "+cpfile+" completed\n"

        #Rename file and copy into virus folder
        nwfile = cpfile.lstrip('[123456789 -]')
        os.rename(cpfile, nwfile)
        print "\nCopying "+nwfile+"...\n"
        shutil.copy(nwfile,dropbox+'\\'+virus)
        os.remove(nwfile)
        print "Copying of "+nwfile+" completed\n"
