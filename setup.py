import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "damsh",
    version = "0.0.4",
    author = "Adrian Herrera Rodríguez",
    author_email = "adrianlega90@gmail.com",
    description = ("Pequeño shell en Python"),
    license = "PSP",
    keywords = "DAM",
    url = "https://tiernogalvan21.notion.site/tiernogalvan21/PSP-pr-ctica-damsh-4f9fc4366e784ae3ac2c6b3ddff933ba",
    scripts=['damsh.py'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)