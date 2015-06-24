import sys
import json

data = []
response = open("output.txt")
for line in response:
	tweet = json.loads(line)
	#data.append(json.loads(line))
#print type(tweet)

sentdic = {}
sf = open("AFINN-111.txt")
for line in sf:
	word,score = line.split("\t")
        sentdic[word]=int(score)
print sentdic['lmao']
print sentdic['no']
#print sentdic['chills']
