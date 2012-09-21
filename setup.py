from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


extra = {}
requirements = ['distribute', 'docutils', 'requests', 'docar', 'pymongo'],
tests_require = ['nose', 'coverage', 'Mock']

setup(
    name="docar_backend_mongo",
    version="0.1",
    packages=['docar_backend_mongo'],
    include_package_data=True,
    #zip_safe=False,  # Don't create egg files, Django cannot find templates
                     # in egg files.
    install_requires=requirements,
    tests_require=tests_require,
    setup_requires='nose',
    test_suite="nose.collector",
    extras_require={'test': tests_require},

    author="Christo Buschek",
    author_email="crito@30loops.net",
    url="https://github.com/30loops/docar-backend-mongo",
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
