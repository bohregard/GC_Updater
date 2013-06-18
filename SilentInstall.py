import os,platform

class PlatformLookup:
    def __init__(self):
        return
    def version_print(self):
        version = platform.release()
        arch = platform.machine()
        print "Windows",version,"detected"
        return version, arch


class SilentInstallAdobe:
    def __init__(self,version):
        if version == '8':
            print "Adobe flash is built in...\nSkipping..."
            os.popen("cmd /k Flash_Plugin.exe -install")
            print "Installed Flash Plugin"
        else:
            print "Installing Flash Active X and Flash Plugins"
            os.popen("cmd /k Flash_Plugin.exe -install")
            os.popen("cmd /k Flash_Active_AX.exe -install")
class SilentInstallJava:
    def __init__(self,arch):
        if arch != 'AMD64':
            print "Arch is x86...\nSkipping Java_64"
            os.popen("cmd /k java_32.exe /s /L Javax86.log")
        else:
            print "Arch is x64...\n"
            print "Installing Java 86..."
            os.popen("cmd /k java_32.exe /s /L Javax86.log")
            print "Completed Java 86\nInstalling Java 64"
            os.popen("cmd /k java_64.exe /s /L Javax64.log")
            print "Completed Java 64"
        return
