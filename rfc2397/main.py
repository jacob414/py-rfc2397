"""
=============================
py-rfc2397, by Jacob Oscarson
=============================

See README.rst.

`MIT Licenced`_

.. _`MIT Licenced`: http://www.opensource.org/licenses/mit-license.php
"""
__docformat__ = 'reStructuredText en'

import os
import sys
import errno
import base64

ext_map = {
    'png': 'image/png',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'gif': 'image/gif',
    # Add more if desired
    }

def dataurl(path):
    ext = path.split('.')[-1]
    try:
        mime = ext_map[ext]
    except KeyError:
        return errno.EINVAL, 'rfc2397: failed to determine file type'

    try:
        with open(path, 'r') as fp:
            return 0, 'data:%s;base64,%s' % (mime, base64.b64encode(fp.read()))
    except IOError, e:
        return e.errno, 'rfc2397: %s' % e.strerror

def cli(args=sys.argv, stdout=sys.stdout, stderr=sys.stderr):
    if len(args) > 1:
        rc, out = dataurl(args[1])
        if rc == 0:
            stdout.write(out + os.linesep)
        else:
            stderr.write(out + os.linesep)
        return rc
    stderr.write('rfc2397: syntax rfc2397 <asset path>' + os.linesep)
    return errno.EINVAL

if __name__ == '__main__':
    sys.exit(cli())
