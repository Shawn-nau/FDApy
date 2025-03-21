#!/usr/bin/env python
"""FDApy: a Python package to analyze functional data.

Functional Data Analysis, usually referred as FDA, concerns the field of
Statistics that deals with discrete observations of continuous d-dimensional
functions.

This package provide modules for the analysis of such data. It includes
methods for different dimensional data as well as irregularly sampled
functional data. An implementation of (multivariate) functional principal
component analysis is also given. Moreover, a simulation toolbox is provided.
It might be used to simulate different clusters of functional data.

Check out the `documentation <https://fdapy.readthedocs.io/en/stable/>`_ for
more complete information on the available features within the package.
"""
import Cython.Build

from setuptools import Extension, find_packages, setup


DOCLINES = (__doc__ or '').split('\n')

extensions = [
    Extension('FDApy.src.sigma',
              sources=['FDApy/src/sigma.pyx'],
              language='c++')
]

setup(name='FDApy',
      version='0.8.6',
      python_requires='>= 3.7, <4',
      description=DOCLINES[1],
      long_description='\n'.join(DOCLINES[3:]),
      long_description_content_type='text/x-rst',
      classifiers=[
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Mathematics'],
      keywords='functional data analysis',
      url='https://github.com/StevenGolovkine/FDApy',
      author='Steven Golovkine',
      author_email='steven_golovkine@icloud.com',
      license='MIT',
      cmdclass={'build_ext': Cython.Build.build_ext},
      package_dir={'FDApy': 'FDApy'},
      packages=find_packages(),
      install_requires=[
        'csaps >= 1.0.4',
        'Cython >= 0.29.4',
        'ggplot >= 0.11.0',
        'numpy >= 1.20.0, <1.22.0',
        'pandas >= 1.3.0',
        'patsy >= 0.5.0',
        'pygam >= 0.8.0',
        'scikit-learn >= 0.23.0',
        'sktime >= 0.5.0'],
      test_suite='nose.collector',
      tests_require=['nose'],
      # extra_requires={'tests': ['cython']},
      include_package_data=True,
      ext_modules=extensions,
      setup_requires=['cython'],
      zip_safe=False)
