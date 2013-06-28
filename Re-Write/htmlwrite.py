import urllib, urllib2, os, sys
from bs4 import BeautifulSoup
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  

def dlProgress(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\rDownload...%d%%" % percent)
    sys.stdout.flush()

class htmlwrite():
    def __init__(self):
        return
    def htmlwrite(self):
        #Java update

        url = urllib2.urlopen("http://java.com/en/download/chrome.jsp?locale=en")
        html = url.read()
        soup = BeautifulSoup(html)
        b_tag = soup.find_all('b')
        java = b_tag[0].get_text()
        java = java.split()
        java = java[2]+' '+java[3]+' '+java[4]

        #Adobe

        url = urllib2.urlopen("http://www.adobe.com/software/flash/about/")
        html = url.read()
        soup = BeautifulSoup(html)
        td_tag = soup.find_all('td')
        adobe = td_tag[2].get_text()
        plugin = td_tag[6].get_text()

        #SAS

        url = urllib2.urlopen('http://www.superantispyware.com/definitions.html')
        html = BeautifulSoup(url)
        td_tag = html.find_all("td",align='center')
        for i in range(len(td_tag)):
            #print i, "=",td_tag[i].get_text()
            if td_tag[i].get_text() == 'Core Definitions':
                #print td_tag[i+1].get_text(),"Found successful"
                core = td_tag[i+1].get_text()
            if td_tag[i].get_text() == 'Trace Definitions':
                #print td_tag[i+1].get_text(),"Found successful"
                trace = td_tag[i+1].get_text()

        #CCleaner

        url = "http://www.piriform.com/ccleaner/builds"
        html = urllib2.urlopen(url)
        soup = BeautifulSoup(html)
        divtag = soup.find_all('div')
        font = soup.find_all('font')
        for i in range(len(divtag)):
            divtag[i] = divtag[i].get_text().split('\n')
        for i in range(len(divtag)):
            for j in range(len(divtag[i])):
                divtag[i][j] = divtag[i][j].strip(' -')
        cleaner = divtag[25][3] #version

        #File Write

        try:
            with open('downloads.html','r') as f:
                f.read()
        except:
            with open('downloads.html','w') as f:
                tobewritten = ['<html>','<head>','<title>Test</title>','</head>','<body>','This is a test','This is my variable:','</body>','</html>']
                for line in tobewritten:
                    f.write(line + '\n')
        (java32,java64) = htmlwrite().java_link()
        (win,plugin) = htmlwrite().adobe_link()

        with open('downloads.html','w') as f:
            tobewritten = ['<html>',
                           '<head>',
                           '<title>Test</title>',
                           '</head>',
                           '<body>',
                           '<h1>Current Versions:</h1>',
                           '<p><h2>Java:</h2> '+java+'</p>',
                           '<p><h2>Adobe Active X:</h2> '+adobe+'</p>',
                           '<p><h2>Adobe Plugin:</h2> '+plugin+'</p>',
                           '<p><h2>SAS Trace:</h2> '+trace+'</p>',
                           '<p><h2>SAS Core:</h2> '+core+'</p>',
                           '<p><h2>Ccleaner:</h2> '+cleaner+'</p>',
                           '<h3>Links:</h3>',
                           '<a href="'+java32+'">Java 32</a>'+'<br>',
                           java64+'<br>',
                           win+'<br>',
                           plugin+'<br>',
                           '</body>',
                           '</html>']
            for line in tobewritten:
                f.write(line + '\n')
        return
    def java_link(self):
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
##        urllib.urlretrieve(java32,"5 - Java_32.exe", reporthook=dlProgress)
##        print "\nCompleted Java 32 bit Download"
##        urllib.urlretrieve(java64,"5 - Java_64.exe", reporthook=dlProgress)
        return java32, java64

    def sas_link(self):
        sas = 'http://www.superantispyware.com/sasportable.php'
        headers = { 'Referer' : 'http://www.superantispyware.com/portablescannertech.html'}
        data = ''
        req = urllib2.Request(sas,data,headers)
        test = urllib2.urlopen(req)
        print test, req
        sas_size = test.headers["Content-Length"]
        sas_size = int(sas_size)
        with open(os.path.basename('3 - Super Anti Spyware.COM'), "wb") as local_file:
            print "Downloading"
            local_file.write(test.read())
            print "Complete"
        return

    def adobe_link(self):
        win = 'http://download.macromedia.com/pub/flashplayer/current/support/install_flash_player_ax.exe'
        plugin = 'http://download.macromedia.com/get/flashplayer/current/licensing/win/install_flash_player_11_plugin.exe'
        return win, plugin
