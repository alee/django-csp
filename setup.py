import sys
import os
import codecs
from setuptools import setup, find_packages


version = '3.7'


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    print('You probably want to also tag the version now:')
    print('  git tag -a %s -m "version %s"' % (version, version))
    print('  git push --tags')
    sys.exit()


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


install_requires = [
    'Django>=2.2',
]

jinja2_requires = [
    'jinja2>=2.9.6',
]

test_requires = [
    'pytest<4.0',
    'pytest-cov',
    'pytest-django',
    'pytest-flakes==1.0.1',
    'pytest-pep8==1.0.6',
    'pep8==1.4.6',
    'mock==1.0.1',
    'six==1.12.0',
]

test_requires += jinja2_requires


setup(
    name='django_csp',
    version=version,
    description='Django Content Security Policy support.',
    long_description=read('README.rst'),
    author='James Socol',
    author_email='me@jamessocol.com',
    maintainer='Christopher Grebs',
    maintainer_email='cg@webshox.org',
    url='http://github.com/mozilla/django-csp',
    license='BSD',
    packages=find_packages(),
    project_urls={
        "Documentation": "http://django-csp.readthedocs.org/",
        "Changelog": "https://github.com/mozilla/django-csp/blob/main/CHANGES",
        "Bug Tracker": "https://github.com/mozilla/django-csp/issues",
        "Source Code": "https://github.com/mozilla/django-csp",
    },
    install_requires=install_requires,
    extras_require={
        'tests': test_requires,
        'jinja2': jinja2_requires,
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
        'Framework :: Django',
    ]
)
