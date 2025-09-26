from setuptools import setup, find_packages
from typing import List
E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    with open(file_path,'r') as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if E_DOT in requirements:
            requirements.remove(E_DOT)
    return requirements



setup(
name='ml_project',
version='0.0.1',
author='Tejasvi',
author_email='tejasvihegde303@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)