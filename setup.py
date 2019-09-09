from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='ngenicpy',
   version='1.0',
   description='Python package for simple access to Ngenic Tune API',
   license="Apache License 2.0",
   long_description=long_description,
   author='Simon Falkman',
   author_email='sfalkman@gmail.com',
   url="https://github.com/sfalkman/ngenic-py",
   packages=['ngenicpy'],
   install_requires=['requests']
)
