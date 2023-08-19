from setuptools import setup, find_packages

setup(
    name="package_name",
    version="0.0.1",
    description="Bjoernski's Package Template [replace]",
    author="Bjoern Winkler",
    author_email="bjoern@bjoern-winkler.de",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(exclude=["test"]),
    install_requires=[""],
    python_requires=">=3",
)
