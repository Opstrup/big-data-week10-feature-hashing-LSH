import os
import json


folder = "data/"
data = []
articles = []

for root, dirs, files in os.walk(folder):
 	for f in files:
 		data.append(json.load(open(folder+str(f))))

for jsonObject in data:
	for line in jsonObject:
		if 'topics' in line and 'body' in line:
			articles.append(line)

print(len(articles))
