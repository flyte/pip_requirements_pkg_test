import os.path
import inspect

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

def required(fname):
    this_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    lines = open(os.path.join(this_dir, fname)).read().strip().split("\n")
    return [l for l in lines if not l.startswith("--")]

setup(
    name = "piptest",
    version = "0.0.1",
    packages = find_packages(),
    install_requires = required("requirements.txt")
)

