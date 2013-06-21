import urllib, downloads, time,sys
def dlProgress(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r...%d%%" % percent)
    sys.stdout.flush()
    
class DownloadFiles:
    def __init__(self, a,b,c,d,e,f):
        i = .5
        #adobe windows
        if a == b:
            print "Match"
            time.sleep(i)
        else:
            print "Downloading Flash for IE:"
            urllib.urlretrieve("http://download.macromedia.com/pub/flashplayer/current/support/install_flash_player_ax.exe","Flash_Active_AX.exe", reporthook=dlProgress)
            print "Completed Flash for IE"
        #adobe firefox
        if c == d:
            print "Match"
            time.sleep(i)
        else:
            print "Downloading Flash Plugin:"
            urllib.urlretrieve("http://download.macromedia.com/get/flashplayer/current/licensing/win/install_flash_player_11_plugin.exe", "Flash_Plugin.exe", reporthook=dlProgress)
            print "Completed Flash Plugin"
        #Java
        if e == f:
            print "Match"
            time.sleep(i)
        else:
            print "Downloading Java 32 and 64 bit:"
            downloads.JavaDownload()
            print "Completed Java 32 and 64 bit"
        return

class Compare:
    def __init__(self, a,b,c,d,e,f,g,h,j,k):
        i = .5
        #adobe windows
        if a == b:
            print "Match"
            time.sleep(i)
        else:
            print "Update available for adobe"
        #adobe firefox
        if c == d:
            print "Match"
            time.sleep(i)
        else:
            print "Update available for adobe plugin"
        #Java
        if e == f:
            print "Match"
            time.sleep(i)
        else:
            print "Update available for Java"
        #SAS
        if g == h:
            print "Match"
            time.sleep(i)
        else:
            print "Update for SAS Core"
        if j == k:
            print "Match"
            time.sleep(i)
        else:
            print "Update for SAS Trace"
        return
