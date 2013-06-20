import webParse, downloads, time, compare, SilentInstall
(version, arch) = SilentInstall.PlatformLookup().version_print()
print "Current setup:\n","Version: Windows",version,"\nArch:",arch
print "Choose an option:\n1: Check for updates (no write to file)\n2: Download and install updates\n3: Check and download updates (drops in dropbox location; no install)"

try:
    with open('Downloads.txt'):pass
except IOError:
    downloads.WriteDownloadsFile('','','')

x = None
while x != 'x':
    x = raw_input('Enter an option (x to exit): ')
    if x == '1':
        print "Checking versions from web...\n"
        time.sleep(.5)
        adobeupdate = webParse.AdobeUpdater()
        (windows, firefox) = adobeupdate.adobe_version()

        javaupdate = webParse.JavaUpdater()
        (java) = javaupdate.java_check()

        print "Comparing versions...\n"
        time.sleep(.5)
        textversion = downloads.Downloads()
        (windows_txt,firefox_txt,java_txt) = textversion.version_print()

        compare.Compare(windows,windows_txt,firefox,firefox_txt,java,java_txt)

        downloads.WriteDownloadsFile(windows,firefox,java)
        
        break
    elif x == '2':
        print "Checking versions from web...\n"
        time.sleep(.5)
        adobeupdate = webParse.AdobeUpdater()
        (windows, firefox) = adobeupdate.adobe_version()

        javaupdate = webParse.JavaUpdater()
        (java) = javaupdate.java_check()

        print "Comparing versions...\n"
        time.sleep(.5)
        textversion = downloads.Downloads()
        (windows_txt,firefox_txt,java_txt) = textversion.version_print()

        compare.DownloadFiles(windows,windows_txt,firefox,firefox_txt,java,java_txt)
        
        if java != java_txt:
            SilentInstall.SilentInstallJava(arch)
        else:
            print "Java already installed and up-to-date"

        if windows != windows_txt:
            SilentInstall.SilentInstallAdobe(version)

        downloads.WriteDownloadsFile(windows,firefox,java)
        
        break
    elif x == '3':
        print "Checking versions from web...\n"
        time.sleep(.5)
        adobeupdate = webParse.AdobeUpdater()
        (windows, firefox) = adobeupdate.adobe_version()

        javaupdate = webParse.JavaUpdater()
        (java) = javaupdate.java_check()

        print "Comparing versions...\n"
        time.sleep(.5)
        textversion = downloads.Downloads()
        (windows_txt,firefox_txt,java_txt) = textversion.version_print()
        
        compare.DownloadFiles(windows,windows_txt,firefox,firefox_txt,java,java_txt)

        downloads.WriteDownloadsFile(windows,firefox,java)
        
        break
    elif x == 'x':
        break
    else:
        print "Not a valid option"
print "\nCompleted with 0 errors"

time.sleep(1.2)
