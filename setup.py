import pathlib
from setuptools import setup, find_packages

file = pathlib.Path(__file__).parent

README = (file / "README.md").read_text()

requirements = (file / "requirements.txt").read_text().splitlines()

setup(
    name="pyplatex",
    version="0.0.1",
    author="Nuhman Pk",
    author_email="nuhmanpk7@gmail.com",
    long_description = README,
    long_description_content_type = "text/markdown",
    description="A scalable and versatile ANPR package leveraging YOLO for detection and multiple OCR options to accurately recognize license plates.",
    license="MIT",
    url="https://github.com/nuhmanpk/pyplatex",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    packages=find_packages(),
    python_requires=">=3.9",
    project_urls={
        'Documentation': 'https://github.com/nuhmanpk/pyplatex/blob/main/README.md',
        'Funding': 'https://github.com/sponsors/nuhmanpk',
        'Source': 'https://github.com/nuhmanpk/pyplatex/',
        'Tracker': 'https://github.com/nuhmanpk/pyplatex/issues',
    },
    
)
