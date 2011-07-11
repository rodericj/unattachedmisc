import urllib2
import simplejson

query = "http://api.twitter.com/1/geo/search.json?lat=37.797&long=-122.409&granularity=city&accuracy=10000"
query = "http://search.twitter.com/search.json?q=4sq&geocode=37.797,-122.409,10mi"
timeline = urllib2.urlopen(query).read()
timelineObject = simplejson.loads(timeline)

for i in timelineObject['results']:
    print "%(from_user)s %(created_at)s %(text)s" %i
