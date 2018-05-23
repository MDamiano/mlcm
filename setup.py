from setuptools import setup
import codecs
import os
import glob

name = 'mlcm'
description = 'Multi Label Confusion Matrix for one-hot-encoded y_test and y_pred'
url = 'https://github.com/MDamiano/mlcm'

os.chdir(os.path.abspath(os.path.dirname(__file__)))

subdirs_to_include = []
for x in os.walk(name):
	if os.path.isdir(x[0]):
		if x[0] != name:
			subdirs_to_include.append(x[0])

files_to_include = []
for x in glob.glob(os.path.join(name, '*')):
	if x[-2:] != 'py':
		files_to_include.append(os.path.join(name, os.path.split(x)[1]))

files_to_include.append('README.md')
files_to_include.append('LICENSE')

w = open('MANIFEST.in', 'w')
for i in subdirs_to_include:
	w.write('include ' + os.path.join(i, '*') + ' \n')

for i in files_to_include:
	w.write('include ' + i + ' \n')

w.close()

with codecs.open('README.md', encoding='utf-8') as f:
	long_description = f.read()

version = ' '
for i in open(os.path.join(name, '__init__.py')):
	if len(i.split('__version__')) > 1:
		version = i.split()[-1][1:-1]

setup(
	  name=name,
	  version=version,
	  description=description,
	  long_description=long_description,
	  url=url,
	  author='Mario Damiano',
	  author_email='mdamiano91@gmail.com',
	  license='MIT',
	  classifiers=['Intended Audience :: Anyone',
				   'Topic :: Scientific/Statistic :: Machine Learning',
				   'License :: OSI Approved :: MIT License',
				   'Operating System :: MacOS :: Unix'
				   'Programming Language :: Python :: 3.6',
				   ],
	  packages=[name],
	  include_package_data=True,
	  zip_safe=False,
	  )
