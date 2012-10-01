from setuptools import setup
import os
import sys


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


extra = {}
requirements = ['requests', 'docar', 'pymongo'],
tests_require = ['nose', 'coverage', 'Mock']

# In case we use python3
if sys.version_info >= (3, 0):
    extra.update(use_2to3=True)

setup(
    name="docar_backend_mongodb",
    version="0.1",
    packages=['docar_backend_mongodb'],
    include_package_data=True,
    install_requires=requirements,
    tests_require=tests_require,
    setup_requires='nose',
    test_suite="nose.collector",
    extras_require={'test': tests_require},

    author="Christo Buschek",
    author_email="crito@30loops.net",
    url="https://github.com/crito/docar-backend-mongodb",
    description="Map docar documents to a MongoDB database.",
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],
    **extra
)
