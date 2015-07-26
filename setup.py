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
    'author_email': 'jon@jpweiser.com',
    'version': '0.37.7',
    'install_requires': [],
    'packages': ['cuts'],
    'scripts': ['bin/cuts'],
    'name': 'cuts',
    'classifiers' : [
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD :: BSD/OS",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: Other",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Text Editors",
        "Topic :: Text Editors :: Documentation",
        "Topic :: Text Editors :: Text Processing",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities"],
}

setup(**config)
