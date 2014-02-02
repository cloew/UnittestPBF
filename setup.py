from distutils.core import setup

setup(name='pbf.python.unittest',
      version='.1',
      description="Programmer's Best Friend Utility Extension for Unittest",
      author='', # Add your name here
      author_email='', # Add your e-mail here
      packages=['pbf.python', 'pbf.python.unittest', 'pbf.python.unittest.Commands', 
                'pbf.python.unittest.helpers', 'pbf.python.unittest.templates'],
      #package_data = {'pbf.python.unittest.templates':[]}, # Add template files
     )