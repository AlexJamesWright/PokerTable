from setuptools import setup

setup(name='PokerTable',
      version='0.1',
      description='Poker simulator',
      url='https://github.com/AlexJamesWright/PokerTable',
      author='Alex James Wright',
      author_email='alex.j.wright2@gmail.com',
      packages=['pokertable'],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])