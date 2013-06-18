from bs4 import BeautifulSoup
import urllib2
import urllib
import re
from downloads import Downloads
from downloads import WriteDownloadsFile
from webParse import JavaUpdater


#Text to display before handling
print "Checking Downloads file:\n"


#Open the Downloads.txt file and read data into variables
downloads = Downloads()
(win_txt,plug_txt,java_txt) = downloads.version_print()
print "Windows Text Version:", win_txt, '\n', "Plugin Text Version:", plug_txt, '\n', "Java Version: ", java_txt

print "\nComparing local versions with actual versions:\n"

#Open the URL and read the url into a variable

url = urllib2.urlopen("http://www.adobe.com/software/flash/about/")
html2 = url.read()

#Use beautiful soup to handle tags and find all td tags

soup = BeautifulSoup(html2)
td_tag = soup.find_all('td')

#create an array that stores each td tag in a slot and for loop through them for specific tags

iTerator = []
iTerator[:] = range(2,16)
windows = ""
firefox = ""
for i in iTerator:
    if i == 2:
        #print i
        windows = td_tag[i].get_text()
        #print "Windows:", td_tag[i].get_text()
    if i == 11:
        #print i
        firefox = td_tag[i].get_text()
        #print "Firefox:", td_tag[i].get_text()

#Compare Java Downloads

javacheck = JavaUpdater()
java = javacheck.java_check()

#If function to check versions of Downloaded copies versus uploaded copies of Flash

if windows == win_txt:
    print "File versions match"
else:
    print "Updating Flash for IE:"
    urllib.urlretrieve("http://download.macromedia.com/pub/flashplayer/current/support/install_flash_player_ax.exe","Flash_Active_AX.exe")
    print "Complete"

if firefox == plug_txt:
    print "File Versions match"
else:
    print "Updating Flash Plugin:"
    urllib.urlretrieve("http://download.macromedia.com/get/flashplayer/current/licensing/win/install_flash_player_11_plugin.exe", "Flash_Plugin.exe")
    print "Complete"

if java == java_txt:
    print "File Versions match"
else:
    print "Updating Java x86 and x64"

    print "Complete"

#Write the versions to the text file for future calls

WriteDownloadsFile(windows,firefox,java)
