from pbf.Commands import command_manager
from pbf_python.Commands.mk_pydir import MakePyDir

from pbf_python_unittest.helpers.unittest_helper import GetTestDirectory, TryToAddSuiteToParent
from pbf_python_unittest.templates import TemplatesRoot

from pbf.templates import template_manager

import os

class MakePyTestDir:
    """ Makes a Python test Directory """
    category = "mk"
    command = "testdir"
    description = "Makes a Python Test Directory"
    
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
    
    def help(self):
        """ Print the usage of the Make Test Dir """
        print "Usage: pbf {category} {command} [path/to/dir]".format(category=self.category, command=self.command)
        print "\tWill create a Python Test Directory called Test at the path given"
    
command_manager.RegisterCommand(MakePyTestDir)