import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whereby-api",
    version="0.1.1",
    author="Philipp Bosch",
    author_email="hello@pb.io",
    description="Client for the Whereby API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/philippbosch/python-whereby-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests==2.24.0",
        "python-dateutil==2.8.1",
    ],
)
