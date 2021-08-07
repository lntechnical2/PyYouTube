import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pyYoutube",
    version="0.0.1",
    author="mrlokaman",
    author_email="ln0technical@gmail.com",
    description="Python library Get YouTube Video Data",
    license="MIT",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    
)
