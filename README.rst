==========
py-rfc2397
==========

:Author: Jacob Oscarson
:Contact email: jacob@plexical.com

Quick implementation of RFC2397_ in Python, `MIT Licenced`_. RFC2397
is also known as the 'data url' format used to embed image data
directly into CSS stylesheets among other things.

The rationale behind this package is described in `this blogpost`_.

.. _RFC2397: http://tools.ietf.org/html/rfc2397
.. _`MIT Licenced`: http://www.opensource.org/licenses/mit-license.php
.. _dataurl: http://pypi.python.org/pypi/dataurl
.. _`this blogpost`: http://bit.ly/kwUnQL

Requirements
------------

Python 2.6 and 2.7, not tested on Python 3+ (yet).

Installation
------------

The latest version can be found on PyPI_. The recommended way to
install is via `pip`_::

    $ pip install rfc2397

An executable named `rfc2397` is then placed in the python environment
that `pip` installs to.

As an alternate method, it's also possible to copy the `rfc2397.py`_
file to any location and run the script stand-alone.

.. _`rfc2397.py`: https://github.com/JacobOscarson/py-rfc2397/blob/master/rfc2397.py

Usage
-----

Just give `rfc2397` a path to an image file. `rfc2397` uses Python's
mimetypes_ module to determine what MIME-type a file has (**N.B**:
the program won't stop you from encoding something too large/an
unsupported mime-type).

    $ rfc2397 dot.png # <- your image path
    data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVQImWP4o8oAAANCASIYayeeAAAAAElFTkSuQmCC

.. _pip: http://www.pip-installer.org/
.. _PyPI: http://pypi.python.org/pypi

Changes
-------

1.0b2 (2012-01-03)
++++++++++++++++++

* Uses mimetypes_ module instead of primitive ad-hoc file name
  extension guessing.
* `rfc2397` is now a single-file module, simplifies package and makes
  it possible to just copy the `rfc2397.py`_ file to an arbitrary
  location as an alternate installation method.
* Better QA by using tox_.

.. _mimetypes: http://docs.python.org/library/mimetypes.html
.. _`rfc2397.py`: https://github.com/JacobOscarson/py-rfc2397/blob/master/rfc2397.py
.. _tox: http://tox.testrun.org/

1.0b1 (2011-06-16)
++++++++++++++++++

Concept and initial coding.
