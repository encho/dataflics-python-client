# dataflics-python-client

A Python client library for creating videos on the Dataflics video platform. This package provides a simple API to interact with the Dataflics REST API, allowing you to create and manage videos with ease.

## Features

- **Simple API:** Create new video objects with a single function call.
- **Intuitive Design:** Use methods like `save()` on video objects to send data to the API.
- **Configurable:** Easily set up your API endpoint and authentication.

## Installation

### From PyPI

Once published, you can install the package via pip:

```bash
pip install dataflics
```

## Development

```bash
source venv/bin/activate
```

When you’re done working, you can deactivate the virtual environment by simply running:

```bash
deactivate
```

To install a package:

```bash
pip install requests
```

Freezing dependencies:

```bash
pip freeze > requirements.txt
```

Later, someone else (or you on another machine) can install the exact versions of dependencies using:

```bash
pip install -r requirements.txt
```

You can also install your package in editable mode if you're developing it:

```bash
pip install -e .
```
