# This third_setup.py defines the name of the file where the source is,
# the extension language, the location of the header files to include
# from the QD library and the library to give to the linker.

from distutils.core import setup, Extension

MOD = 'doubleDouble'
setup(name=MOD,ext_modules=[Extension(MOD, \
  sources=['double_double.c'], language = "c++", \
  include_dirs=['/usr/local/qd-2.3.9/include'], \
  extra_objects=['/usr/local/qd-2.3.9/src/libqd.a'])])
