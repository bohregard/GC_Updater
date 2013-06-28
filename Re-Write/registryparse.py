import platform
import _winreg as reg

class Parser:
    def __init__(self):
        return
    
    def updaterJava(self):
        disp64 = []
        vers64 = []
        disp32 = []
        vers32 = []
        arch = platform.machine()
        if arch == 'AMD64':
            bit = reg.KEY_WOW64_64KEY
            (disp64, vers64) = Parser().registryParser(bit)
            bit = reg.KEY_WOW64_32KEY
            (disp32, vers32) = Parser().registryParser(bit)
        else:
            bit = reg.KEY_WOW64_32KEY
        for i in range(len(disp32)):
            if 'Java' in disp32[i]:
                print "Display Name: ",disp32[i],"\tDisplay Version: ",vers32[i]
        for i in range(len(disp64)):
            if 'Java' in disp64[i]:
                print "Display Name: ",disp64[i],"\tDisplay Version: ",vers64[i]
        return

    def updaterAdobe(self):
        disp64 = []
        vers64 = []
        disp32 = []
        vers32 = []
        arch = platform.machine()
        if arch == 'AMD64':
            bit = reg.KEY_WOW64_64KEY
            (disp64, vers64) = Parser().registryParser(bit)
            bit = reg.KEY_WOW64_32KEY
            (disp32, vers32) = Parser().registryParser(bit)
        else:
            bit = reg.KEY_WOW64_32KEY
        for i in range(len(disp32)):
            if 'Adobe Flash' in disp32[i]:
                print "Display Name: ",disp32[i],"\tDisplay Version: ",vers32[i]
        for i in range(len(disp64)):
            if 'Adobe Flash' in disp64[i]:
                print "Display Name: ",disp64[i],"\tDisplay Version: ",vers64[i]
        return
    
    def registryParser(self, bit):
        softlog = 'Installed_Software.log'
        uninstall = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'
        i_soft = open(softlog,'w')
        uninstaller = reg.OpenKey(reg.HKEY_LOCAL_MACHINE,uninstall,0,reg.KEY_ALL_ACCESS | bit)
        length = reg.QueryInfoKey(uninstaller)
        displayname = range(int(length[0]))
        version = range(int(length[0]))
        try:
            i = 0
            while True:
                subkey = reg.EnumKey(uninstaller, i)
                key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE,uninstall+'\\'+subkey,0,reg.KEY_ALL_ACCESS | bit)
                try:
                    displayname[i] = reg.QueryValueEx(key,'DisplayName')
                    displayname[i] = displayname[i][0]
                except WindowsError:
                    displayname[i] = subkey
                try:
                    version[i] = reg.QueryValueEx(key,'DisplayVersion')
                    version[i] = version[i][0]
                except WindowsError:
                    version[i] = 'Null'
                i += 1
        except WindowsError:
            print

        for i in range(len(displayname)):
            try:
                displayname[i] = str((displayname[i]).encode('utf-8'))
            except:
                displayname[i] = str(displayname[i])
        i_soft.write('*'*80+'\n'+'32-Bit Software Installed\n'+'*'*80+'\n\n')
        for i in range(len(displayname)):
            i_soft.write("Display Name: "+displayname[i]+'; Version: '+str(version[i])+'\n')
        i_soft.close()

        return displayname, version

Parser().updaterJava()
Parser().updaterAdobe()
