import json
import csv

with open('./blocks.json') as json_file:
    blockjson = json.load(json_file)

block_file = open('blocks.csv','w')
block_writer = csv.writer(block_file)

block_writer.writerow(['name', 'id', 'properties'])
for block in blockjson:
    init = True
    for state in blockjson[block]['states']:
        name = block if init else ' '
        prop = str(state['properties']) if 'properties' in state else ' '
        block_writer.writerow([name, state['id'], prop])
        init = False

block_file.close()

with open('./registries.json') as json_file:
    regjson = json.load(json_file)

item_file = open('items.csv','w')
item_writer = csv.writer(item_file)

item_writer.writerow(['item', 'protocol id'])
for item in regjson['minecraft:item']['entries']:
    pid = regjson['minecraft:item']['entries'][item]['protocol_id']
    item_writer.writerow([item, pid])

item_file.close()
