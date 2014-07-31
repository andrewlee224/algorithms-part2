from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension("floydwarshall", sources=["floydwarshall.pyx"])
]

setup(
        name="floydwarshall",
        include_dirs=[np.get_include()],
        ext_modules = cythonize(extensions)
)
