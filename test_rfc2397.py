"""
Test suite should be able to run with py.test_ or nose_.

For additional information see README.rst.

.. _py.test: http://pytest.org
.. _nose: http://somethingaboutorange.com/mrl/projects/nose
"""
__docformat__ = 'reStructuredText en'

import sys
import errno
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
    ec, data = dataurl('noexist.png')
    assert ec == errno.ENOENT
    assert data[0:8] == 'rfc2397:'

def test_empty_args():
    ec, data = cli(('rfc',))
    assert ec == errno.EINVAL
    assert data == 'rfc2397: syntax rfc2397 <asset path>'
