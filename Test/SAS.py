from bs4 import BeautifulSoup
import urllib, urllib2
def dlProgress(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r...%d%%" % percent)
    sys.stdout.flush()
html = urllib2.urlopen("http://www.superantispyware.com/sasportable.php","sas.com")

soup = BeautifulSoup(html)
print soup


