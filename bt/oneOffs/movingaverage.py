import sys
window = 0
try:
	FILE = open(sys.argv[1], 'r')
	window = int(sys.argv[2])
except:
	print "usage: python movingaverage.py <datafile> <moving average window>"
	sys.exit(0)

#this is what we will convert to our CSV
dataList = []
for i in FILE:
	row = i.split(',')	
	#print row
	try:
		dataList.append([row[0], float(row[1])])
		#Set up our window. 
		#   We can take a moving average of the first 
		#	few elements even if we don't have a full window
		windowStart = max(0, len(dataList)-window)
		windowValue = 0

		windowList = [value[1] for value in dataList[windowStart:] ]

		#calculate the moving average
		if len(windowList) > 0:
			windowValue = sum(windowList)/len(windowList)
		else:
			windowValue = 0

		#append the moving average to the last element in the list 
		#	(aka the element we are workiing on)
		dataList[-1].append(windowValue)

	#This means that we hit the header or some other bad data. Skip it.
	except ValueError:
		pass

#Make it a CSV
print "date,amount,%s day average"% window
for data in  dataList:
	print data[0], ",",data[1], ",", data[2]
