# setup.py
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="dataflics",
    version="0.2.0",
    packages=find_packages(),
    install_requires=["requests"],
    description="A Python client library for creating videos via the dataflics.com platform.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lorenzo Bertolini",
    author_email="lorenzo@dataflics.com",
    url="https://github.com/encho/dataflics-python-client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={
        "dataflics": ["py.typed"],
    },
)
