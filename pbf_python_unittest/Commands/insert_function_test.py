from pbf.helpers.file_helper import GetLinesFromFile, Save

from pbf_python_unittest.templates import TemplatesRoot

from pbf.templates import template_manager

class InsertFunctionTest:
    """ Command to Insert a test class for a function into a pre-existing test file """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('function', action='store', help='Function to create test class for')
        parser.add_argument('testfile', action='store', help='Test File to add test to')
    
    def run(self, arguments):
        """ Run the command """
        functionToTest = arguments.function
        testFilename = arguments.testfile
        print "Inserting Python Test for Function:", functionToTest, "in:", testFilename
        self.insertFunctionTestLogic(functionToTest, testFilename)
        
    def insertFunctionTestLogic(self, functionToTest, testFilename):
        """ Insert Function Test Logic """
        originalLines = GetLinesFromFile(testFilename)
        newLines = self.getTemplateLines(functionToTest)
        
        originalLines[1:1] = newLines
        Save(testFilename, originalLines)
        
    def getTemplateLines(self, functionToTest):
        """ Return the lines from the template file """
        return template_manager.GetTemplateFileLinesWithKeywordsReplaced("functiontest.py", 
                                                                         {"%functionToTest%":functionToTest}, 
                                                                         templates_directory=TemplatesRoot)
