import os
import sys
from pip.req import parse_requirements

# http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

README = open(os.path.join(here, 'README.txt')).read()

# here we are pretend to be smart python guys

class Options(object):
    def __getattr__(self, name):
        return None
reqs = [str(ir.req) for ir in parse_requirements('requirements.txt', options=Options())]  # options is necessary for this function when there vcs links in requirements file, because of implementation bug


setup(name='yarnee.pyramid',
      version='0.1',
      description='yarnee.pyramid',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=reqs,
      tests_require=reqs,
      test_suite="yarnee.pyramid",
      entry_points="""\
      [paste.app_factory]
      main = yarnee.pyramid:main
      [console_scripts]
      initialize_yarnee.pyramid_db = yarnee.pyramid.scripts.initializedb:main
      """,
      )
