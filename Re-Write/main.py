import sys,platform


#Global Definitions
def exit_(f): #Defines exit
    if f == True:
        sys.exit()
    else:
        pass

#Global Variables

stars = "*"*80
arch = platform.machine()
win = platform.release()
exit_now = False

#File check
try:
    with open('Downloads.db','r') as f:
        var = f.read()
except IOError:
    print "Read failed, generating new file..."
    with open('Downloads.db','w') as f:
        tobewritten = ['Adobe Windows:','','Adobe Plugin:','','Java:','','SAS Core:','','SAS Trace:','']
        for line in tobewritten:
            f.write(line+'\n')

#Try:Except for system arguments if available

try:
    x = sys.argv[1]
    exit_now = True
    if x == '--check' or x == '-c':
        x = '1'
    elif x == '--update' or x == '-u':
        x = '2'
    elif x == '--SAS' or x == '-s':
        x = '3'
    elif x == '--help' or x == '-h':
        print """GC Updater Version 1.2:\n
The program looks for updates for programs and downloads them into the company dropbox (and/or) storage server. The option for silent installs are available as well for Java and Adobe.

This utility does not rely on system arguments but can be used from a command line for task scheduler purposes or for batch script purposes.
Detailed below are the following arguments available.


Command\t\t\tUsage\n
-c, --check\t\tChecks for updates
-u, --update\t\tDownloads updates and places them in dropbox folder
-s, --SAS\t\tUpdates SAS only

"""
        raw_input("Press any key to exit")
        x='x'
except:
    print stars
    print "* Archetype:",arch,"\n* Windows",win
    print "* Re-Write: Genius Connect Updater Version 1.2\n* This will include the ability to \"Silently\" install files in the background\n* for users"
    print "* Arugments called:",sys.argv
    print stars,"\n"
    x = raw_input("Enter an option:")

#While loop

while x != 'x':
    if x == '1':
        print "Place holder for updater check"
    elif x == '2':
        print "Place holder for tools update"
    elif x == '3':
        print "Place holder for SAS only update"
    elif x == '4':
        print "Place holder for machine version of java and adobe"
    elif x == 'x':
        print "Exiting..."
        break
    else:
        print "Not a valid option"
    exit_(exit_now)
    x = raw_input("Enter another option (x to exit):")
