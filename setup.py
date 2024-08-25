VERSION = '0.1.1'
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = """
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

# -- Define Dependencies --------------------------------------------------
import atexit
import glob
import os
import shutil
import matplotlib
from setuptools import setup
from setuptools.command.install import install
from setuptools import find_packages
# -------------------------------------------------------------------------


def install_styles():

    # Find all style files
    stylefiles = glob.glob('mplstyles/*.mplstyle', recursive=True)

    # Find stylelib directory (where the *.mplstyle files go)
    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)

    # Copy files over
    print("Installing styles into", mpl_stylelib_dir)
    for stylefile in stylefiles:
        print(os.path.basename(stylefile))
        shutil.copy(
            stylefile,
            os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))


class PostInstallMoveFile(install):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)


# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="ChalcedonPy",
    version=VERSION,
    author="DTMc",
    author_email="dtm@mci4me.at",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "matplotlib >= 3.9", "scikit-learn", "pandas >= 2.2.2",
        "opencv-python >= 4.10.0.84", "pillow >= 10.4.0"
    ],
    cmdclass={'install': PostInstallMoveFile},
    keywords=['python', 'mci', 'lecture'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ])
