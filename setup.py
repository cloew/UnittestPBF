from distutils.core import setup

setup(name='pbf.python.unittest',
      version='.2',
      description="Programmer's Best Friend Utility Extension for the Python Unittest Library",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['pbf.python', 'pbf.python.unittest', 'pbf.python.unittest.Commands', 
                'pbf.python.unittest.helpers', 'pbf.python.unittest.templates'],
      #package_data = {'pbf.python.unittest.templates':[]}, # Add template files
     )