import setuptools
from setuptools import find_packages
import re

with open("./siml-parser/__init__.py", 'r') as f:
    content = f.read()
    version = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content).group(1)
    
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="siml-parser",
    version=version,
    author="capjamesg",
    author_email="jamesg@jamesg.blog",
    description="Structured Index Markup Language (SIML) parser.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/capjamesg/siml",
    install_requires=[
        "lark",
    ],
    packages=find_packages(exclude=("tests",)),
    extras_require={
        "dev": ["flake8", "black==22.3.0", "isort", "twine", "pytest", "wheel", "tox", "responses"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
