import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.globo.com')
except urllib.error.URLError:
    print('ERROR')
else:
    print('OK')