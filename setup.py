from setuptools import setup, find_packages
import os

version = '2.0'

setup(name='xtgl.theme',
      version=version,
      description="A diazotheme based Bootstrap3.0.0 for Plone5",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='python plone',
      author='Adam tang',
      author_email='yuejun.tang@gmail.com',
      url='https://github.com/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['xtgl'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          'z3c.caching',   
          # -*- Extra requirements: -*-
      ],
      extras_require={
    'test': ['plone.app.testing',]
        },            
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
