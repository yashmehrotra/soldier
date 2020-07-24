try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = None
with open('soldier/__init__.py', 'r') as f:
    for line in f.readlines():
        if '__version__' in line:
            version = line.split('=')[1].replace('\'', '').strip()

if not version:
    raise Exception("Error fetching version from soldier/__init__.py")

setup(
    name='soldier',
    version='0.2.4',
    author='Yash Mehrotra',
    author_email='yashmehrotra95@gmail.com',
    packages=['soldier'],
    url='https://pypi.python.org/pypi/soldier',
    license='Apache 2.0',
    description='Subprocess with Style',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
)
