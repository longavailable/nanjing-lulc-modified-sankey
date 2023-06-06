# -*- coding: utf-8 -*-
"""
* Updated on 2019/08/07
* Python3
**
* - Concatenate links and nodes for M-Sankey charting
"""

import json
import csv
import pathlib
from pprint import pprint

dataset = {}

# convert nodes.csv to dictionary
filenameNodes = pathlib.Path('nodes.csv')
with open(filenameNodes) as f:
	reader = csv.DictReader(f)
	dataNode = [r for r in reader]	
#pprint(dataNode)

# re-organize nodes into dataset
dataset['nodes'] = []
for row in dataNode:
	dataset['nodes'].append({
		'node': int(row['node']),
		'name': 'Class_' + row['class'] + '_of_' + row['year']
	})

# convert links.csv to dictionary
filenameLinks = pathlib.Path('links-transitionMatrix-lulc-nanjing.csv')
with open(filenameLinks) as f:
	reader = csv.DictReader(f)
	dataLink=[r for r in reader]

# for-loop zones
for zone in range(1,22):
	# re-organize links into dataset
	dataset['links']=[]
	zoneStr = 'Z' + str(zone).zfill(2)
	for row in dataLink:
		#print(row['regionID'])
		if row['regionID'] == zoneStr:
			dataset['links'].append({
				'source': int(row['source']),
				'target': int(row['target']),
				'value': float(row['value'])
			})
	
	# export 
	filename =  pathlib.Path('nanjing_lulc_data_for_msankey/' + zoneStr + '_1985-2000-2015.json')
	with open(filename,'w') as outfile:
		json.dump(dataset,outfile)

print('Done')