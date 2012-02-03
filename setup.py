import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyandexmap',
    version='0.0.2',
    description='Scripts for get data from yandex map API',
    author='Svintsov Dmitry',
    author_email='spam@19216801.ru',
    url='http://github.com/uralbash/pyandexmap/',
    keywords = "yandex map api search ajax geocode geocodding directions\
        navigation json",
    install_requires=[''],
    license='GPL',
    packages=['pyandexmap'],
    long_description=read('README'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Natural Language :: Russian',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
        ],
)
