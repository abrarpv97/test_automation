# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in test_automation/__init__.py
from test_automation import __version__ as version

setup(
	name='test_automation',
	version=version,
	description='payroll process automation using sceduler',
	author='frappe',
	author_email='test@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
