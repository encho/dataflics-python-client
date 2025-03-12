# setup.py
from setuptools import setup, find_packages

setup(
    name="dataflics",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    description="A Python client library for creating videos via the dataflics.com platform.",
    author="Lorenzo Bertolini",
    author_email="lorenzo@dataflics.com",
    url="https://github.com/encho/dataflics-python-client"
)
