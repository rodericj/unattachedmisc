#From a phonecall with a friend at Google, this is one of their interview questions
#TODO, finish this
#
#1) character count
#
#
#
#2 english strings. Transform 1 word to the other 1 letter at a time.
#
#input: fog, dig
#output: len(fog dog dig)
#
#maintain: levels away from input, which character we are on*****
#
#[fog:(0,true), cog:(1,false), dog:(1,false)]
#
#assume: isEnglishWord(aString)
#
#######
#
#
#
#shorthand
import sys
alphabet = ['a','b','c','d','e','f', 'g', 'h', 'i' , 'j', 'k' ,'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def isEnglishWord(someString):
     return True

def lengthOfTrain(start, dest):
     distance_from_start = 0
     train_map = {start:(0,False)}
     return evaluateDerivitives(start, dest, train_map, distance_from_start)


def evaluateDerivitives(start, dest, train_map, distance_from_start):
    distance_from_start += 1
    for word in train_map:
        for character_position in range(0,len(word)):
            for char in alphabet:
                #1
                print word, character_position, char
                new_word = word.replace(character_position, char, 1)
                print "we have a new word: ", new_word
                if train_map.get(new_word, False):
                    if new_word == dest:
                        return train_map[new_word][1]
                    if (isEnglishWord(new_word)):
                        tup = (distance_from_start, False)
                        train_map[new_word] = tup
                        evaluateDerivitives(start, dest, train_map, distance_from_start)
                        train_map[new_word][1] = true
                        print train_map
            

print "start train"
lengthOfTrain(sys.argv[1], sys.argv[2])
print "end train"
