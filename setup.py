#!/usr/bin/env python
import io
import os
import sys
if sys.version_info < (3,3):
    from imp import load_source
elif sys.version_info < (3,6):
    from importlib.machinery import SourceFileLoader
    def load_source(name, pathname):
        return SourceFileLoader(name, pathname).load_module()
else:
    # From https://docs.python.org/dev/whatsnew/3.12.html#imp
    import importlib.util
    import importlib.machinery

    def load_source(modname, filename):
        loader = importlib.machinery.SourceFileLoader(modname, filename)
        spec = importlib.util.spec_from_file_location(modname, filename, loader=loader)
        module = importlib.util.module_from_spec(spec)
        # The module is always executed and not cached in sys.modules.
        # Uncomment the following line to cache the module.
        # sys.modules[module.__name__] = module
        loader.exec_module(module)
        return module

try:
    from setuptools import find_packages, setup
except ImportError:
    raise ImportError(
        "'setuptools' is required but not installed. To install it, "
        "follow the instructions at "
        "https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py"
    )


def read(*filenames, **kwargs):
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", "\n")
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


root = os.path.dirname(os.path.realpath(__file__))
version_module = load_source(
    "version", os.path.join(root, "nengo_gui", "version.py")
)

setup(
    name="nengo-gui",
    version=version_module.version,
    author="Applied Brain Research",
    author_email="info@appliedbrainresearch.com",
    packages=find_packages(),
    scripts=[],
    include_package_data=True,
    url="https://github.com/nengo/nengo-gui",
    license="GNU General Public License, version 2",
    description="Web-based GUI for building and visualizing Nengo models.",
    long_description=read("README.rst", "CHANGES.rst"),
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "nengo_gui = nengo_gui:old_main",
            "nengo = nengo_gui:main",
        ]
    },
    install_requires=[
        "nengo>=2.6.0",
    ],
    tests_require=[
        "pytest",
        "selenium",
    ],
    classifiers=[  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
