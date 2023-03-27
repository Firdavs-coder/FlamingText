from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Unofficial API of flamingtext.com'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

setup(
    name="FlamingText",
    version=VERSION,
    author="Firdavs Shodiyev",
    author_email="firdavscoder1@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
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
