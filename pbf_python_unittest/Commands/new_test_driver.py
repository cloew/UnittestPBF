from pbf.templates.template_loader import TemplateLoader
from pbf_python_unittest.templates import TemplatesRoot

class NewTestDriver:
    """ Command to create a new Python unittest test driver """
    TEMPLATE_LOADER = TemplateLoader("test_driver.py", TemplatesRoot, defaultFilename="test.py")
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination for the new Test Driver')
    
    def run(self, arguments):
        """ Run the command """
        driverFilename = arguments.destination
        self.createNewTestDriver(driverFilename)
        
    def createNewTestDriver(self, driverFilename):
        """ Create the new Test Driver """
        self.TEMPLATE_LOADER.copy(driverFilename)
