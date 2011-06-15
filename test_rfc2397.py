"""
Test suite depends on py.test_.

For additional information see README.rst.

.. _py.test: http://pytest.org
"""
__docformat__ = 'reStructuredText en'

import sys
import errno
import subprocess
import tempfile

import py
import pytest

from rfc2397.main import dataurl, cli

def test_succeed():
    ec, data = dataurl('dot.png')
    assert ec == 0
    assert data == 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVQImWP4o8oAAANCASIYayeeAAAAAElFTkSuQmCC'

def test_not_classifiable():
    ec, data = cli(('rfc', 'xxx'))
    assert ec == errno.EINVAL
    assert data == 'rfc2397: failed to determine file type'

def test_file_not_found():
    ec, data = cli(('rfc', 'noexist.png'))
    assert ec == errno.ENOENT
    assert data[0:8] == 'rfc2397:'

def test_empty_args():
    ec, data = cli(('rfc',))
    assert ec == errno.EINVAL
    assert data == 'rfc2397: syntax rfc2397 <asset path>'

def no_venv():
    try:
        return subprocess.call(('virtualenv', '--version')) != 0
    except:
        return True

@pytest.mark.skipif("no_venv()")
class TestPackagingIntegration(object):

    def setup_class(cls):
        cls.tmpdir = tempfile.mkdtemp()

    def teardown_class(cls):
        pass # XXX <---

    def test_sdist(self):
        rc = subprocess.call(('python', 'setup.py', 'sdist'))
        assert rc == 0

    def test_installation(self):
        # XXX run `virtualenv `tmpdir``, run `pin install `.tgz from above`
        pass
