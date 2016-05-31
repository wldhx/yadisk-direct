from setuptools import setup, find_packages
import sys, os

setup(
    name='wldhx.yadisk_direct',
    version='0.0.1',
    description="Get real direct links usable with tools like curl or wget for files stored in Yandex.Disk",
    long_description=open('README.rst').read(),
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    keywords='Yandex.Disk',
    author='wldhx',
    author_email='wldhx+pypi_python_org@wldhx.me',
    url='https://gitlab.com/wldhx/yadisk_direct',
    license='GPLv3',
    packages=find_packages(exclude=['examples', 'tests']),
    zip_safe=True,
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'yadisk_direct = wldhx.yadisk_direct.main:main',
        ],
    })
