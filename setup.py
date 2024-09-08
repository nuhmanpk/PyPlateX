import pathlib
from setuptools import setup, find_packages

file = pathlib.Path(__file__).parent

README = (file / "README.md").read_text()

requirements = (file / "requirements.txt").read_text().splitlines()

setup(
    name="pyplatex",
    version="0.0.6",
    author="Nuhman Pk",
    author_email="nuhmanpk7@gmail.com",
    long_description = README,
    long_description_content_type = "text/markdown",
    description="A high-performance, scalable, and ready-to-use Automatic Number Plate Recognition (ANPR) package.",
    license="MIT",
    url="https://github.com/nuhmanpk/pyplatex",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
        package_data={
        'pyplatex.models': ['plate-detection-models/*.pt'],  # Include all .pt files 
    },
    install_requires=requirements,
    python_requires=">=3.9",
    project_urls={
        'Documentation': 'https://github.com/nuhmanpk/pyplatex/blob/main/README.md',
        'Funding': 'https://github.com/sponsors/nuhmanpk',
        'Source': 'https://github.com/nuhmanpk/pyplatex/',
        'Tracker': 'https://github.com/nuhmanpk/pyplatex/issues',
    },
    
)
