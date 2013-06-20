import urllib, os, sys,time

def dlProgress(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r...%d%%" % percent)
    sys.stdout.flush()

urllib.urlretrieve('http://javadl.sun.com/webapps/download/AutoDL?BundleId=78825', 'java.exe', reporthook=dlProgress)
