from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='ngenicpy',
   version='0.1',
   description='Python package for simple access to Ngenic Tune API',
   license="Apache License 2.0",
   long_description=long_description,
   author='Simon Falkman',
   author_email='sfalkman@gmail.com',
   url="https://github.com/sfalkman/ngenic-py",
   packages=find_packages(exclude=["tests"]),
   install_requires=['requests']
)
