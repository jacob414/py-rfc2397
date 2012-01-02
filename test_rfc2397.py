"""
Test suite depends on py.test_.

For additional information see README.rst.

.. _py.test: http://pytest.org
"""
__docformat__ = 'reStructuredText en'

import os
import sys
import errno
import subprocess
import tempfile
import shutil

from cStringIO import StringIO

import py
import pytest

try:
    import virtualenv
except ImportError:
    virtualenv = None

import rfc2397

def test_succeed():
    ec, out = rfc2397.dataurl('dot.png')
    assert ec == 0
    assert out == 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVQImWP4o8oAAANCASIYayeeAAAAAElFTkSuQmCC'

def test_not_classifiable():
    err = StringIO()
    ec = rfc2397.cli(('rfc', 'xxx'), stderr=err)
    assert ec == errno.EINVAL
    assert err.getvalue().startswith('rfc2397: failed to determine file type')

def test_file_not_found():
    err = StringIO()
    ec = rfc2397.cli(('rfc', 'noexist.png'), stderr=err)
    assert ec == errno.ENOENT
    assert err.getvalue()[0:8] == 'rfc2397:'

def test_empty_args():
    err = StringIO()
    ec = rfc2397.cli(('rfc',), stderr=err)
    assert ec == errno.EINVAL
    assert err.getvalue().startswith('rfc2397: syntax rfc2397 <asset path>')
