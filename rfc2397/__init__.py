import os

name = 'rfc2397'
version = '1.0b1'

sdist = lambda: os.path.abspath((os.path.join(
            os.path.dirname(__file__),
            '..',
            'dist',
            '%s-%s.tar.gz' % (name, version))))
