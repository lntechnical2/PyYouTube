import pathlib
import setuptools

file = pathlib.Path(__file__).parent

README = (file / "README.md").read_text()

setuptools.setup(
    name="PyYouTube",
    version="1.0.6",
    author="mrlokaman",
    author_email="ln0technical@gmail.com",
    long_description = README,
    long_description_content_type = "text/markdown",
    description="Python library Get YouTube Video Data",
    license="MIT",
    url="https://github.com/lntechnical2/PyYouTube",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires = ["youtube_dl"],
    python_requires=">=3.6"
)
