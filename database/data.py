import json

## Database functions to call in cogs ##

## read database ##
def read(key, id):
	with open('db.json') as json_file:
		data = json.load(json_file)
	return data[key][id]

## write to database ##
def write(key, id, value):
	with open("replayScript.json", "r+") as jsonFile:
		data = json.load(jsonFile)

	data[key][id] = value

	jsonFile.seek(0)  # rewind
	json.dump(data, jsonFile)
	jsonFile.truncate()
	return True

## append to database list ##
def append(key, id, value):
	with open("replayScript.json", "r+") as jsonFile:
		data = json.load(jsonFile)

	data[key][id] = data[key][id].append(value)

	jsonFile.seek(0)  # rewind
	json.dump(data, jsonFile)
	jsonFile.truncate()
	return True