import urllib, downloads, time,sys, webParse, copy

def dlProgress(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r...%d%%" % percent)
    sys.stdout.flush()

i = .5

class CompAdobe:
    def comp(self, a, b, c, d):
        if a == b:
            print "Match"
            time.sleep(i)
        else:
            print "Update available for adobe"
        if c == d:
            print "Match"
            time.sleep(i)
        else:
            print "Update available for adobe plugin"
        return
    def download(self,a,b,c,d):
        #adobe windows
        if a == b:
            print "Adobe AX: Match"
            time.sleep(i)
        else:
            print "Adobe AX: Mismatch\nDownloading Flash for IE:"
            urllib.urlretrieve("http://download.macromedia.com/pub/flashplayer/current/support/install_flash_player_ax.exe","4 - Flash_Active_AX.exe", reporthook=dlProgress)
            copy.CopyFiles('4 - Flash_Active_AX.exe')
            print "\nCompleted Flash for IE"
        #adobe firefox
        if c == d:
            print "Adobe Plugin: Match"
            time.sleep(i)
        else:
            print "Adobe Plugin: Mismatch\nDownloading Flash Plugin:"
            urllib.urlretrieve("http://download.macromedia.com/get/flashplayer/current/licensing/win/install_flash_player_11_plugin.exe", "4 - Flash_Plugin.exe", reporthook=dlProgress)
            copy.CopyFiles('4 - Flash_Plugin.exe')
            print "\nCompleted Flash Plugin"
            
class CompJava:
    def comp(self,a,b):
        if a == b:
            print "Match"
            time.sleep(i)
        else:
            print "Update available for Java"
        return
    def download(self,a,b):
        #Java
        if a == b:
            print "Java: Match"
            time.sleep(i)
        else:
            print "Java: Mismatch\nDownloading Java 32 and 64 bit:"
            downloads.JavaDownload()
            copy.CopyFiles("5 - Java_32.exe")
            copy.CopyFiles("5 - Java_64.exe")
            print "\nCompleted Java 32 and 64 bit"
            
class CompSAS:
    def comp(self,a,b,c,d):
        if a == b and c == d:
            print "Match"
            time.sleep(i)
        else:
            print "Update available for SAS"
        return
    def download(self,a,b,c,d):
        if a == b and c == d:
            print "SuperAntiSpyware: Match"
            time.sleep(i)
        else:
            print "SuperAntiSpyware: Mismatch\nDownloading SuperAntiSpyware:"
            downloads.SuperDownload()
            copy.CopyFiles('3 - SuperAntiSpyware.COM')
            print "\nCompleted SuperAntiSpyware"
            
class CompCleaner:
    def comp(self,a,b):
        if a == b:
            print "Match"
        else:
            print "Update available for CCleaner"
        return
    def download(self,a,b):
        if a == b:
            print "CCleaner: Match"
        else:
            print "CCleaner: Mismatch\nDownoading CCleaner:"
            webParse.CCleanerUpdater().clean_down()
            copy.CopyFiles('2 - CCleaner (64).exe')
            copy.CopyFiles('2 - CCleaner (32).exe')
            print "\nCompleted CCleaner"
        return
