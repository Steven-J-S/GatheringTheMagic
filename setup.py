"""
Setup for GatheringTheMagic
"""

from distutils.core import setup

with open('README') as file:
    readme = file.read()

setup(
    name='GatheringTheMagic',
    version='1.0.0',
    packages=['game'],
    license='LICENSE.txt',
    lsong_description=readme
)
