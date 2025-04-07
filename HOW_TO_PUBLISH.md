## 1. Update Your Package

Before publishing, make sure to update the version number in your `setup.py`. For example, if you are updating from version `0.1.0`, change it to `0.1.1`:

```python
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="dataflics",
    version="0.2.1",  # Update the version for a new release
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
```

## 2. Build the Distribution Packages

Make sure you are in the root directory of your repository (where `setup.py` is located) and run:

```bash
python setup.py sdist bdist_wheel
```

## 3. Upload to TestPyPI

Before releasing to production, you should test your package on TestPyPI. Ensure you have a properly configured `.pypirc` file. An example `.pypirc` for TestPyPI might look like:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-<your-production-token>

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-<your-test-token>
```

```bash
twine upload --config-file ./.pypirc --repository testpypi dist/*
```

## 4. Test the Installation from TestPyPI

Create or activate a new virtual environment and install your package from TestPyPI:

```bash
pip install --upgrade --index-url https://test.pypi.org/simple/ dataflics
```

OR, force reinstall:

```bash
pip install --force-reinstall --index-url https://test.pypi.org/simple/ dataflics
```

## 5. Upload to Production PyPI

Once you are satisfied with the TestPyPI version, update your `.pypirc` to include your production credentials and upload to PyPI with:

```bash
twine upload --config-file ./.pypirc --repository pypi dist/*
```

## 6. Verify the Release

After publishing, users can install your package via:

```bash
pip install dataflics
```

## Additional Notes

- **Versioning:**  
  Always update the version number in `setup.py` when making changes. PyPI does not allow overwriting a version that's already been published.

- **Type Annotations:**  
  To ensure type checkers (like Pylance) recognize that your package is typed, include a `py.typed` file in your `dataflics` directory and ensure it is included in your package distribution by setting `include_package_data=True` and specifying it in `package_data`.

- **Testing Environment:**  
  It is a good idea to test your changes in a new virtual environment to ensure that there are no caching or dependency issues.
