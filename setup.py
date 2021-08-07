from setuptools import setup, find_packages

setup(name='PokerTable',
      version='0.1',
      description='Poker simulator',
      url='https://github.com/AlexJamesWright/PokerTable',
      author='Alex James Wright',
      author_email='alex.j.wright2@gmail.com',
      packages=find_packages(),
      package_dir = {"" : "./"},
      include_package_data=True)