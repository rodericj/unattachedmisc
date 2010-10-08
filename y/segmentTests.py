import unittest
import segment
import testStrings

class TestUnitTest(unittest.TestCase):
    def testGivenTest(self):
        res = segment.highlight_doc(testStrings.given_doc, testStrings.given_query)
        assert res == testStrings.given_result
    #multiple matches
    def testPizzaHacker(self):
        res = segment.highlight_doc(testStrings.pizzahacker, testStrings.pizzahacker_query)
        assert res == testStrings.pizzahacker_result

    def testGottsRoadSide(self):
        res = segment.highlight_doc(testStrings.cheeseburger_doc, testStrings.cheeseburger_query)
        assert res == testStrings.cheeseburger_result

    #whole document
    def testWholeDocumentMatches(self):
        res = segment.highlight_doc(testStrings.whole_doc, testStrings.whole_query)
        assert res == testStrings.whole_result
        
    def testQueryNotFound(self):
        res = segment.highlight_doc(testStrings.notfound_doc, testStrings.notfound_query)
        assert res == testStrings.notfound_result

    #unicode type things
    def testUnicode(self):
        res = segment.highlight_doc(testStrings.unicode_doc, testStrings.unicode_query)
        assert res == testStrings.unicode_result
    
#invalid input




suite = unittest.makeSuite(TestUnitTest, 'test')
runner = unittest.TextTestRunner()
runner.run(suite)
