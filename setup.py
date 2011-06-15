from setuptools import setup

setup(name='rfc2397',
      packages=('rfc2397',),
      version='1.0b1',
      author='Jacob Oscarson',
      author_email='jacob@plexical.com',
      description='A Python RFC2397 implementation',
      long_description=open('README.rst').read(),
      entry_points = { 'console_scripts': ('rfc2397 = rfc2397.main:cli') },
      classifiers = [
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Environment :: Console',
          'Topic :: Internet :: WWW/HTTP :: Site Management',
          'Topic :: Multimedia :: Graphics :: Graphics Conversion'
          ],
      license='MIT')
