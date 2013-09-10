from lxml import etree
import json

ns = {'x': 'http://www.opengis.net/kml/2.2'}
kml = etree.parse('/home/exe-dealer/development/wike/water.kml')
 
features = list()
for placemark in kml.xpath('//x:Placemark', namespaces=ns):
	coords = placemark.xpath('.//x:coordinates/text()', namespaces=ns)[0].split(',')
	name = placemark.xpath('.//x:name/text()', namespaces=ns)[0]
	features.append({
		'type': 'Feature',
		'geometry': {
			'type': 'Point',
			'coordinates': [float(coords[0]), float(coords[1])]
		},
		'properties': {
			'name': name
		}
	})

geojson = json.dumps({
	'type': 'FeatureCollection',
	'features': features
}, sort_keys=False, indent=2)



f = open('/home/exe-dealer/development/wike/water.geojson', 'w')
f.write(geojson)
f.close()