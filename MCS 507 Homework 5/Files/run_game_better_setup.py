# L-31 MCS 507 Wed 7 Nov 2012 : run_game_better_setup.py

# We build the shared object file run_game_better.so with cython by
# python run_game_better_setup.py build_ext --inplace

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy

ext_modules = [Extension("run_game_better",
                        sources=["run_game_better.pyx"],
                        include_dirs=[numpy.get_include()])]

setup(
  name = 'game of life' ,
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
