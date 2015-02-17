from pbf.helpers.file_helper import GetDirname
from pbf.helpers.filename_helper import GetBaseFilenameWithoutExtension

from mk_testdir import MakePyTestDir
from new_test import NewTest
from pbf_python_unittest.helpers.unittest_helper import GetTestDirectory, HasTestDirectory

import os

class NewTestFor:
    """ Command to create a unittest for a given file """
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('fileToTest', action='store', help='File to create the new Python test file for')
        parser.add_argument('function', action='store', nargs='?', default=None, help='The function to test')
    
    def __init__(self):
        """ Initialize the New Test Command """
        self.makeTestDirCommand = MakePyTestDir()
        self.newTestCommand = NewTest()
    
    def run(self, arguments):
        """ Run the command """
        fileToTest = arguments.fileToTest
        print "Creating Python Test for:", fileToTest
        self.newTestFor(fileToTest, function=arguments.function)
        
    def newTestFor(self, fileToTest, function=None):
        """ Create the Python unittest file """
        filedir = GetDirname(fileToTest)
        if not HasTestDirectory(filedir):
            self.makeTestDirCommand.makeTestDirectory(filedir)
            
        testfile = os.path.join(GetTestDirectory(filedir), "{0}_test.py".format(GetBaseFilenameWithoutExtension(fileToTest)))
        self.newTestCommand.newTest(testfile, function=function)
