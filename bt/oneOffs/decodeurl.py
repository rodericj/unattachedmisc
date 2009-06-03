import re

def htc(m):
    return chr(int(m.group(1),16))

def urldecode(url):
    rex=re.compile('%([0-9a-hA-H][0-9a-hA-H])',re.M)
    return rex.sub(htc,url)

if  __name__ == '__main__':
	FILE = open('data/strippedurls.txt', 'r')
	for i in FILE:
		print urldecode(i)

