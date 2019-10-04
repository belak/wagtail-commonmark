from setuptools import setup, find_packages

from os import path
README_PATH = path.join(path.abspath(path.dirname(__file__)), 'README.md')
with open(README_PATH, encoding='utf-8') as f:
    long_description = f.read()


INSTALL_REQUIRES = [
    'bleach>=3.0,<4.0',
    'commonmark>=0.8,<0.10'
    'Wagtail>=2.0,<3.0',
]


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Wagtail',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python',
]


setup(
    name='wagtail-commonmark',
    version='0.1.1',
    description='Commonmark support for Wagtail',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kaleb Elwert',
    author_email='belak@coded.io',
    url='https://github.com/belak/wagtail-commonmark',
    install_requires=INSTALL_REQUIRES,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    classifiers=CLASSIFIERS,
)
