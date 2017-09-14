import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import urllib2
import socket
import xbmcaddon
import datetime
import re
import os
import defin
import base64
import requests
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP


addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])




xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

if mode is None:
    finder = "aHR0cHM6Ly9qZXN1c29icmVnb24uMDAwd2ViaG9zdGFwcC5jb20vY3BhbmVsL2NhdGVnb3JpZXMvaW5kZXgucGhw"
    finder = base64.b64decode(finder)
    data = defin.geturl(finder)
    pattern = "<ppal(.*?)<\/ppal"
    matches = defin.findall(pattern, data, re.IGNORECASE)
    for match in matches:

        pattern = '.*?title.*?lue=(.*?)\/'
        name = defin.findall(pattern, match, re.IGNORECASE)[0]
        name = base64.b64decode(name)

        pattern = '.*?thum.*?lue=(.*?)\/>'
        thumbnail = defin.findall(pattern, match, re.IGNORECASE)[0]
        thumbnail = base64.b64decode(thumbnail)

        pattern = '.*?fana.*?lue=(.*?)\/>'
        fanart = defin.findall(pattern, match, re.IGNORECASE)[0]
        fanart = base64.b64decode(fanart)

        pattern = '.*?info.*?lue=(.*?)\/>'
        info = defin.findall(pattern, match, re.IGNORECASE)[0]
        info = base64.b64decode(info)

        pattern = '.*?link.*?lue=(.*?)\/>'
        enlace = defin.findall(pattern, match, re.IGNORECASE)[0]
        enlace = base64.b64decode(enlace)

        url = build_url({'mode': 'categorias', 'foldername': name, 'direccion': enlace})
        li = xbmcgui.ListItem(name, iconImage='DefaultFolder.png', thumbnailImage=thumbnail)
        li.setInfo("video", {"Title": name, "FileName": name, "Plot": info})
        li.setProperty('fanart_image', fanart)
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'categorias':
    foldername = args['foldername'][0]
    dir = args['direccion'][0]
    name = args['foldername'][0]
    dominio = dir
    if name =='Peliculas':
        html = defin.geturl(dominio)
        pattern = "<ppal(.*?)<\/ppal"
        matches = defin.findall(pattern, html, re.MULTILINE)
        for match in matches:
            pattern = 'title.*?value=\'(.*?)\''
            name = defin.findall(pattern, match, re.MULTILINE)[0]

            thumbnail = ''

            fanart = ''

            info = ''

            pattern = 'link.*?value=\'(.*?)\''
            enlace = defin.findall(pattern, match, re.MULTILINE)[0]

            url = build_url({'mode': 'peliculas', 'foldername': name, 'direccion': enlace})
            li = xbmcgui.ListItem(name, iconImage='DefaultFolder.png', thumbnailImage=thumbnail)
            li.setInfo("video", {"Title": name, "FileName": name, "Plot": info})
            li.setProperty('fanart_image', fanart)
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                        listitem=li, isFolder=True)
        xbmcplugin.endOfDirectory(addon_handle)

    elif name =='ZonaX':
        addon = xbmcaddon.Addon()
        parental = addon.getSetting('parental')
        keyboard = xbmc.Keyboard("", "Poner el Password de Control parental?", False)
        keyboard.setHiddenInput(True)
        keyboard.doModal()
        if keyboard.getText() == parental:
            html = defin.geturl(dominio)
            pattern = "<ppal(.*?)<\/ppal"
            matches = defin.findall(pattern, html, re.MULTILINE)
            for match in matches:
                pattern = 'title.*?value=\'(.*?)\''
                name = defin.findall(pattern, match, re.MULTILINE)[0]

                thumbnail = ''

                fanart = ''

                info = ''

                pattern = 'link.*?value=\'(.*?)\''
                enlace = defin.findall(pattern, match, re.MULTILINE)[0]

                url = build_url({'mode': 'xxx', 'foldername': name, 'direccion': enlace})
                li = xbmcgui.ListItem(name, iconImage='DefaultFolder.png', thumbnailImage=thumbnail)
                li.setInfo("video", {"Title": name, "FileName": name, "Plot": info})
                li.setProperty('fanart_image', fanart)
                xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                            listitem=li, isFolder=True)
            xbmcplugin.endOfDirectory(addon_handle)

        else:
            addon = xbmcaddon.Addon()
            addonname = addon.getAddonInfo('name')

            line1 = "Favor de poner el Password correcto Pide ayuda a tus Padres :)"

            xbmcgui.Dialog().ok(addonname, line1)

    elif name =='Television':
        html = defin.geturl(dominio)
        pattern = "<ppal(.*?)<\/ppal"
        matches = defin.findall(pattern, html, re.MULTILINE)
        for match in matches:
            pattern = 'title.*?lue=(.*?)\/'
            title = defin.findall(pattern, match, re.MULTILINE)[0]
            title = base64.b64decode(title)

            pattern = 'thumb.*?lue=(.*?)\/'
            thumbnail = defin.findall(pattern, match, re.MULTILINE)[0]
            thumbnail = base64.b64decode(thumbnail)

            pattern = 'fanart.*?lue=(.*?)\/'
            fanart = defin.findall(pattern, match, re.MULTILINE)[0]
            fanart = base64.b64decode(fanart)

            pattern = 'info.*?lue=(.*?)\/'
            info = defin.findall(pattern, match, re.MULTILINE)[0]
            info = base64.b64decode(info)

            pattern = 'link.*?lue=(.*?)\/'
            url = defin.findall(pattern, match, re.MULTILINE)[0]
            url = base64.b64decode(url)

            li = xbmcgui.ListItem(title, iconImage='DefaultFolder.png', thumbnailImage=thumbnail)
            li.setInfo("video", {"Title": title, "FileName": title, "Plot": info})
            li.setProperty('fanart_image', fanart)
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                        listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)


    elif name =='Series':
        html = defin.geturl(dominio)
        pattern = "<ppal(.*?)<\/ppal"
        matches = defin.findall(pattern, html, re.MULTILINE)
        for match in matches:
            pattern = 'name.*?lue=(.*?)\/'
            name = defin.findall(pattern, match, re.MULTILINE)[0]
            name = base64.b64decode(name)

            pattern = 'thumb.*?lue=(.*?)\/'
            thumbnail = defin.findall(pattern, match, re.MULTILINE)[0]
            thumbnail = base64.b64decode(thumbnail)

            pattern = 'fanart.*?lue=(.*?)\/'
            fanart = defin.findall(pattern, match, re.MULTILINE)[0]
            fanart = base64.b64decode(fanart)

            pattern = 'info.*?lue=(.*?)\/'
            info = defin.findall(pattern, match, re.MULTILINE)[0]
            info = base64.b64decode(info)

            pattern = 'enlace.*?lue=(.*?)\/'
            enlace = defin.findall(pattern, match, re.MULTILINE)[0]
            enlace = base64.b64decode(enlace)

            url = build_url({'mode': 'series', 'foldername': name, 'direccion': enlace})
            li = xbmcgui.ListItem(name, iconImage='DefaultFolder.png', thumbnailImage=thumbnail)
            li.setInfo("video", {"Title": name, "FileName": name, "Plot": info})
            li.setProperty('fanart_image', fanart)
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                        listitem=li, isFolder=True)
        xbmcplugin.endOfDirectory(addon_handle)


    elif name =='Anime':
        html = defin.geturl(dominio)
        pattern = "<ppal(.*?)<\/ppal"
        matches = defin.findall(pattern, html, re.MULTILINE)
        for match in matches:
            pattern = 'name.*?lue=(.*?)\/'
            name = defin.findall(pattern, match, re.MULTILINE)[0]
            name = base64.b64decode(name)

            pattern = 'thumb.*?lue=(.*?)\/'
            thumbnail = defin.findall(pattern, match, re.MULTILINE)[0]
            thumbnail = base64.b64decode(thumbnail)

            pattern = 'fanart.*?lue=(.*?)\/'
            fanart = defin.findall(pattern, match, re.MULTILINE)[0]
            fanart = base64.b64decode(fanart)

            pattern = 'info.*?lue=(.*?)\/'
            info = defin.findall(pattern, match, re.MULTILINE)[0]
            info = base64.b64decode(info)

            pattern = 'enlace.*?lue=(.*?)\/'
            enlace = defin.findall(pattern, match, re.MULTILINE)[0]
            enlace = base64.b64decode(enlace)

            url = build_url({'mode': 'anime', 'foldername': name, 'direccion': enlace})
            li = xbmcgui.ListItem(name, iconImage='DefaultFolder.png', thumbnailImage=thumbnail)
            li.setInfo("video", {"Title": name, "FileName": name, "Plot": info})
            li.setProperty('fanart_image', fanart)
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                        listitem=li, isFolder=True)
        xbmcplugin.endOfDirectory(addon_handle)



    elif name == 'Infantil':
        html = defin.geturl(dominio)
        pattern = "<ppal>(.*?)<\/ppal>"
        items = defin.findall(pattern, html, re.MULTILINE)

        for item in items:
            # Not the better way to parse XML, but clean and easy
            pattern = '.*title.*?=(.*?)\/>'
            title = defin.findall(pattern, item, re.IGNORECASE)[0]
            title = base64.b64decode(title)

            pattern = '.*info.*?=(.*?)\/>'
            plot = defin.findall(pattern, item, re.IGNORECASE)[0]
            plot = base64.b64decode(plot)

            pattern = '.*thum.*?=(.*?)\/>'
            thumbnail = defin.findall(pattern, item, re.IGNORECASE)[0]
            thumbnail = base64.b64decode(thumbnail)

            pattern = '.*fanart.*?=(.*?)\/>'
            fanart = defin.findall(pattern, item, re.IGNORECASE)[0]
            fanart = base64.b64decode(fanart)

            pattern = '.*lin.*?=(.*?)\/>'
            url = defin.findall(pattern, item, re.IGNORECASE)[0]
            url = base64.b64decode(url)

            if 'rapidvideo' in url:
                req = defin.read3(url)
                pattern = 'source.*src=\"(.*?)\"'
                url = defin.findall(pattern, req, re.IGNORECASE)[0]

            url = build_url(
                {'mode': 'infantiles1', 'foldername': title, 'direccion': url, 'thumbnail': thumbnail, 'fanart': fanart,
                 'info': plot})
            li = xbmcgui.ListItem(title, iconImage=thumbnail, thumbnailImage=thumbnail)
            li.setInfo("video", {"Title": title, "FileName": title, "Plot": plot})
            li.setProperty('fanart_image', fanart)

            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
        xbmcplugin.endOfDirectory(addon_handle)






