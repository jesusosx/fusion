import xbmcaddon
import re
import urllib2
import xbmcaddon
import xbmcplugin
import sys
import cookielib
import urllib
import xbmcgui
import base64



def geturl(url):
    addon = xbmcaddon.Addon()
    username = addon.getSetting('username')
    password = addon.getSetting('password')

    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    login_data = urllib.urlencode({'username' : username, 'password' : password})
    header_string = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
    oup = "aHR0cHM6Ly9qZXN1c29icmVnb24uMDAwd2ViaG9zdGFwcC5jb20vY3BhbmVsL2NoZWtsb2dpbi5waHA="
    oup = base64.b64decode(oup)
    opener.open(oup, login_data)
    f=opener.open(url)
    data=f.read()
    f.close()

    return data


def findall(pattern, searText, flags):

    try:
        return re.findall(pattern, searText, flags)

    except Exception as e:
        return None

		
		
def read3(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.71 Safari/537.36')]
    response = opener.open(url)
    data = response.read()

    return data		