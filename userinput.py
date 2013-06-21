import webParse, downloads, time, compare, SilentInstall

#Global Variabls
globstar = 70

#Begin Version Check

(version, arch) = SilentInstall.PlatformLookup().version_print()
print "*"*globstar,"\nCurrent setup:\n","Version: Windows",version,"\nArch:",arch,"\n","*"*globstar

#Begin Main Program

print "\nChoose an option:\n1: Check for updates (no write to file)\n2: Download and install updates\n3: Check and download updates (drops in dropbox location; no install)\n4: Check for SuperAnti-Spyware Update"

try:
    with open('Downloads.txt'):pass
except IOError:
    downloads.WriteDownloadsFile('','','','','','')

x = None
while x != 'x':
    x = raw_input('\nEnter an option (x to exit): ')
    if x == '1':
        print "\nChecking versions from web...\n"
        time.sleep(.5)
        adobeupdate = webParse.AdobeUpdater()
        (windows, firefox) = adobeupdate.adobe_version()

        javaupdate = webParse.JavaUpdater()
        (java) = javaupdate.java_check()

        (core,trace) = webParse.SuperAntiUpdater().sas_check()

        cleaner = webParse.CCleanerUpdater().clean_check()

        print "Comparing versions...\n"
        time.sleep(.5)
        textversion = downloads.Downloads()
        (windows_txt,firefox_txt,java_txt, core_txt, trace_txt, cleaner_txt) = textversion.version_print()

        print "*"*globstar,"\nAdobe Versions:",windows,"and",firefox,"\n","*"*globstar
        compare.CompAdobe().comp(windows,windows_txt,firefox,firefox_txt)

        print "*"*globstar,"\nJava Version:",java,"\n","*"*globstar
        compare.CompJava().comp(java,java_txt)

        print "*"*globstar,"\nSAS Versions: Core:",core,"Trace:",trace,"\n","*"*globstar
        compare.CompSAS().comp(core,core_txt,trace,trace_txt)
        
        print "*"*globstar,"\nCCleaner Versions: ",cleaner,"\n","*"*globstar
        compare.CompCleaner().comp(cleaner, cleaner_txt)
        

        
        
    elif x == '2':
        print "\nPlace holder for future silent install option"
        

    elif x == '3':
        print "\nChecking versions from web...\n"
        time.sleep(.5)
        adobeupdate = webParse.AdobeUpdater()
        (windows, firefox) = adobeupdate.adobe_version()

        javaupdate = webParse.JavaUpdater()
        (java) = javaupdate.java_check()

        (core,trace) = webParse.SuperAntiUpdater().sas_check()

        cleaner = webParse.CCleanerUpdater().clean_check()

        print "Comparing versions...\n"
        time.sleep(.5)
        textversion = downloads.Downloads()
        (windows_txt,firefox_txt,java_txt, core_txt, trace_txt, cleaner_txt) = textversion.version_print()

        print "*"*globstar,"\nAdobe Versions:",windows,"and",firefox,"\n","*"*globstar
        compare.CompAdobe().download(windows,windows_txt,firefox,firefox_txt)

        print "*"*globstar,"\nJava Version:",java,"\n","*"*globstar
        compare.CompJava().download(java,java_txt)

        print "*"*globstar,"\nSAS Versions: Core:",core,"Trace:",trace,"\n","*"*globstar
        compare.CompSAS().download(core,core_txt,trace,trace_txt)

        print "*"*globstar,"\nCCleaner Versions: ",cleaner,"\n","*"*globstar
        compare.CompCleaner().download(cleaner, cleaner_txt)

        downloads.WriteDownloadsFile(windows,firefox,java,core,trace, cleaner)

    elif x == '4':
        print "Checking for SuperAnti-Spyware Update"
        (a,b) = webParse.SuperAntiUpdater().sas_check()
        print "Core Def:",a,"\nTrace Def:",b

    elif x == 'x':
        break
    else:
        print "Not a valid option"
print "\nCompleted with 0 errors"

time.sleep(1.2)
