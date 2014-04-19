from pbf.helpers.file_helper import IsDirectory
from pbf.Commands import command_manager
from pbf.templates import template_manager

from pbf_python_unittest.templates import TemplatesRoot

import os

class NewTestDriver:
    """ Command to create a new Python unittest test driver """
    category = "new"
    command = "test-driver"
    description = "Create a Python unittest test driver"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        driverFilename = args[0]
        self.createNewTestDriver(driverFilename)
        
    def createNewTestDriver(self, driverFilename):
        """ Create the new Test Driver """
        if IsDirectory(driverFilename):
            driverFilename = os.path.join(driverFilename, "test.py")
        template_manager.CopyTemplate(driverFilename, "test_driver.py", templates_directory=TemplatesRoot)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/test]".format(category=self.category, command=self.command)
        print "Create a Python unittest test driver at the path provided"
    
command_manager.RegisterCommand(NewTestDriver)