import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='doh-json-client',
    url='https://github.com/kacchan822/doh-json-client-py',
    version='0.1.0',
    description='',
    long_description=README,
    author='Katsuya SAITO',
    author_email='hello@skatsuya.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
)
