from setuptools import setup, find_packages
import os, sys

execfile('PySO8601/__version__.py')

setup(name="PySO8601",
      description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
      url="http://unpluggd.github.com/PySO8601",
      version=__version__,
      author=__author__,
      author_email=__author_email__,
      packages=find_packages(exclude="specs"),
      )

