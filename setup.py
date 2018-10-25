from setuptools import setup

setup(
  name='HashClose',
  version='0.1',
  packages=['HashClose'],
  license='MIT',
  include_package_data=True,
  long_description=open('README.md', 'r').read(),
  install_requires=[
    'bitarray==0.8.3'
  ],
)
