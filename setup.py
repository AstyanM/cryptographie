#! /usr/bin/env python3
# coding: utf-8


"""All imports"""


from setuptools import setup, find_packages


with open('README.txt') as f_doc:
    my_readme = f_doc.read()

with open('LICENSE.txt', encoding="mbcs") as s_doc:
    my_license = s_doc.read()


setup(
    name='Cryptography Project',
    version='3.8.0',
    packages=find_packages(exclude='tests'),
    license=my_license,
    author='MARTIN Astyan',
    author_email='martin.astyan68@hotmail.com',
    description='A package for the cryptography',
    long_description=my_readme
)
