#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of convertdate.
# http://github.com/fitnr/convertdate

# Licensed under the MIT license:
# http://opensource.org/licenses/MIT
# Copyright (c) 2016, fitnr <fitnr@fakeisthenewreal>
from setuptools import setup


try:
    readme = open('README.md').read()
except IOError:
    readme = ''

with open('src/convertdate/__init__.py') as i:
    version = next(r for r in i.readlines() if '__version__' in r).split('=')[1].strip('"\' \n')

tests_require = [
    "coverage",
]

setup(
    name="convertdate",
    version=version,
    description=("Converts between Gregorian dates and other calendar systems."
                 "Calendars included: Baha'i, French Republican, Hebrew, "
                 "Indian Civil, Islamic, ISO, Julian, Mayan and Persian."),
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Neil Freeman",
    license='MIT',
    author_email="contact@fakeisthenewreal.org",
    url="https://github.com/fitnr/convertdate",
    packages=['convertdate', 'convertdate.data'],
    package_dir={'convertdate': 'src/convertdate'},
    zip_safe=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Religion',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires=">=3.5",
    install_requires=[
        'pytz>=2014.10',
        'pymeeus>=0.3.13, <=1'
    ],
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'docs': [
            'sphinx',
            'sphinx_rtd_theme'
        ]
    }
)
