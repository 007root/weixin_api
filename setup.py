#!/usr/bin/env python

sdict = {
    'name': 'weixin_api',
    'version': "0.1.0",
    'packages': ['weixin_api'],
    'zip_safe': False,
    'install_requires': ['requests'],
    'author': 'WZS',
    'classifiers': [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python']
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**sdict)
