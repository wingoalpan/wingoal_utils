#!C:\Users\pypy2\AppData\Local\Programs\Python\Python311\python.exe

from __future__ import print_function
from setuptools import setup, find_packages
import sys


setup(
    name="wingoal_utils",
    version="0.1.0",
    author="Wingoal",  # 作者名字
    author_email="panwingoal@gmail.com",
    description="Some helpful functions from Wingoal",
    license="MIT",
    url="https://github.com/wingoalpan/wingoal_utils.git",  # github地址或其他地址
    # packages=find_packages(),
    packages=['wingoal_utils'],
    package_dir={'wingoal_utils': '.'},
    # package_data={'config': ['config/*.json']},
    include_package_data=False,
    classifiers=[
        "Environment :: Windows Environment",
        'Intended Audience :: AI LLM developer',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.11',
    ],
    install_requires=[],
    zip_safe=True,
)
