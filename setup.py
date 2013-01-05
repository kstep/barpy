#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

class Nothing(object):
    def __call__(self, *args, **kw):
        return self
    def __getattr__(self, name):
        return self
    def __setattr__(self, name, value):
        pass
    def __delattr__(self, name):
        pass

    def __str__(self):
        return ''
    __repr__ = __str__

    def __unicode__(self):
        return u''
    def __len__(self):
        return 0

nothing = Nothing()

def maybe(func):
    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except:
            return nothing
    return wrapper

setup(name="barpy",
      version="0.1.2",
      url="http://github.com/kstep/barpy/",
      description="Ruby barby barcodes generating library port to Python",
      long_description=maybe(open)("README.txt").read(),
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

