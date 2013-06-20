import urllib2, urllib, copy
from bs4 import BeautifulSoup
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  

############################################
#Checks Text file to begin version compares#
############################################

class Downloads:
    
    def __init__(self):
        return

    def version_find(self, windows, firefox, java):
        self = open('Downloads.txt', 'r')
        lines = []
        lines[:] = range(0,20)
        count = []
        count[:] = range(0,20)
        i = 0
        for line in self:
            lines[i] = line
            i += 1
        i = 0
        while lines[i] != '\n':
            if lines[i] == "Windows:\n":
                windows = lines[i+1]
                windows = windows.rstrip('\n')
                #print windows
            if lines[i] == "Firefox:\n":
                firefox = lines[i+1]
                firefox = firefox.rstrip('\n')
            if lines[i] == "Java:\n":
                java = lines[i+1]
                java = java.rstrip('\n')
            i += 1
        self.close
        return windows, firefox, java

    def version_print(self):
        windows = ""
        firefox = ""
        java = ""
        (windows, firefox, java) = self.version_find(windows, firefox, java)
        #print "Windows:", windows, "Firefox:", firefox
        return windows, firefox, java

class JavaDownload:
    def __init__(self):
        browser = webdriver.Ie()  
        browser.get('http://java.com/en/download/manual.jsp')  
        html_source = browser.page_source
        browser.quit()
        #html = urllib2.urlopen("http://java.com/en/download/manual.jsp")
        #html = html.read()
        soup = BeautifulSoup(html_source)
        (java32,java64) = ('','')
        for link in soup.find_all(title='Download Java software for Windows Offline'):
            java32 = link.get('href')
        for link in soup.find_all(title='Download Java software for Windows (64-bit)'):
            java64 = link.get('href')
        urllib.urlretrieve(java32,"5 - Java_32.exe")
        print "Completed Java 32 bit Download"
        urllib.urlretrieve(java64,"5 - Java_64.exe")
        copy.CopyFiles("5 - Java_32.exe")
        copy.CopyFiles("5 - Java_64.exe")

class WriteDownloadsFile:

    def __init__(self, a, b, c):
        tobewritten = ['Windows:', a,'Firefox:',b,'Java:',c,'\n']
        self = open('Downloads.txt', 'w')
        self.seek(0)
        for line in tobewritten:
            self.write(line + '\n')
        self.seek(0)
        #self.read()
        self.close
        return
