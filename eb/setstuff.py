import sys
import re
def evaluate(stream):
    #split out the tuples based on the formula given
    #   -using the findall with the concrete regular 
    #      expression allows us to flex based on spaces
    #   -the regular expression reads as exactly one open paren followed by 
    #      'a' or 'b' or 'A' or 'B' followed by
    #      one or more non alphanumeric, followed by 
    #      one or more digits ending with a closed paren
    group_list = re.findall('\([aAbB]\W+\d+\)', stream)

    #set up the temporary eval variables
    a = 'a'
    b = 'b'

    #put each element in the stream into a tuple for usability
    tuple_list = [eval(x) for x in group_list]
 
    #build the individual sets based on the tuple
    #  run through the list once, 
    #    if 'a', add to the a list, 
    #    if b, at to the b list
    #a = [x[1] for x in tuple_list if x[0] == 'a']
    #b = [x[1] for x in tuple_list if x[0] == 'b']
    set_map = {'a':[],'b':[]}
    for x in tuple_list:
        set_map[x[0]].append(x[1])

    print set_map
    print 'a has', [x for x in a if x not in b], 'which are not in b'
    print 'b has', [x for x in b if x not in a], 'which are not in a'

evaluate(str(sys.argv[1]))
