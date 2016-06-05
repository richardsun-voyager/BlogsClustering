#Read blog contents on http://www.bigdatanews.com/
import urllib2
import re
import os
import cookielib
from BeautifulSoup import *

#Get the cookie
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

#Read the links
os.chdir('E:/My Document/MyProjects/DataScienceCentralProject')
fh = open('blogs3.txt')#Open the file of blog links
log_error = open('BigDataNews/log_error.txt','w+')#Record the inaccessible links
popularity = open('BigDataNews/popularity.txt','w+')#Create a file to record comments, like count and facebook count of each blog
for line in fh:
    try:
        #Find the blog content and save it
        link = line.strip('\n')#Remove the end line characters
        web = opener.open(link)#Connect each blog
        html = web.read()
        soup = BeautifulSoup(html)
        blog = soup.findAll('div',{'class':'xg_user_generated'})#Find the blog contents part in div table
        if(len(blog)>0):
            temp = blog[0]
            contents = temp.text #Read the text of the post body
            t = open('BigDataNews/'+link.lstrip('http://www.bigdatanews.com/profiles/blogs/') + '.txt','w')
            t.write(contents.encode('utf-8'))#Write the blog content
            t.close()
            
        #Record the popularity such as like count, share count, views
        like_count = '0'
        view_count = '0'
        fb_count = '0'

        like = soup.find('div',{'class':'like-count'})
        if like!=None:
            like_count = filter(lambda x:x.isdigit(),like.text.encode('utf-8'))
        view = soup.find('span',{'class':'view-count'})
        if view!=None:
            view_count = view.text.encode('utf-8')
        facebook = soup.find('span',{'class':'pluginCountTextDisconnected'})
        if facebook!=None:
            fb_count = facebook.text.encode('utf-8')
        pop = link + ':like ' + like_count + ',view ' + view_count+  ', facebook ' + fb_count + '\n'
        popularity.write(pop)
        
    except:#If error happens, record it in a log
        print 'Error',link #Print the error
        log_error.write(link)#Record the unvisited webpage
        continue #Go to next one

#Close all file handles
fh.close()
log_error.close()
popularity.close()
    



        
