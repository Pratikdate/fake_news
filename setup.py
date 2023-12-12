from setuptools import setup,find_packages
from typing import List


def get_requires():
    "this function returns a list of requirements"
    with open("requirement.txt", "r") as f:
        requirements=f.readlines()
        requirements=[requirements.replace("\n", " ") for requirements in requirements]
        if "-e ."==requirements:
            requirements.remove("-e .")
    return requirements


setup(

    name="fake-news",
    version='0.0.1',
    author_email="pdate73@gmail.com",
    packages=find_packages(),
    install_require=get_requires(),
)