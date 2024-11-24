from setuptools import setup,find_packages
from typing import List

HYPHEN_E_DOT='-e .'
'''
The function to return the list of requirements.
'''
def get_requirements(file_path:str)->List[str]:
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")  for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


    return requirements

setup(name="ML Projects")
