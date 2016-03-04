# coding=utf-8
from setuptools import setup

setup(
    name="mailroom",
    description="Python 401 Mail Room Madness",
    version=0.1,
    author=["Joe McClenahan", "Nadia Bahrami"],
    author_email=["jmcclena94@gmail.com", "nadia.bahrami@gmail.com"],
    license="MIT",
    py_modules=["mailroom"],
    package_dir={"": "src"},
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-xdist", "tox"]},
)
