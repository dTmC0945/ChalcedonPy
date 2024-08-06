from setuptools import setup, find_packages

VERSION = '0.0.6' 
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION ="""
This Package is designed for to be used in lectures to teach concepts and simplify certain operations. \n
\n
Currently ChalcedonPy support the following lectures: \n
\n
1 - Electrodynamics \n
2 - Digital Image Processing \n
3 - Higher Mathematics \n
4 - Data Science \n
5 - Machine Learning \n
"""

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="ChalcedonPy", 
        version=VERSION,
        author="DTMc",
        author_email="test@dm.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
