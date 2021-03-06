# -*- coding: utf-8 -*-
"""
This module contains the tool of unweb.recipe.ploneftp
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

long_description = (
    read('README.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
   'Download\n'
    '********\n'
    )
entry_point = 'unweb.recipe.ploneftp:Recipe'
entry_points = {"zc.buildout": ["default = %s" % entry_point]}

tests_require=['zope.testing', 'zc.buildout']

setup(name='unweb.recipe.ploneftp',
      version=version,
      description="Buildout recipe to configure an ftp proxy for Plone sites",
      long_description=long_description,
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Zope Public License',
        ],
      keywords='plone zope ftp buildout',
      author='unweb.me',
      author_email='we@unweb.me',
      url='http://svn.plone.org/svn/collective/unweb.recipe.ploneftp/',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['unweb', 'unweb.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout',
                        # -*- Extra requirements: -*-
                        'pyftpdlib',
                        'zc.recipe.egg',
                        'plone.i18n',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'unweb.recipe.ploneftp.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
