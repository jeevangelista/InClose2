from setuptools import setup

setup(
  name='InClose2',
  version='0.1',
  packages=['InClose2'],
  license='MIT',
  include_package_data=True,
  long_description=open('README.md', 'r').read(),
  install_requires=[
    'bitarray==0.8.3'
  ],
)
