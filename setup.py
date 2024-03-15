from setuptools import find_packages,setup

print("Successfully imported find_packages() from setuptools")

Hypen_e_dot = '-e .'

def get_requirments(file_path:str)->list[str]:
  '''
  this function will return list of requirment
  '''
  requirements = []
  with open(file_path) as file_obj:
    requirements = file_obj.readlines()
    requirements = [req.replace("\n","") for req in requirements]

    if Hypen_e_dot in requirements:
      requirements.remove(Hypen_e_dot)

setup(
  name='mlproject',
  version='0.0.1',
  author='Fayis',
  author_email='muhammedfayisktd@gmail.com',
  packages=find_packages(),
  install_requires=get_requirments('requirements.txt') #['pandas','numpy','seaborn']
)
