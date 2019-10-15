### Guide to Simulating Economic Datasets using WGANs

This repository contains wgan_model, a python module built on PyTorch for using WGANs to simulate from joint and conditional distributions of economic datasets. 

This [Google Colab Notebook](https://colab.research.google.com/drive/1AYvY4ZpCeHjEWLte39CFTs6_KgwRP-N6#scrollTo=NEX_jqVFFwS5) contains a tutorial for the code, including how to install requirements, and estimate and simulate from the resulting models, using a free Google GPU. The tutorial simulates from the Lalonde-Dehejia-Wahba dataset, as described in detail in the following paper. 

Athey, Susan, Guido Imbens, Jonas Metzger, and Evan Munro. 
"Using Wasserstein Generative Adversial Networks for the Design of Monte Carlo Simulations."
[arXiv:1909.02210](https://arxiv.org/abs/1909.02210). September 2019. 

The data folder contains the raw Lalonde-Dehejia-Wahba data.

#### Installation Instructions

For running the WGAN code outside of a Google Colab environment an installation of [python3](https://www.python.org/downloads/) is required. 

First, clone our repository. 
``` 
git clone https://www.github.com/gsbDBI/ds-wgan 
``` 

Then, in the ds-wgan folder, run 
``` 
pip install -r requirements.txt 
```

