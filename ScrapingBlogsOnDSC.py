#Get all the links of blogs on Data Science Central Website
import urllib2
import re
import cookielib
from BeautifulSoup import *

#Save the current cookie
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
#Set initial values
pages = 105 #There are 104 pages of blogs
i = 1 #Page Number
src = list() #Store the links of blogs
blogs = open('blogs.txt','w+')
log_error = open('log_error.txt','w+')
while i<=pages:
    url = 'http://www.datasciencecentral.com/profiles/blog/list?page=' + str(i)
    i = i + 1
    try:
        fh = opener.open(url)
        html = fh.read()#Read the webpage
        soup = BeautifulSoup(html)
        tags = soup('a') #Search anchors
        for tag in tags:
            temp = tag.get('href',None)#Find the link
            if 'comment' in temp:continue
            if 'weekly-digest' in temp:continue
            if re.match('(http://www.datasciencecentral.com/profiles/blogs/.+)', temp) and temp not in src:
                src.append(temp)
                blogs.writelines(temp + '\n')
    except:
        print 'error in page',i
        log_error.writelines(url + '\n')#Record those pages unavailable
        continue

#Save all the links for latter usage
log_error.close()   
blogs.close()



