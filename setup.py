from setuptools import setup, find_packages

setup(
        name="diff_csvj
    version="0.0.1",
    description="Bjoernski's CSV file comparer"
    author="Bjoern Winkler",
    author_email="bjoern@bjoern-winkler.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.11",
    ],
    packages=find_packages(exclude=["test"]),
    install_requires=[""],
    python_requires=">=3",
)
