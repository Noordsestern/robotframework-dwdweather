# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='robotframework-dwdweather',
      version='0.0.1',
      author='Markus Stahl',
      author_email='markus.i.sverige@googlemail.com',
      description='Call dwd weather service with Robot Framework',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Noordsestern/robotframework-dwdweather.git',
      keywords='robotframework dwd weather germany',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ],
      install_requires=[
          'robotframework >= 3.1.0,<3.2',
          'dwdweather2 >= 0.9.0',
          'geopy'
      ],
      packages=['DwdWeatherLibrary'],
)