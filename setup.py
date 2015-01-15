"""Setup script of blogger2zinnia"""
from setuptools import setup
from setuptools import find_packages

import zinnia_blogger

setup(
    name='blogger2zinnia',
    version=zinnia_blogger.__version__,

    description='Import your Blogger blog into Zinnia',
    long_description=open('README.rst').read(),

    keywords='django, zinnia, blogger',

    author=zinnia_blogger.__author__,
    author_email=zinnia_blogger.__email__,
    url=zinnia_blogger.__url__,

    packages=find_packages(exclude=['demo_zinnia_blogger']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=zinnia_blogger.__license__,
    include_package_data=True,
    zip_safe=False,
    install_requires=['gdata>=2.0.18']
)
