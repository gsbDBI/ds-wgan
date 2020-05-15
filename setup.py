from os.path import abspath, dirname, join

from setuptools import setup, find_packages

here = abspath(dirname(__file__))

with open(join(here, 'README.md')) as f:
    readme = f.read()

with open(join(here, 'LICENSE')) as f:
    lic = f.read()

setup(name='wgan',
      version='0.2',
      description='wgan',
      author='Jonas Metzger and Evan Munro',
      author_email='munro@stanford.edu',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/gsbDBI/ds-wgan',
      packages=find_packages(),
      install_requires=[
          "numpy",
          "torch>=1.1.0",
          "pandas",
          "matplotlib"
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
        license=lic,
      )
