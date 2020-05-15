from os.path import abspath, dirname, join

from setuptools import setup, find_packages

here = abspath(dirname(__file__))

with open(join(here, 'README.md')) as f:
    readme = f.read()

# Uncomment once LICENSE is added
# with open(join(here, 'LICENSE')) as f:
#     lic = f.read()

setup(name='wgan',
      version='0.2',
      description='wgan',
      author='Jonas Metzger and Evan Munro',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/gsbDBI/ds-wgan',
      py_modules=['wgan'],
      install_requires=[
          "numpy",
          "torch>=1.1.0",
          "pandas",
          "matplotlib",
          "scipy"
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          # Uncomment once license it added
          # 'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
      # license=lic,
      # Uncomment when license is approved
      )
