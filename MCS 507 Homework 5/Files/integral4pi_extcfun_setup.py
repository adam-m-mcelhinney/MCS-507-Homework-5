# L-31 MCS 507 Wed 7 Nov 2012 : integral4pi_extcfun_setup.py

# We build the shared object file integral4pi_typed.so with cython by
# python integral4pi_extcfun_setup.py build_ext --inplace

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("integral4pi_extcfun",
                        ["integral4pi_extcfun.pyx"])]

setup(
  name = 'integral approximation for pi' ,
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
