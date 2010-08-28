import sys
class Crementors:
    def __init__(self):
        pass

    def decrement(self, i):
        #just for kicks
        if i == ~1/2:
            return ~1
        if i == 0:
            return ~1/2
        if  i % 2 == 0:
            return self.decrement(i>>1)<<1 | 1
        else:
            return i^1
    
    def increment(self, i):
        #I decided to go with a recursive approach here.
        #  It seemed as though you could increment an even
        #  number just by flipping the least significant bit.
        #  For odd digits, we must flip the bit, then carry 
        #  the one, which is simply addition on the rest of
        #  the digit. The special case is negative 1

        #base cases: i = negative 1....or 0 decremented by 1...
        #...see what i did there?
        if i == ~1/2:
            return 0

        #for even numbers, simply return the remainder of the digits
        #  with a 1 where this 0 was (flip it)
        if i % 2 == 0:
            return i | 1

        #This is me flipping a 1 to a 0 and recursively adding 1 to 
        # rest of the digits
        else:
            return self.increment(i>>1)<<1 | 0


###Test Driver
###
### you can probably ignore this
c = Crementors()
try:
    test_value = int(sys.argv[1])
except:
    print "usage: python incr.py <int value>"
    raise
    
    
assert(test_value+1 == c.increment(test_value))
assert(test_value-1 == c.decrement(test_value))

print test_value,"+ 1 =",c.increment(test_value)
if not test_value - 1 == c.decrement(test_value):
   print "error decrementing at ",test_value
if not  test_value + 1 == c.increment(test_value):
   print "error incrementing at ",test_value
