#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(name="barpy",
      version="0.1",
      url="http://github.com/kstep/barpy/",
      description="Ruby barby barcodes generating library port to Python",
      long_description=open("README.txt").read(),
      author="Konstantin Stepanov",
      author_email="me@kstep.me",
      license="BSD",
      packages=find_packages(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: BSD License',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries'
          ],
      install_requires=[
          'PIL', 'qrcode'
          ]
      )

