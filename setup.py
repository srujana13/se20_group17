from setuptools import setup, find_packages
  
setup(
    name='se_grp17',
    version='0.1',
    description='Homework 1 Python Tests',
    author='NCSU CS grp 17',
    author_email='smavinh@ncsu.edu',
    packages=find_packages(),
    tests_require=['pytest'],
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Data structures",
      ],

      license='MIT',
      install_requires=[
        'pytest',
      ]
      )
