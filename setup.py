from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

version_file = open(os.path.join(here, 'pypkg', 'VERSION'))
version = version_file.read().strip()

# Get the long description from the relevant file
with codecs.open(os.path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pypkg',

    # Versions should comply with PEP440. For single-sourced versioning, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version=version,

    description='A sample Python project',
    long_description=long_description,

    # The project URL.
    url='https://github.com/dghubble/pypkg',

    # Author details
    author='Dalton Hubble',
    author_email='dghubble@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        # Project maturity. 
        'Development Status :: 4 - Beta',

        # Intended audience
        'Intended Audience :: Developers',

        # Topic
        'Topic :: Software Development :: Build Tools',

        # License should match "license" above
        'License :: OSI Approved :: MIT License',

        # Python versions supported
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='pypkg setuptools development',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # Run-time package dependencies. These will be installed by pip when your
    # project is installed.
    install_requires=[
        'requests',
    ],

    # Data files included in your packages. If using Python 2.6 or less, 
    # then these have to be included in MANIFEST.in as well.
    package_data={
        'pypkg': ['package_data.dat'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'pypkg=pypkg.main:main',
        ],
    },

    # MANIFEST.in included entries should be included as package data and
    # installed into site-packages 
    include_package_data=True,

    # Default to False unless you specifically intend the package to be
    # installed as an .egg
    zip_safe=False,
)
