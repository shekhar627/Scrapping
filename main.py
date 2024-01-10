from urllib.request import urlopen
from bs4 import BeautifulSoup
import docx
from category import getCategories

url = 'https://b.hatena.ne.jp'
allLinksByCategoryDict={}
allLinksByCategoryWithTitleDict={}
categories = getCategories(baseUrl=url)


class LinkWithTitle:
    def __init__(self,title,link):
        self.title = title
        self.link = link


#get all links.
def getLinksWithTitle(content):
    linkWithTitle=[]
    soup = BeautifulSoup(content, 'xml')
    allFetchedElements = soup.find_all('item')
    for element in allFetchedElements:
        obj = LinkWithTitle(title=element.find_all('title')[0].contents[0],link=element.find_all('link')[0].contents[0])
        linkWithTitle.append(obj)
    return linkWithTitle



def fillDictionaryWithData():
    for category in categories:
        content = urlopen(url+category).read()
        linksWithTitle = getLinksWithTitle(content)
        allLinksByCategoryDict[category] = linksWithTitle



def getOnlyLinks():
    doc = docx.Document()
    for key,value in allLinksByCategoryDict.items():
        doc.add_heading(key)
        for obj in value:
            doc.add_paragraph(obj.link)
    doc.save('C:\\Users\\shekhar\\Downloads\\links.docx')

def getLinks_Title():
    doc = docx.Document()
    for key,value in allLinksByCategoryDict.items():
        doc.add_heading(key)
        for obj in value:
            doc.add_paragraph('Title: {}'.format(obj.title))
            doc.add_paragraph('Link: {}'.format(obj.link))
    doc.save('C:\\Users\\shekhar\\Downloads\\links_with_title.docx')



fillDictionaryWithData()

getOnlyLinks()

getLinks_Title()




