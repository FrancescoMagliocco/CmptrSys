#!/usr/bin/env python2
# vim: se fenc=utf8

import urllib2
import json

baseurl = 'services.runescape.com'
response = urllib2.urlopen(
        'http://{0}/m=hiscore/ranking.json?table=9&category=0&size=2'.format(baseurl))

print json.load(response)
