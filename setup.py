#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='wordwide',
    version='1.0.0',
    author='Ayub Farah',
    author_email='razortyphon@Gmail.com',
    description='Use this tool to quickly get defenitions for words without using a browser',
    packages=find_packages(),
    url='https://github.com/ayubf/wordwide',
    license='MIT',
    scripts=['bin/wordwide.py'],
    entry_points = {
        'console_scripts': ['wordwide=wordwide:main'],
    }
)