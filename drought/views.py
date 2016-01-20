from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.db import connection
#from django.contrib.gis.geos import Point

def init(req):

	#return render_to_response("index.html")
	
	
#def dates(req):
	"""
	Retrieve the list of ssi dates in the db - geoserver
	"""

	data = []
	if req.method == 'GET':		
		cursor = connection.cursor()
		cursor.execute("select date from ag_ndvi_afr order by date;")
		rows = cursor.fetchall()
		i=0
		for row in rows:
			data.append({'data': row[0].date().isoformat()})
			i=i+1
			
		return render_to_response("index.html", {"elenco_date": simplejson.dumps(data) })
		#return HttpResponse (simplejson.dumps(data))
		cursor.close()
	else:
		return HttpResponse('Forbidden',status_code=403)	


