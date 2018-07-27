import  urllib.request
import urllib.parse
import ssl
import simplejson

# SSLContext to avoid "SSL: CERTIFICATE_VERIFY_FAILED" Error
ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://sampleserver6.arcgisonline.com/arcgis/rest/services/Hurricanes/MapServer?f=json'

search = urllib.request.urlopen( url )

json = simplejson.loads(search.read())

print( 'Version ArcGIS Server :\n\n\t', json['currentVersion'] )
print( 'Layers : \n' )
for layer in json['layers']:
    print('\t', layer['name'])
