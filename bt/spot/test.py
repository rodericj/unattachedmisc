import spot

a = spot.Spot(30,1000)
#print a
print "above: "+ str(a.getAbove()) + " "+ str(a.getAbove().sumDigits())
print "below: "+ str(a.getBelow()) +" " +  str(a.getBelow().sumDigits())
print "left: " + str(a.getLeft()) + " " + str(a.getLeft().sumDigits())
print "right: "+ str(a.getRight()) + " " + str(a.getRight().sumDigits())