elif mode[0] == 'anime':
        foldername = args['foldername'][0]
        dir = args['direccion'][0]
        dominio = dir
        html = defin.geturl(dominio)
        pattern = "<ppal>(.*?)<\/ppal>"
        items = defin.findall(pattern, html, re.MULTILINE)


        for item in items:
            # Not the better way to parse XML, but clean and easy
            pattern = '.*title.*?=(.*?)\/>'
            title = defin.findall(pattern, item, re.IGNORECASE)[0]
            title = base64.b64decode(title)

            pattern = '.*info.*?=(.*?)\/>'
            plot = defin.findall(pattern, item, re.IGNORECASE)[0]
            plot = base64.b64decode(plot)

            pattern = '.*thum.*?=(.*?)\/>'
            thumbnail = defin.findall(pattern, item, re.IGNORECASE)[0]
            thumbnail = base64.b64decode(thumbnail)

            pattern = '.*fanart.*?=(.*?)\/>'
            fanart = defin.findall(pattern, item, re.IGNORECASE)[0]
            fanart = base64.b64decode(fanart)

            pattern = '.*lin.*?=(.*?)\/>'
            url = defin.findall(pattern, item, re.IGNORECASE)[0]
            url = base64.b64decode(url)

            if 'rapidvideo' in url:
                req = defin.read3(url)
                pattern = 'source.*src=\"(.*?)\"'
                url = defin.findall(pattern, req, re.IGNORECASE)[0]


            li = xbmcgui.ListItem(title, iconImage=thumbnail, thumbnailImage=thumbnail)
            li.setInfo("video", {"Title": title, "FileName": title, "Plot": plot})
            li.setProperty('fanart_image', fanart)

            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url , listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)



