import _winreg as reg

uninstaller = reg.OpenKey(
    reg.HKEY_LOCAL_MACHINE,
    "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall"
    )

try:
    i = 0
    while True:
        subkey = reg.EnumKey(uninstaller,i)
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE,
        "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\"+subkey
        )
        value = reg.QueryValueEx(key,'DisplayName')
        print subkey, value[0]
        i += 1
except WindowsError:
    print

