import urllib,json

def ReturnRes(a):
	results =[]
	JsonFile = json.loads(a)
	for i in range(0,len(JsonFile["draws"]["draw"])):
		results.append(JsonFile["draws"]["draw"][i]["results"])

	return results

Numbers = [0 for i in range(80)]
date = raw_input("Input a date in form dd-mm-yyyy (e.g 08-03-2016): ")

url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/"+date+".json"
code = urllib.urlopen(url)
data = code.read()
results = ReturnRes(data)
for i in range(len(results)):
	for j in range(20):
		Numbers[results[i][j]-1] += 1

for i in range(len(Numbers)):
	print i+1, ":", Numbers[i]
