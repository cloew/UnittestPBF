from pbf.Commands import command_manager
from pbf_python_unittest.Commands.insert_function_test import InsertFunctionTest
from pbf_python_unittest.helpers.unittest_helper import TryToAddSuiteToParent
from pbf_python_unittest.templates import TemplatesRoot
from pbf.templates import template_manager

class NewTest:
    """ Create a New Python Test """
    category = "new"
    command = "test"
    description = "Creates a new Python unittest file"
    
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
        template_manager.CopyTemplate(path, "test.py", templates_directory=TemplatesRoot)
        
        if addTest:
            if function is None:
                function = "functionToTest"
            self.insertFunctionTestCommand.insertFunctionTestLogic(function, path)
            
        TryToAddSuiteToParent(path)
    
    def help(self):
        """ Print the Usage of the New Test Command """
        print "Usage: pbf {category} {command} [path/to/test]".format(category=self.category, command=self.command)
        print "\tWill create a new unittest style test file at the path given"
    
command_manager.RegisterCommand(NewTest)