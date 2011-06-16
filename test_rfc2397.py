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
from rfc2397.main import dataurl, cli

def test_succeed():
    ec, out = dataurl('dot.png')
    assert ec == 0
    assert out == 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVQImWP4o8oAAANCASIYayeeAAAAAElFTkSuQmCC'

def test_not_classifiable():
    err = StringIO()
    ec = cli(('rfc', 'xxx'), stderr=err)
    assert ec == errno.EINVAL
    assert err.getvalue().startswith('rfc2397: failed to determine file type')

def test_file_not_found():
    err = StringIO()
    ec = cli(('rfc', 'noexist.png'), stderr=err)
    assert ec == errno.ENOENT
    assert err.getvalue()[0:8] == 'rfc2397:'

def test_empty_args():
    err = StringIO()
    ec = cli(('rfc',), stderr=err)
    assert ec == errno.EINVAL
    assert err.getvalue().startswith('rfc2397: syntax rfc2397 <asset path>')

@pytest.mark.skipif("virtualenv is None")
class TestPackagingIntegration(object):

    def setup_class(cls):
        cls.env = tempfile.mkdtemp()
        virtualenv.create_environment(cls.env)

    def teardown_class(cls):
        shutil.rmtree(cls.env)

    def env_path(self, *relpath):
        return os.path.join(self.env, *relpath)

    def test_sdist(self):
        rc = subprocess.call(('python', 'setup.py', 'sdist'))
        assert rc == 0

    def test_installation(self):
        rc = subprocess.call( (self.env_path('bin', 'pip'),
                               'install',
                               rfc2397.sdist()) )
        assert rc == 0
        proc = subprocess.Popen(self.env_path('bin', 'rfc2397'),
                                stderr=subprocess.PIPE)
        out, err = proc.communicate()
        rc = proc.wait()
        assert rc == errno.EINVAL
        assert err.startswith('rfc2397: syntax rfc2397 <asset path>')
