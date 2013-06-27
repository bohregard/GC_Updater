import urllib, urllib2
from bs4 import BeautifulSoup

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
                   '</body>',
                   '</html>']
    for line in tobewritten:
        f.write(line + '\n')
