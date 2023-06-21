from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in club_customization/__init__.py
from club_customization import __version__ as version

setup(
	name="club_customization",
	version=version,
	description="the club customization",
	author="Ahmed",
	author_email="ahmed751995@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
