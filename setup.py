'''
This setup.py file is an essential part of the Python packaging ecosystem. It is used to install the package and its dependencies.
To define configuration options for the package, we use the setup() function from the setuptools module.
'''

from setuptools import find_packages, setup #look
from typing import List
def get_requirements()->List[str]:
    requirement_lst: List[str]= []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
                    
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author= 'Emre dost',
    author_email= 'emredost1987@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    
)