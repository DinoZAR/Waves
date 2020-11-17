# Setup

* Install `pyenv`
* Install Python 3.7.8 using pyenv. Make sure that shared libraries are enabled:
```
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.7.8
```
* Install `poetry`
* Make a virtual environment using the Python from pyenv
* Run `poetry install`