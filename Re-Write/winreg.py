import _winreg as reg
i_soft = open('Installed_Software.log','w')
uninstaller = reg.OpenKey(
    reg.HKEY_LOCAL_MACHINE,
    "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall",
    0,
    reg.KEY_ALL_ACCESS | reg.KEY_WOW64_64KEY
    )
length = reg.QueryInfoKey(uninstaller)
value = displayname = range(int(length[0]))
version = range(int(length[0]))
try:
    i = 0
    while True:
        subkey = reg.EnumKey(uninstaller,i)
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE,
        "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\"+subkey,
                          0,
                          reg.KEY_ALL_ACCESS | reg.KEY_WOW64_64KEY
        )
        try:
            value[i] = reg.QueryValueEx(key,'DisplayName')
            value[i] = value[i][0]
        except WindowsError:
            value[i] = subkey
        try:
            version[i] = reg.QueryValueEx(key,'DisplayVersion')
            version[i] = version[i][0]
        except WindowsError:
            version[i] = 'Null'
        try:
            pass
            #print subkey, displayname[i], version[i]
        except:
            #print subkey
            pass
        i += 1
except WindowsError:
    print

for i in range(len(displayname)):
    try:
        value[i] = str((value[i]).encode("utf-8"))
        #print i, value[i]
    except:
        value[i] = str(value[i])
        #print i, value[i]

for i in range(len(displayname)):
    #print i
    if 'Java' in value[i]:
        #print "Successfully found java"
        print "Display Name: ",value[i]
        print "Display Version: ",version[i]

i_soft.write('*'*80+'\n'+'64-Bit Software Installed\n'+'*'*80+'\n\n')
for i in range(len(displayname)):
    i_soft.write("Display Name: "+value[i]+'; Version: '+str(version[i])+'\n')

i_soft.close()
#####32 BIT REGISTRY#####

i_soft = open('Installed_Software.log','a')
uninstaller = reg.OpenKey(
    reg.HKEY_LOCAL_MACHINE,
    "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall",
    0,
    reg.KEY_ALL_ACCESS | reg.KEY_WOW64_32KEY
    )
length = reg.QueryInfoKey(uninstaller)
value = displayname = range(int(length[0]))
version = range(int(length[0]))
try:
    i = 0
    while True:
        subkey = reg.EnumKey(uninstaller,i)
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE,
        "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\"+subkey,
                          0,
                          reg.KEY_ALL_ACCESS | reg.KEY_WOW64_32KEY
        )
        try:
            value[i] = reg.QueryValueEx(key,'DisplayName')
            value[i] = value[i][0]
        except WindowsError:
            value[i] = subkey
        try:
            version[i] = reg.QueryValueEx(key,'DisplayVersion')
            version[i] = version[i][0]
        except WindowsError:
            version[i] = 'Null'
        try:
            pass
            #print subkey, displayname[i], version[i]
        except:
            #print subkey
            pass
        i += 1
except WindowsError:
    print

for i in range(len(displayname)):
    try:
        value[i] = str((value[i]).encode("utf-8"))
        #print i, value[i]
    except:
        value[i] = str(value[i])
        #print i, value[i]

for i in range(len(displayname)):
    #print i
    if 'Java' in value[i]:
        #print "Successfully found java"
        print "Display Name: ",value[i]
        print "Display Version: ",version[i]

i_soft.write('\n\n'+'*'*80+'\n'+'32-Bit Software Installed\n'+'*'*80+'\n\n')
for i in range(len(displayname)):
    i_soft.write("Display Name: "+value[i]+'; Version: '+str(version[i])+'\n')
i_soft.close()
