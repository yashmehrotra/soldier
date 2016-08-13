Soldier: Subprocess with Style
==============================
.. image:: https://travis-ci.org/yashmehrotra/soldier.svg?branch=master
    :target: https://travis-ci.org/yashmehrotra/soldier

.. image:: https://img.shields.io/badge/license-APACHE2-blue.svg?style=flat-square
    :target: https://github.com/yashmehrotra/soldier/blob/master/LICENSE

.. image:: https://readthedocs.org/projects/soldier/badge/?version=latest
    :target: http://soldier.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

|
.. image:: https://raw.githubusercontent.com/yashmehrotra/soldier/master/images/flint.jpg

Soldier is an Apache2 licensed library designed for executing and managing system processes with ease.

It is written on top of subprocess and has a much user-friendly and pythonic interface.

And the best part - it is very easy to get started

Installation 
------------
.. code-block:: sh

    $ pip install soldier

Getting Started
---------------
.. code-block:: python

    >>> import soldier

    >>> print soldier.run('pwd').output
    /home/python/
    
    >>> firefox_process = soldier.run('firefox', background=True)
    >>> firefox_process.pid
    20749

    >>> job = soldier.run('myjob', timeout=30)

Documenation
------------

The documentation is available at `soldier.readthedocs.io <http://soldier.readthedocs.io/>`_
