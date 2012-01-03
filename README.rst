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
that `pip` installs to. Just give `rfc2397` a path to an image
file. For the moment it recognizes `.jpg`, `.gif` and `.png`::

    $ rfc2397 dot.png # <- your image path
    data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVQImWP4o8oAAANCASIYayeeAAAAAElFTkSuQmCC

That's basically all there is to know about it.

.. _pip: http://www.pip-installer.org/
.. _PyPI: http://pypi.python.org/pypi
