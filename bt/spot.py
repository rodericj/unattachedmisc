""" Spot class to determine travel rules for an ant on a grid
usage: python spot.py <x coorinate> <y coordinate> <limit>
"""

import sys
import getopt

class Spot():
	
	def __init__(self, xDimensions, yDimensions):

		#it's best to store them as ints for the neighbor functions
		self.xSpot = int(xDimensions)
		self.ySpot = int(yDimensions)

	def __str__(self):
		#This can be used for the "did we check here" dictionary
		return "("+str(self.xSpot)+","+ str(self.ySpot)+")"

	def isValid(self):
		#removing negatives as there would be an infinite number of 
		# pairs if we can have negatives
		return self.xSpot >= 0 and self.ySpot >= 0
			

	#Neighbor functions
	def getRight(self):
		ret = Spot(self.xSpot + 1, self.ySpot)
		return ret.isValid() and  ret or None
		
	def getLeft(self):
		ret = Spot(self.xSpot - 1, self.ySpot)
		return ret.isValid() and ret or None
		
	def getAbove(self):
		ret = Spot(self.xSpot, self.ySpot + 1)
		return ret.isValid() and ret or None
		
	def getBelow(self):
		ret = Spot(self.xSpot, self.ySpot - 1)
		return ret.isValid() and ret or None
		
	def neighbors(self):
		return[self.getAbove(),
				self.getBelow(),
				self.getLeft(),
				self.getRight()]

	#Our processing			
	def sumDigits(self):
		a = str(self.xSpot)
		b = str(self.ySpot)
		return sum([int(i) for i in list(a+b)])

def runSim(start, limit):
	#dictionary determining if we've checked here yet
	beenChecked = {}

	#The queue of spots to check
	spotQ = []

	#our limit
	if start.sumDigits() <= limit:
		spotQ.append(start)
		beenChecked[str(start)] = None

	for i in spotQ:
		#The queue will grow as we find valid moves. Duplicate checking 
		#   will be minimal as we maintain the beenChecked dictionary
		for j in i.neighbors():
			if j != None and not beenChecked.has_key(str(j)) and j.sumDigits() <= limit: 
				#add it to our black list
				beenChecked[str(j)] = None
		
				#add it to the processing queue
				spotQ.append(j)

			else:
				#it's failed, so we can add it to the beenChecked 
				# dict to speed up the lookup above. This should save on
				# the calculations in sumDigits. Though with a simple
				# addition in sumDigits we don't save much time: only cycles
				beenChecked[str(j)] = True

	print "The ant can go to " +str(len(spotQ)) + " positions."
	#stringed = ''
	#for x in spotQ:
		#stringed += " " + str(x)
	#print str(spotQ[0])
	#print stringed
def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
	except getopt.error, msg: 
		print msg
		print "for help use --help"
		sys.exit(2)

	# process options
	for o, a in opts:
		if o in ("-h", "--help"):
			print __doc__
			sys.exit(0)
	if len(args) != 3:
		print __doc__
		sys.exit(0)
		
	#pre condition setup
	try:
		limit = int(args[2])
		start = Spot(args[0], args[1])	
	except ValueError:
		print __doc__
		sys.exit(0)
		
	# process stuff
	runSim(start, limit)

if __name__=="__main__":
	main()
