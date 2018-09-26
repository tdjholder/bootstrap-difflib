import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bootstrap-difflib",
    version="0.0.1",
    author="Thomas Holder",
    author_email="tdjholder@gmail.com",
    description="Making the output of DiffLib Bootstrap compatible",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tdjholder/bootstrap-difflib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
