
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "uberipy",
    version = "1.0",
    author = "Vivan Kumar",
    author_email = "vivangkumar@gmail.com",
    description = "A pure python wrapper for the Uber API.",
    license = "MIT",
    keywords = "uber api wrapper library",
    url = "https://github.com/vivangkumar/uberipy",
    packages = ['uberipy', 'tests'],
    long_description = read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers"
        "Topic :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
)
