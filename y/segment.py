"""
    'segment' is a function to emulate Yelp's segment highlighting based on a search string

    usage: python segment.py <document> <query>
"""
import sys
import re
import getopt

def highlight_doc(doc, query):
    """Given a doc and a query, return a highlighted segment within the doc
         of the query. 
         For example given:
            doc = "abcdefg"
            query = "cd"
            return "ab[[HIGHLIGHT]]cd[[ENDHIGHLIGHT]]efg"


       This will happen in a few steps:
       1. Find all occurrences of the query
       2. Return if the search string was not found
       3. Split each of the strings into frontHalf, query, backHalf
             'ab', 'cd', 'efg' 
       4. Handle special cases around punctuation
       5. Build the resulting string with the HIGHLIGHT marks
    """

    #setup highlight constants
    SH = '[[HIGHLIGHT]]'
    EH = '[[ENDHIGHLIGHT]]'
    PUNCTUATION = "[\.\?\!]"

    CHOPLENGTH = 50

    #1
    #find the offset of the query in the string
    indices = [match.start() for match in re.finditer(query, doc)]

    #2
    #if not found, return empty string
    if not len(indices):
        return ""

    retArray = []

    #Yes..I'm only returning the first one, I thought it best to build into
    #   the function the ability to return a different section if need be
    for index in indices:
        #3
        #split document by search query
        splitByQuery = doc.split(query)

        #now we have 3 sections, [front of sentence, the query, back of sentence]
        #chop front of sentence at punctuation
        puncPattern = re.compile(PUNCTUATION)
        frontHalf = puncPattern.split(splitByQuery[0])[-1]

        backHalf = splitByQuery[1]

        #4
        #get the first character of the backHalf, assuming it's a non-trivial string
        store = len(backHalf) > 0 and backHalf[0] or 0
  
        #check special case where back half ends in our first punctuation
        backTmpSplit = puncPattern.split(backHalf)
        #if not (len(backTmpSplit) == 2 and len(backTmpSplit[1]) == 0):
        if len(backTmpSplit) != 2 or len(backTmpSplit[1]) != 0:
            #split it
            backHalf = puncPattern.split(backHalf)[0]

        #check special case where first char after query is punctuation
        if store == '.' or store == '?' or store == '!':
            backHalf = backHalf+store

        #5
        #we have to truncate long sentences at some point, hence the CHOPLENGTH
        ret = frontHalf[-50:] + SH + query + EH + backHalf[:CHOPLENGTH]
        retArray.append(ret)

    return retArray[0].lstrip().strip()

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
    if len(args) != 2:
        print __doc__
        sys.exit(0)

    doc, query = args[0], args[1]

    print highlight_doc(doc, query)
    

if __name__=="__main__":
    main()


