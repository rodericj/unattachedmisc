import re
def highlight_doc(doc, query):

    #setup constants
    sh = '[[HIGHLIGHT]]'
    eh = '[[ENDHIGHLIGHT]]'

    #find the offset of the query in the string
    indices = [match.start() for match in re.finditer(query, doc)]

    #if not found, return empty string
    if not len(indices):
        return ""

    retArray = []
    for index in indices:
        #find the sentence boundary before within 100 characters
        segStart = doc[:index].rfind('.')

        #if it's -1, make it a 0, else, make it not the end of the last sentence
        segStart = segStart != -1 and segStart+1 or 0

        #find the sentence boundary after within 100 characters
        segEnd = doc[index:].find('.')
        segEnd = segEnd == -1 and len(doc) or segEnd

        ret =  doc[segStart:index+segEnd+1]

        #add highlight tags
        beginHighlightIndex = ret.find(query)
        endHighlightIndex = beginHighlightIndex + len(query)
        
        splits = ret.split(query)
        ret = splits[0] + sh + query + eh + splits[1]
        retArray.append(ret)

    return retArray[0].lstrip()
