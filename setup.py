from distutils.core import setup
import nbt
import py2exe

setup(console=['region-fixer.py'], data_files=['COPYING.txt','README.rst','CONTRIBUTORS.txt'])
