from bs4 import BeautifulSoup
import urllib, urllib2

url = urllib2.urlopen('http://www.superantispyware.com/definitions.html')
html = BeautifulSoup(url)

td_tag = html.find_all("td",align='center')

for i in range(len(td_tag)):
    #print i, "=",td_tag[i].get_text()
    if td_tag[i].get_text() == 'Core Definitions':
        #print td_tag[i+1].get_text(),"Found successful"
        core_Def = td_tag[i+1].get_text()
    if td_tag[i].get_text() == 'Trace Definitions':
        #print td_tag[i+1].get_text(),"Found successful"
        trace_Def = td_tag[i+1].get_text()
print "Core Definitions:",core_Def,"\nTrace Defintions:",trace_Def
