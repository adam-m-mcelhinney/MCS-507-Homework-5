from distutils.core import setup, Extension

MOD = 'doubleDouble'
setup(name=MOD,ext_modules=[Extension(MOD, \
  sources=['dd_sqrt.c'], language = "c++", \
  include_dirs=['/usr/local/qd-2.3.9/include'], \
  extra_objects=['/usr/local/qd-2.3.9/src/libqd.a'])])
