import webParse, downloads, time, compare, SilentInstall

print "Choose an option:\n1: Check for updates\n2: Download and install updates\n3: Check and download updates (no install)"

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

        compare.Compare(windows,windows_txt,firefox,firefox_txt,java,java_txt)

        
        break
    elif x == '3':
        print "Choice 3"
        break
    elif x == 'x':
        break
    else:
        print "Not a valid option"
print "\nCompleted with 0 errors"
