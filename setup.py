__author__ = 'Vivan'


from distutils.core import setup

setup(
    name = 'uber-py',
    version = '1.0.0',
    author = 'vivangkumar',
    author_email = 'vivangkumar@gmail.com',
    url = 'https://github.com/vivangkumar/uber-py',
    packages = ['uber-py'],
    license = 'LICENSE.txt',
    install_requires = ['httplib2'],
    description = 'A Python wrapper for the Uber API',
    long_description = 'See the GitHub page for more information'
)