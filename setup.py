from distutils.core import setup

setup(
    name='soldier',
    version='0.0.1.4',
    author='Yash Mehrotra',
    author_email='yashmehrotra95@gmail.com',
    packages=['soldier'],
    scripts=[],
    url='https://pypi.python.org/pypi/soldier',
    license='Apache 2.0',
    description='Subprocess with all guns blazing',
    long_description=open('README.txt').read(),
    install_requires=['psutil==3.2.1'],
)
