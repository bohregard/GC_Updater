import webParse, downloads, compare, time

#########################################################
#               Check versions from web                 #
#########################################################
print "Checking versions from web...\n"
time.sleep(2)
adobeupdate = webParse.AdobeUpdater()
(windows, firefox) = adobeupdate.adobe_version()

javaupdate = webParse.JavaUpdater()
(java) = javaupdate.java_check()
print windows, firefox, java


#########################################################
#               Compare versions from file              #
#########################################################
print "\nComparing versions...\n"
time.sleep(2)
textversion = downloads.Downloads()
(windows_txt,firefox_txt,java_txt) = textversion.version_print()
print windows_txt,firefox_txt,java_txt,'\n'


#########################################################
#               Download and write versions             #
#########################################################

a,b,c,d,e,f = ('','','','','','')
compare.DownloadFiles(windows, windows_txt,firefox,firefox_txt,java,java_txt)


downloads.WriteDownloadsFile(windows,firefox,java)

print "\nFinished\n"
time.sleep(5)
