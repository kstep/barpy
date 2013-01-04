#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(name="barpy",
      version="0.1",
      description="Ruby barby barcodes generating library port to Python",
      long_description=open("README.md").read(),
      author="Konstantin Stepanov",
      author_email="me@kstep.me",
      license="BSD",
      packages=find_packages(),
      install_requires=[
          'PIL', 'qrcode'
          ]
      )

