from setuptools import setup

import rfc2397

setup(name=rfc2397.name,
      packages=(rfc2397.name,),
      version=rfc2397.version,
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
