# Soldier: Subprocess with Style

[![image](https://img.shields.io/travis/yashmehrotra/soldier.svg?style=flat-square)](https://travis-ci.org/yashmehrotra/soldier) [![image](https://img.shields.io/badge/license-APACHE2-blue.svg?style=flat-square)](https://github.com/yashmehrotra/soldier/blob/master/LICENSE) [![Documentation](https://readthedocs.org/projects/soldier/badge/?version=latest)](http://soldier.readthedocs.org/en/latest/?badge=latest)

![image](https://raw.githubusercontent.com/yashmehrotra/soldier/master/images/flint.jpg)

Soldier is an Apache2 licensed library designed for executing and
managing system processes with ease.

It is written on top of subprocess and has a much user-friendly and
pythonic interface.

And the best part - it is very easy to get started

## Installation

``` sh
$ pip install soldier
```

## Getting Started

``` python
>>> import soldier

>>> print soldier.run('pwd').output
/home/python/

>>> firefox_process = soldier.run('firefox', background=True)
>>> firefox_process.pid
20749

>>> job = soldier.run('myjob', timeout=30)
```

## Documentation

The documentation is available at [soldier.readthedocs.io](http://soldier.readthedocs.io/)
