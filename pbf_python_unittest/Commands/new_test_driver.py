from pbf.helpers.file_helper import IsDirectory
from pbf.templates import template_manager

from pbf_python_unittest.templates import TemplatesRoot

import os

class NewTestDriver:
    """ Command to create a new Python unittest test driver """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the new Test Driver')
    
    def run(self, arguments):
        """ Run the command """
        driverFilename = arguments.destination
        self.createNewTestDriver(driverFilename)
        
    def createNewTestDriver(self, driverFilename):
        """ Create the new Test Driver """
        if IsDirectory(driverFilename):
            driverFilename = os.path.join(driverFilename, "test.py")
        template_manager.CopyTemplate(driverFilename, "test_driver.py", templates_directory=TemplatesRoot)
