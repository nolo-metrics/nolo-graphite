#!/usr/bin/env python

from distutils.core import setup

setup(name='nolo-graphite',
      version='1.0',
      description='Graphite adapter for nolo plugins',
      author='Joseph Anthony Pasquale Holsten',
      author_email='joseph@josephholsten.com',
      url='https://github.com/nolo-metrics/nolo-graphite',
      packages=['nolo_graphite'],
      scripts=['nolo-graphite']
)
