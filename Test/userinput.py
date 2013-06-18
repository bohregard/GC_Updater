print "Choose an option:\n1: Check for updates\n2: Download and install updates\n3: Download updates only"

x = None
while x != 'x':
    x = raw_input('Enter an option (x to exit): ')
    if x == '1':
        print "Choice 1"
        break
    elif x == '2':
        print "Choice 2"
        break
    elif x == '3':
        print "Choice 3"
        break
    elif x == 'x':
        break
    else:
        print "Not a valid option"
print "Completed with 0 errors"

