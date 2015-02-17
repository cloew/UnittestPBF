from pbf_python.Commands.mk_pydir import MakePyDir

from pbf_python_unittest.helpers.unittest_helper import GetTestDirectory, TryToAddSuiteToParent
from pbf_python_unittest.templates import TemplatesRoot

from pbf.templates import template_manager

import os

class MakePyTestDir:
    """ Makes a Python test Directory """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('directory', action='store', help='Directory to generate Python Test directory')
    
    def run(self, arguments):
        """ Create the Python Test Directory """
        destinationDirectory = arguments.directory
        print "Creating Python Test Directory:", destinationDirectory
        self.makeTestDirectory(destinationDirectory)
        
    def makeTestDirectory(self, dirname):
        """ Make the Test Directory """
        testDirectory = GetTestDirectory(dirname)
        mkPyDir = MakePyDir()
        mkPyDir.makePyDir(testDirectory)
        suiteFilename = os.path.join(testDirectory, "suite.py")
        template_manager.CopyTemplate(suiteFilename, "suite.py", templates_directory=TemplatesRoot)
        TryToAddSuiteToParent(suiteFilename)
