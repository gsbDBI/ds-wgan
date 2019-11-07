Introduction
============================

``wgan`` is a python module built on PyTorch for using WGANs (Wasserstein Generative Adversarial Networks) as introduced in `Athey et al. [2019] <https://arxiv.org/abs/1909.02210>`_. The module allows to simulate from joint and conditional distributions of economic datasets. The following documentation will explain how to set up the data, train the models, generate the artificial data and evaluate the models.

`Generative Adversarial Networks <http://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf>`_ (GANs) consist of two parts, the generator and a discriminator. The generator generates new observations based on the distribution of a training data set and  aims to maximize the probability of the discriminator making a mistake. The discriminator classifies observations as coming from the training data rather than the generator. Therefore, GANs can be seen as a two-player minmax game.
WGANs are GANs minimizing the Wasserstein distance. In the ``wgan`` module both the generator and the discriminator are neural networks.

The workflow for the fitting of a distribution is the following:

#. :ref:`section_data`

    +   Load and prepare data
    +   Initialize a :ref:`data_wrapper` object, which takes care of handling the data
    +   Initialize :ref:`specifications` object given the :ref:`data_wrapper`, which summarizes hyperparameters, etc.
    +   Initialize :ref:`generator` (generator) & :ref:`critic` (discriminator) given the :ref:`specifications`
    +   Preprocess the data with the :ref:`data_wrapper` object

#. :ref:`section_train`:

    +   Train the :ref:`generator` & :ref:`critic` via :ref:`train`

#. :ref:`section_gendata`

    +   Replace columns in df with simulated data from :ref:`generator` using ``DataWrapper.apply_generator``

#. :ref:`section_evaluate`:

    +   Explore the data via :ref:`compare_dfs` and save the new data.

If you run into any issues when using the ``wgan`` module, please submit an issue in the `Github repository <https://github.com/gsbDBI/ds-wgan>`_.

Additional resources:

+  Athey, Susan, Guido Imbens, Jonas Metzger, and Evan Munro. "Using Wasserstein Generative Adversial Networks for the Design of Monte Carlo Simulations." `arXiv:1909.02210 <https://arxiv.org/abs/1909.02210>`_. September 2019
+  The module also comes with a tutorial that can be accessed `here <https://colab.research.google.com/drive/1AYvY4ZpCeHjEWLte39CFTs6_KgwRP-N6#scrollTo=NEX_jqVFFwS5>`_
