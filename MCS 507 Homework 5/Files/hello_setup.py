# L-31 MCS 507 Wed 7 Nov 2012 : hello_setup.py

# We build the shared object file hello.so with cython by
# python hello_setup.py build_ext --inplace

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("hello", ["hello.pyx"])]

setup(
  name = 'hello world' ,
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
