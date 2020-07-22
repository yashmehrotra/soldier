try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='soldier',
    version='0.2.3',
    author='Yash Mehrotra',
    author_email='yashmehrotra95@gmail.com',
    packages=['soldier'],
    url='https://pypi.python.org/pypi/soldier',
    license='Apache 2.0',
    description='Subprocess with Style',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
)
