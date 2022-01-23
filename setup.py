"""Setup for pip package."""
import os
from setuptools import setup, find_packages

version = '1.0.0'
cwd = os.path.dirname(os.path.abspath(__file__))
version_path = os.path.join(cwd, 'textContribution', 'version.py')
with open(version_path, 'w') as version_file:
	version_file.write("__version__ = '{}'\n".format(version))
with open('./requirements.txt') as f:
	setupRequires = f.read().splitlines()

setup(
	name="textContribution",
	version=version,
	author="Xudongyu",
	description="a package for BI-Selection",
	install_requires=setupRequires,
	packages=find_packages(),
	python_requires='>=3'
)
