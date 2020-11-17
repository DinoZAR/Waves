# Setup

* Install `pyenv`
* Install Python 3.7.8 using pyenv. Make sure that shared libraries are enabled:
```
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.7.8
```
* Install `poetry`
* Make a virtual environment using the Python from pyenv
* Run `poetry install`

# Create a package

* Export all of the variables in the .env file. Make sure that LD_LIBRARY_PATH points to the correct place.
* Run `make package`
