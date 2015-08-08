from pbf_python_unittest.Commands.insert_function_test import InsertFunctionTest
from pbf.templates.template_loader import TemplateLoader
from pbf_python_unittest.templates import TemplatesRoot

class NewTest:
    """ Create a New Python Test """
    TEMPLATE_LOADER = TemplateLoader("test.py", TemplatesRoot)
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the new Python test file')
        parser.add_argument('function', action='store', nargs='?', default=None, help='The function to test')
    
    def __init__(self):
        """ Initialize the New Test Command """
        self.insertFunctionTestCommand = InsertFunctionTest()
    
    def run(self, arguments):
        """ Create the Python unittest file """
        destination = arguments.destination
        print "Creating Python Test:", destination
        self.newTest(destination, function=arguments.function)
        
    def newTest(self, path, addTest=True, function=None):
        """ Create the Python unittest file """
        self.TEMPLATE_LOADER.copy(path)
        
        if addTest:
            if function is None:
                function = "functionToTest"
            self.insertFunctionTestCommand.insertFunctionTestLogic(function, path)
