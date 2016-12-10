#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


# should be loaded below
__version__ = None

with open('nbtutor/_version.py') as version:
    exec(version.read())

with open('./README.rst') as readme:
    long_description = readme.read()


setup(
    name="nbtutor",
    version=__version__,
    description="Visualize Python code execution in Jupyter Notebook cells",
    long_description=long_description,
    author="Logan Page",
    author_email="page.lg@gmail.com",
    license="BSD 3-Clause",
    url='https://github.com/lgpage/nbtutor',
    keywords="ipython jupyter notebook python tutor visualize code exection",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: IPython",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD 3-Clause License"
    ],
    packages=["nbtutor"],
    install_requires=[
        "notebook",
    ],
    tests_require=[
        "check-manifest",
        "coverage",
        "pytest",
        "pytest-cov",
        "requests",
        "sphinxcontrib-spelling",
    ],
    include_package_data=True,
    entry_points={
        # 'console_scripts': ['nbtutor=nbtutor.export:main'],
    }
)
