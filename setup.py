"""
Flask-HTTPClient
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-Client',
    version='1.0',
    url='https://blog.haojunyu.com/projects/flask-httpclient',
    license='BSD',
    author='haojunyu',
    author_email='haojunyu@datagrand.com',
    description='HTTP Client extension for Flask',
    long_description=__doc__,
    py_modules=['flask_httpclient'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
