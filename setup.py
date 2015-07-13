#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Remove and/or rearrange sections from each line of a file(s).',
    'author': 'J.P. Weiser',
    'url': 'https://github.com/jpweiser/cuts',
    'download_url': 'https://github.com/jpweiser/cuts/tarball/master',
    'author_email': 'jpweiser@email.arizona.edu',
    'version': '0.37',
    'install_requires': [],
    'packages': ['cuts'],
    'scripts': ['bin/cuts'],
    'name': 'cuts'
}

setup(**config)
