from setuptools import setup
import setuptools
setup(name='GabTools',
      version='0.1.8',
      description='Diverse Python Utilities',
      author='Gabriel Fortin',
      author_email='gabriel.fortin97@gmail.com',
      url='https://www.github.com/gabrielfortin/gabtools',
      tests_require=['pytest'],
      setup_requires=['pytest-runner', 'numpy'],
      packages=setuptools.find_packages(),
     )
