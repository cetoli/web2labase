import urllib as u
import time as t
import md5
import tempfile as tmp
from elementtidy import TidyHTMLTreeBuilder


rxf = tmp.mktemp()
rx5 = md5.md5('http://www.amk.ca/python/howto/regex/regex.html').hexdigest()
rxd = u.urlretrieve('http://del.icio.us/url/%s'%rx5,filename=rxf)
tree = TidyHTMLTreeBuilder.parse(rxf)
root = tree.getroot()
ns   = '{http://www.w3.org/1999/xhtml}'
awho = [a.text for a in root.findall('.//%sa'%ns) if 'class' in a.keys() and a.attrib['class'] == 'who']
li = [a for a in root.findall('.//%sli'%ns) if a.getchildren()[0].getchildren() and 'class' in a.getchildren()[0].getchildren()[0].keys() and a.getchildren()[0].getchildren()[0].attrib['class'] == 'who']
tagdict=dict([(a.getchildren()[0].getchildren()[0].text, [b.text for b in a.getchildren()[0].getchildren()[1:]]) for a in li])

#criar as pastinhas com tagdict.keys()


#friends=[a.text for a in li[0].getchildren()[0].getchildren()]
#tagdict={}
#d= tagdict[friends[0]]=[a.text for a in li[0].getchildren()[0].getchildren()[1:]]

""" li[0].getchildren()[0].getchildren() 
pega os 'netos' de li, ou seja, who e as tags """