elif mode[0] == 'series':
        foldername = args['foldername'][0]
        dir = args['direccion'][0]
        dominio = dir
        html = defin.geturl(dominio)
        pattern = "<ppal>(.*?)<\/ppal>"
        items = defin.findall(pattern, html, re.MULTILINE)


        for item in items:
            # Not the better way to parse XML, but clean and easy
            pattern = '.*title.*?=(.*?)\/>'
            title = defin.findall(pattern, item, re.IGNORECASE)[0]
            title = base64.b64decode(title)

            pattern = '.*info.*?=(.*?)\/>'
            plot = defin.findall(pattern, item, re.IGNORECASE)[0]
            plot = base64.b64decode(plot)

            pattern = '.*thum.*?=(.*?)\/>'
            thumbnail = defin.findall(pattern, item, re.IGNORECASE)[0]
            thumbnail = base64.b64decode(thumbnail)

            pattern = '.*fanart.*?=(.*?)\/>'
            fanart = defin.findall(pattern, item, re.IGNORECASE)[0]
            fanart = base64.b64decode(fanart)

            pattern = '.*lin.*?=(.*?)\/>'
            url = defin.findall(pattern, item, re.IGNORECASE)[0]
            url = base64.b64decode(url)

            if 'rapidvideo' in url:
                req = defin.read3(url)
                pattern = 'source.*src=\"(.*?)\"'
                url = defin.findall(pattern, req, re.IGNORECASE)[0]


            li = xbmcgui.ListItem(title, iconImage=thumbnail, thumbnailImage=thumbnail)
            li.setInfo("video", {"Title": title, "FileName": title, "Plot": plot})
            li.setProperty('fanart_image', fanart)

            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url , listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)













