from setuptools import find_packages
from setuptools import setup

install_requires = [
    "requests", "pytest", "coverage"
]

setup(
    name="pyTogglTimes",
    version="1.0.0",
    url="None",
    license="None",
    maintainer="CDF",
    maintainer_email="n/a",
    description="Callum's Toggl Insert Script...",
    long_description="Callum's Toggl Insert Script...",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
)
