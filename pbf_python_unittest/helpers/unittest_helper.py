import os
        
def GetTestDirectory(directory):
    """ Return if the given directory has a test directory """
    return os.path.join(directory, "Test")
        
def HasTestDirectory(directory):
    """ Return if the given directory has a test directory """
    return os.path.exists(os.path.join(directory, "Test"))