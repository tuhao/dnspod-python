
import urllib2
import re
import base64

def getIP(content):
        import re
        pattern = re.compile(r"Address:(.*?)<")
        match = pattern.search(content)
        if match:
		return match.group(1)

        return ""

def find_ip(content):
        pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
        return pattern.search(content).group(0)

def get():
        """Get IP from ip138.com"""
        #content = urllib2.urlopen('http://iframe.ip138.com/ic.asp').read()
        #return find_ip(content)
        content = urllib2.urlopen('http://ddns.oray.com/checkip').read()
        return getIP(content).strip()

def get_from_local():
	"""Get wan IP from family router"""
	url = 'http://192.168.0.1/info.htm'
	auth = base64.encodestring('admin:504504')
	headers = {'Authorization':'Basic ' + auth}
	req = urllib2.Request(url, None, headers)
	response = urllib2.urlopen(req)
	ret = response.read()
	response.close()
	return find_ip(ret)
