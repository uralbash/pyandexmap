# coding=utf8
import urllib
import urlparse
import urllib2
import json
from pprint import pprint

def showNode(node, level):
    if type(node) == dict:
        for i in node.keys():
            if type(node[i]) in (dict, list, tuple):
                print ' '.join([' '*4*level,
                                 i,
                                 str(type(node[i])),
                                ])
            else:
                print ' '.join([' '*4*level,
                                 i,
                                 str(type(node[i])),
                                 ': ',
                                 '%s' % node[i],
                                ])
            showNode(node[i], level + 1)
    if type(node) in (list, tuple):
        for i in node:
            showNode(i, level + 1)

# It's implemented in Werkzeug as follows:
def url_fix(s, charset='utf-8'):
    """Sometimes you get an URL by a user that just isn't a real
    URL because it contains unsafe characters like ' ' and so on.  This
    function can fix some of the problems in a similar way browsers
    handle data entered by the user:

    >>> url_fix(u'http://de.wikipedia.org/wiki/Elf (Begriffsklärung)')
    'http://de.wikipedia.org/wiki/Elf%20%28Begriffskl%C3%A4rung%29'

    :param charset: The target charset for the URL if the url was
                    given as unicode string.
    """
    if isinstance(s, unicode):
        s = s.encode(charset, 'ignore')
    scheme, netloc, path, qs, anchor = urlparse.urlsplit(s)
    path = urllib.quote(path, '/%')
    qs = urllib.quote_plus(qs, ':&=')
    return urlparse.urlunsplit((scheme, netloc, path, qs, anchor))

def getJSON(address, key):
    """Get latitude longitude from Yandex.maps service.
    """
    yandexGeotaggingApi = url_fix("http://geocode-maps.yandex.ru/1.x/"+\
            "?format=json&geocode=%s&key=%s" % (address, key))
    f = urllib2.urlopen(yandexGeotaggingApi)
    return f.read()

if __name__ == '__main__':
    address = "Екатеринбург 8 марта 13"
    key = "ANpUFEkBAAAAf7jmJwMAHGZHrcKNDsbEqEVjEUtCmufxQMwAAAAAAAAAAAAvVrub"+\
          "VT4btztbduoIgTLAeFILaQ=="
    response = getJSON(address, key)
    data = json.loads(response)['response']['GeoObjectCollection']
    if data['metaDataProperty']['GeocoderResponseMetaData']['found']:
        geoObjects = data['featureMember']
        showNode(geoObjects[0]['GeoObject'], 0);
        print map(float, geoObjects[0]['GeoObject']['Point']['pos'].split(' '))
    else:
        print 'Nothing to find'
