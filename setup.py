"""
Setup script for testthis package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="testthis",
    version="0.1.0",
    author="testthis project",
    author_email="contact@example.com",
    description="A Python project for testing and experimentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ikemike01/testthis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.12",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.910",
        ],
    },
    entry_points={
        "console_scripts": [
            "testthis=trift.python:main",
        ],
    },
)