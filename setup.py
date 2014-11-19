
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="uberpy",
    version="1.0",
    author="Vivan Kumar",
    author_email="vivangkumar@gmail.com",
    description="A pure python wrapper for the Uber API.",
    license="MIT",
    keywords="uber api wrapper library",
    url="https://github.com/vivangkumar/uberpy",
    packages=['uberpy', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License"
    ],
)
