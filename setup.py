import os
import pakietanalizy
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

setup(
    name='PakietAnalizy',
    version=pakietanalizy.__version__,
    description='Aplikacja: pakiet analityczny',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python", ],
    author='Piotr Czaja',
    author_email='czaja_piotr@o2.pl',
    url='http://piotr.czaja.link',
    keywords='python analysis',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['wykonaj-obliczenia = pakietanalizy.wykonaj:main', ]
        },
    platforms='any',
      )
