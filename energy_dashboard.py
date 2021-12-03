'''

docker run -it ^
-p 0.0.0.0:3674:3674 ^
-p 0.0.0.0:3122:3122 ^
-v "E:\dcd_data":/dcd_data/ ^
-v "E:\data":/data/ ^
-v "C:\Users\gaoyu\Documents":/Documents/ ^
yanliang12/yan_sm_download:1.0.1 


mv /jessica/elasticsearch-6.7.1 /jessica/elasticsearch_energy
cp -r /jessica/elasticsearch_energy /dcd_data/es/

'''

import os
import re
import time
import pandas
import jessica_es
from os import listdir
from os.path import isfile, join, exists

es_session = jessica_es.start_es(
	es_path = "/dcd_data/es/elasticsearch_energy",
	es_port_number = "3674")

jessica_es.start_kibana(
	kibana_path = '/jessica/kibana-6.7.1-linux-x86_64',
	kibana_port_number = "3122",
	es_port_number = "3674",
	)

'''
localhost:3122
'''


'''

DELETE energy

PUT energy
{
  "mappings": {
  "doc":{
	    "properties": {
	    }
   }
  }
}

'''


property_es_data = '/data/daily.json'

jessica_es.ingest_json_to_es_index(
	json_file = property_es_data,
	es_index = "energy",
	es_session = es_session,
	document_id_feild = 'document_id',
	)
