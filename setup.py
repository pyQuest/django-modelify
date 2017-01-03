#!/usr/bin/env python

from setuptools import setup


with open('README.md', 'r') as f:
    readme = f.read()

setup(
    author='Piotr Szpetkowski',
    author_email='piotr.szpetkowski@pyquest.space',
    description='Models without reinventing the wheel every time',
    license='BSD-3-Clause',
    long_description=readme,
    maintainer="Piotr Szpetkowski",
    maintainer_email="piotr.szpetkowski@pyquest.space",
    name='django-modelify',
    url='https://django-modelify.readthedocs.io/',
    use_scm_version=True,
    packages=['modelify'],
    install_requires=['django>=1.10.0'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)