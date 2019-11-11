

Source Code Documentation
========================================

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents:

   Setting Up Data <data>
   Training Models and Generating Artificial Data <train>
   Evaluating Models <evaluate>
   API <api>

.. _section_intro:

Introduction
============================

wgan is a python module built on top of `PyTorch <https://pytorch.org>`_ for using Wasserstein Generative Adversarial Network with Gradient Penalty
(`WGAN-GP <http://papers.nips.cc/paper/7159-improved-training-of-wasserstein-gans.pdf>`_) to simulate data with a known ground truth from real
datasets, in order to test the properties  of different estimators, as described in `Athey et al. [2019] <https://arxiv.org/abs/1909.02210>`_.
The module contains functionality to simulate from either joint or conditional distributions. This documentation
will explain how to set up the data, train the models, generate the artificial data and evaluate the models.

`Generative Adversarial Networks <http://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf>`_ (GANs) consist of two parts,
the generator and a discriminator. The generator generates new observations that look similar to training data by maximizing the probability
that the discriminator makes a mistake; the discriminator minimizes the probability of misclassifying generated data as real data.
In the wgan module both the generator and the discriminator are neural networks.

The workflow for fitting a distribution and generating data from it using the module is as follows:

#. :ref:`section_data`

    +   Load data into memory
    +   Initialize a :ref:`data_wrapper` object and specify the data type for each variable
    +   Initialize :ref:`specifications` object given the :ref:`data_wrapper`, which specifies hyperparameters for training
    +   Initialize :ref:`generator` (generator) & :ref:`critic` (discriminator) given the :ref:`specifications`
    +   Normalize the data with the :ref:`data_wrapper` object
    |
#. :ref:`section_train`:

    +   Train the :ref:`generator` & :ref:`critic` via :ref:`train`
    |
#. :ref:`section_gendata`

    +   Replace columns in df with simulated data from :ref:`generator` using :ref:`DataWrapper.apply_generator <data_wrapper>`
    |
#. :ref:`section_evaluate`:

    +   Check the generated data via :ref:`compare_dfs`
    +   Save generated data

For bug reports and feature requests, please submit an issue in the `Github repository <https://github.com/gsbDBI/ds-wgan>`_. The repository
also contains a Google Colab tutorial that can be accessed `here <https://colab.research.google.com/drive/1AYvY4ZpCeHjEWLte39CFTs6_KgwRP-N6#scrollTo=NEX_jqVFFwS5>`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
