import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="utils",
    version="0.0.1",
    author="Rainer Weinberger",
    license="GNU General Public License v3 (GPLv3)",
    author_email="rainer.weinberger@cfa.harvard.edu",
    description="Useful routines for python",
    url="https://github.com/rainerweinberger/utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
        "Operating System :: OS Independent",
    ],
)
