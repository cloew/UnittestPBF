from distutils.core import setup

setup(name='pbf_python_unittest',
      version='0.4.0',
      description="Programmer's Best Friend Utility Extension for the Python Unittest Library",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['pbf_python_unittest', 'pbf_python_unittest.Commands', 
                'pbf_python_unittest.helpers', 'pbf_python_unittest.templates'],
      #package_data = {'pbf_python_unittest.templates':[]}, # Add template files
     )