# Welcome to iTile

iTile is a sub-module developed as a component of a generic
[scaffolding](https://github.com/web2py/py4web/tree/master/apps/_scaffold)
[py4web](http://py4web.com/) application and it's part of the
[Planet Suite](https://manuelep.github.io/planet-suite/).

> **Note**
> Please refer to the
> [py4web official documentation](http://py4web.com/_documentation/static/index.html#chapter-01)
> for framework installation, setup and basics concepts about implementing applications
> and about what the *apps* folder is.

# Description

This module implements helpers base on the [Mapnik](https://mapnik.org/) python
implementation for easy raster tile layer API services implementation.

# How to's

## Include iTile in your custom application

Py4web applications are nothing more than native [python modules](https://docs.python.org/3/tutorial/modules.html)
and the iTile code is structured in the same way so can be used actually as
a *submodule* that can be nested in custom applications.

You can link the module to your code repository using [Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
but the minimal requirement is to copy/clone the [iTile repository](https://github.com/manuelep/itile)
nested in your `root` project folder.

### Requirements

#### system requirements

Please refer to the official [Mapnik documentation](https://mapnik.org/pages/downloads.html)
for compilation and installation.

An easy alternative under Debian/Ubuntu GNU/Linux systems is to use the package:

* python3.6-mapnik (it implies nothing more than python3.6)

#### Python dependencies

Please refer to the `requirements.txt` file for an updated list of required python
modules and install them using:

```sh
pip install -r [path/to/apps/<your app>/itile/]requirements.txt
```

# Doc

Please refer to the [repository wiki](https://github.com/manuelep/itile/wiki)
for the module detailed documentation.
