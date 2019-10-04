from setuptools import setup, find_packages
import subprocess


def get_git_revision_hash():
    try:
        git_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    except subprocess.CalledProcessError:
        return 'master'
    else:
        return git_hash.decode('ascii').splitlines()[0]


README = 'https://github.com/belak/wagtail-commonmark/blob/{hash}/README.md'
README = README.format(
    hash=get_git_revision_hash()
)


INSTALL_REQUIRES = [
    'bleach>=1.4.2,<2.2',
    'Wagtail>=2.0',
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
    version='0.1',
    description='Commonmark support for Wagtail',
    long_description="Provides CommonMark page field and streamfield block for "
                     "Wagtail. More info: {}".format(README),
    author='Kaleb Elwert',
    author_email='belak@coded.io',
    url='https://github.com/torchbox/wagtail-markdown',
    install_requires=INSTALL_REQUIRES,
    license='zlib',
    packages=find_packages(),
    include_package_data=True,
    classifiers=CLASSIFIERS,
)