elif mode[0] == 'peliculas':
        foldername = args['foldername'][0]
        dir = args['direccion'][0]
        dominio = dir
        html = defin.geturl(dominio)
        pattern = "<ppal>(.*?)<\/ppal>"
        items = defin.findall(pattern, html, re.MULTILINE)


        for item in items:
            # Not the better way to parse XML, but clean and easy
            pattern = '.*title.*?=(.*?)\/>'
            title = defin.findall(pattern, item, re.IGNORECASE)[0]
            title = base64.b64decode(title)

            pattern = '.*info.*?=(.*?)\/>'
            plot = defin.findall(pattern, item, re.IGNORECASE)[0]
            plot = base64.b64decode(plot)

            pattern = '.*thum.*?=(.*?)\/>'
            thumbnail = defin.findall(pattern, item, re.IGNORECASE)[0]
            thumbnail = base64.b64decode(thumbnail)

            pattern = '.*fanart.*?=(.*?)\/>'
            fanart = defin.findall(pattern, item, re.IGNORECASE)[0]
            fanart = base64.b64decode(fanart)

            pattern = '.*lin.*?=(.*?)\/>'
            url = defin.findall(pattern, item, re.IGNORECASE)[0]
            url = base64.b64decode(url)

            if 'rapidvideo' in url:
                req = defin.read3(url)
                pattern = 'source.*src=\"(.*?)\"'
                url = defin.findall(pattern, req, re.IGNORECASE)[0]


            url = build_url({'mode': 'peliculas1', 'foldername': title, 'direccion': url, 'thumbnail': thumbnail, 'fanart': fanart, 'info': plot})
            li = xbmcgui.ListItem(title, iconImage=thumbnail, thumbnailImage=thumbnail)
            li.setInfo("video", {"Title": title, "FileName": title, "Plot": plot})
            li.setProperty('fanart_image', fanart)

            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url , listitem=li, isFolder=True)
        xbmcplugin.endOfDirectory(addon_handle)



