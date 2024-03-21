from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.8'
DESCRIPTION = 'Unofficial API of flamingtext.com'
long_description = 'FlamingText is free online logo generator that anyone can use to create a great logo in minutes! Just select one of our logo designs, and get started now!'

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name="FlamingText",
    version=VERSION,
    author="Firdavs Shodiyev",
    author_email="firdavscoder1@gmail.com",
    long_description_content_type="text/markdown",
    url="https://github.com/Firdavs-coder/FlamingText",
    description=DESCRIPTION,
    long_description=long_description,
    packages=find_packages(),
    install_requires=["requests"],
    keywords=['python', 'effects', 'text', 'flamingtext'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
