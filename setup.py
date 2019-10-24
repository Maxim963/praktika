from distutils.core import setup
import py2exe

setup(
    windows=[{"script": "Rifmovalka.py"}],
    options={"py2exe": {"includes": ["sip", "qad", "dialog", "sys", "PyQt4"]}},
    zipfile=None

)