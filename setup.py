from setuptools import setup, find_packages
import subprocess
import sys

# Load the README file to use it as the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

import subprocess
import sys

setup(
    name="inspectio", 
    version="1.0",
    author="Ayman Abdul Kareem",
    description="A secure log review tool that detects sensitive data using regex and spaCy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/unpluggedsec/inspectio.git",  # GitHub or project URL
    packages=find_packages(where='src'), #(where='src')
    # package_dir={},
    include_package_data=True,  # This is key to including non-code files
    # py_modules=["inspectio"],             # Directly include the inspectio module
    package_dir={"": "src"},              # Packages and modules are in src/
    # include_package_data=True,            # Include non-Python files
    # package_data={
    #     '': ['patterns.yaml'],            # Include the YAML file in the package
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'spacy>=3.0.0',
        'PyYAML>=5.4.1',
        'argparse>=1.4.0',
    ],
    entry_points={
        'console_scripts': [
            'inspectio=inspectio.inspectio:main',
        ],
    },
)
