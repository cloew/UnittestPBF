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
    minimumNumberOfArguments = 1
    
    def __init__(self):
        """ Initialize the New Test Command """
        self.insertFunctionTestCommand = InsertFunctionTest()
    
    def run(self, args):
        """ Create the Python unittest file """
        print "Creating Python Test:", args[0]
        self.newTest(args[0])
        
    def newTest(self, path, addTest=True):
        """ Create the Python unittest file """
        template_manager.CopyTemplate(path, "test.py", templates_directory=TemplatesRoot)
        
        if addTest:
            self.insertFunctionTestCommand.insertFunctionTestLogic("functionToTest", path)
            
        TryToAddSuiteToParent(path)
    
    def help(self):
        """ Print the Usage of the New Test Command """
        print "Usage: pbf {category} {command} [path/to/test]".format(category=self.category, command=self.command)
        print "\tWill create a new unittest style test file at the path given"
    
command_manager.RegisterCommand(NewTest)