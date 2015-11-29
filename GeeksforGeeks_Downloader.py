import httplib2
from bs4 import BeautifulSoup,SoupStrainer

http=httplib2.Http()

s='http://geeksforgeeks.org/'

to_crawl=[]
crawled=[]

to_crawl.append(s)

status,response=http.request(s)

crawled.append(s)

soup=BeautifulSoup(response,'html.parser')

for links in soup.find_all('a'):
	#print links.get('href')
	to_crawl.append(links.get('href'))

print len(to_crawl)



while len(to_crawl):
	link=to_crawl.pop()
	#print link
	if link not in crawled and link.find('forum')<0 and link.find('geeksforgeeks')>=0:
		print link
		crawled.append(link)
		status,response=http.request(link)
		soup=BeautifulSoup(response,'html.parser')
		for links in soup.find_all('a'):
			node=links.get('href')
			if node not in crawled and node.find('geeksforgeeks')>=0:
				to_crawl.append(node)


amazon=[]
print len(to_crawl)

print len(crawled)

for node in crawled:
	if node.find('amazon')>=0 and node.find('#')<0 and node.find('tag')<0 and node.find('forum')<0:
		amazon.append(node)
		print node


def get_page(page):
	import urllib3
	source=urllib3.urlopen(page)
	return source.read()

def save_as_pdf(s):
	global i
	try:
	    client=pdfcrowd.Client("vkthakur","ed993869e91cf968f0447038f96c85c3");
	    output_file=open('amazon'+str(i)+'.pdf','wb')
	    i=i+1
	    html=get_page(s)
	    client.convertHtml(html,output_file)
	    output_file.close()
	except pdfcrowd.Error,why:
		print 'Failed:',why

print len(amazon)

for page in amazon:
	print page
	save_as_pdf(page)

print "!!..process finished..!!"
