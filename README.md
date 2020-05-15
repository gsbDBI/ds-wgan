### Guide to Simulating Economic Datasets using WGANs

This repository contains `wgan`, a python package built on PyTorch for using WGANs to simulate from joint and conditional distributions of economic datasets. Brief documentation and the API for the module is available [here](https://ds-wgan.readthedocs.io/en/latest/).

This [Google Colab Notebook](https://colab.research.google.com/drive/1V3TOkPcU8pfPdoxH_UTSPUcNAfAtH9rW#scrollTo=rQtGe_MH746N) contains a tutorial for the code, including how to install the package and estimate and simulate from the resulting models, using a free Google GPU. The tutorial simulates from the Lalonde-Dehejia-Wahba dataset, as described in detail in the following paper.

Athey, Susan, Guido Imbens, Jonas Metzger, and Evan Munro.
"Using Wasserstein Generative Adversial Networks for the Design of Monte Carlo Simulations."
[arXiv:1909.02210](https://arxiv.org/abs/1909.02210). September 2019.

The data folder contains the raw Lalonde-Dehejia-Wahba data.

#### Installation Instructions

For running the WGAN code outside of a Google Colab environment an installation of [python3](https://www.python.org/downloads/) is required.

In order to install the package and dependencies from Github, use pip:
```
pip install git+https://github.com/gsbDBI/ds-wgan.git#egg=wgan/
```