elif mode[0] == 'infantil1':
        dir = args['direccion'][0]
        url = dir
        title = dir

        if 'rapidvideo' in title:
            title = 'Servidor Rapidvideo'
            req = defin.read3(url)
            pattern = 'source.*src=\"(.*?)\"'
            url = defin.findall(pattern, req, re.IGNORECASE)[0]

        elif 'goo.gl' in title:
            title = 'Servidor Onedrive'




        thumbnail = args['thumbnail'][0]
        fanart = args['fanart'][0]
        plot = args['info'][0]




        li = xbmcgui.ListItem(title, iconImage=thumbnail, thumbnailImage=thumbnail)
        li.setInfo("video", {"Title": title, "FileName": title, "Plot": plot})
        li.setProperty('fanart_image', fanart)
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)







elif mode[0] == 'peliculas1':
        dir = args['direccion'][0]
        url = dir
        title = dir

        if 'rapidvideo' in title:
            title = 'Servidor Rapidvideo'
            req = defin.read3(url)
            pattern = 'source.*src=\"(.*?)\"'
            url = defin.findall(pattern, req, re.IGNORECASE)[0]

        elif 'goo.gl' in title:
            title = 'Servidor Onedrive'




        thumbnail = args['thumbnail'][0]
        fanart = args['fanart'][0]
        plot = args['info'][0]




        li = xbmcgui.ListItem(title, iconImage=thumbnail, thumbnailImage=thumbnail)
        li.setInfo("video", {"Title": title, "FileName": title, "Plot": plot})
        li.setProperty('fanart_image', fanart)
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)












elif mode[0] == 'xxx':
        foldername = args['foldername'][0]
        dir = args['direccion'][0]
        dominio = dir
        html = defin.read3(dominio)
        pattern = "<div id=\"video(.*<\/)div"
        items = defin.findall(pattern, html, re.MULTILINE)


        for item in items:
            # Not the better way to parse XML, but clean and easy
            pattern = '.*title=\"(.*?)\"'
            title = defin.findall(pattern, item, re.IGNORECASE)[0]

            pattern = ''
            plot = defin.findall(pattern, item, re.IGNORECASE)[0]

            pattern = '.*src=\"(.*?)\"'
            thumbnail = defin.findall(pattern, item, re.IGNORECASE)[0]

            pattern = ''
            fanart = defin.findall(pattern, item, re.IGNORECASE)[0]

            pattern = '.*?href=\"(.*?)\"><im'
            host = defin.findall(pattern, item, re.IGNORECASE)[0]
            if 'video' in host:
                url = 'https://www.xvideos.com' + host
                url = build_url({'mode': 'xxx2', 'direccion': url, 'thumbnail': thumbnail})
                li = xbmcgui.ListItem(title, iconImage=thumbnail, thumbnailImage=thumbnail)
                li.setInfo("video", {"Title": title, "FileName": title, "Plot": plot})
                li.setProperty('fanart_image', fanart)

                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)

        xbmcplugin.endOfDirectory(addon_handle)



elif mode[0] == 'xxx2':
        dir = args['direccion'][0]
        thumbnail = args['thumbnail'][0]
        dominio = dir
        html = defin.geturl(dominio)
        pattern = "oHLS\(\'(.*?)\'\)"
        url = defin.findall(pattern, html, re.IGNORECASE)[0]
        li = xbmcgui.ListItem('Reproducir Ahora', iconImage=thumbnail, thumbnailImage=thumbnail)
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)
