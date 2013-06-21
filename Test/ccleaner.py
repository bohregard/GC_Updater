import urllib, urllib2, os, zipfile
from bs4 import BeautifulSoup

downurl = "http://www.piriform.com/ccleaner/download/portable//downloadfile"

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
        
for i in range(len(divtag)):
    for j in range(len(divtag[i])):            
        if 'Zip' in divtag[i][j]:
            print "true for divtag[",i,"][",j,"]",divtag[i][j+2]

urllib.urlretrieve(downurl,'Ccleaner.zip')
zipfile.ZipFile('Ccleaner.zip').extract('CCleaner.exe')
zipfile.ZipFile('Ccleaner.zip').extract('CCleaner64.exe')
zipfile.ZipFile('Ccleaner.zip').close()
