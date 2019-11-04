Introduction
============================

`wgan` is a python module built on PyTorch for using WGANs (Wasserstein Generative Adversarial Networks) to simulate from joint and conditional distributions of economic datasets. The following documentation will explain how to set up the data, train the models, generate the artificial data and evaluate the models.

The workflow for the fitting of a distribution is the following:

#. :ref:`section_data`

  + Load and prepare data
  + Initialize a :ref:`data_wrapper` object, which takes care of handling the data
  + Initialize :ref:`specifications` object given the :ref:`data_wrapper`, which summarizes hyperparameters, etc.
  + Initialize :ref:`generator` & :ref:`critic` given the :ref:`specifications`
  + Preprocess the data with the :ref:`data_wrapper` object

#. :ref:`section_train`:

  + Train the :ref:`generator` & :ref:`critic` via :ref:`train`

#. :ref:`section_gendata`

  + Replace columns in df with simulated data from :ref:`generator` using `DataWrapper.apply_generator`

#. :ref:`section_train`:

  + Explore the data via :ref:`compare_dfs` and save the new data.

Additional resources:

+  Athey, Susan, Guido Imbens, Jonas Metzger, and Evan Munro. "Using Wasserstein Generative Adversial Networks for the Design of Monte Carlo Simulations." `arXiv:1909.02210 <https://arxiv.org/abs/1909.02210>`_. September 2019
+  `github <https://github.com/gsbDBI/ds-wgan>`_
+  The module also comes with a tutorial that can be accessed `here <https://colab.research.google.com/drive/1AYvY4ZpCeHjEWLte39CFTs6_KgwRP-N6#scrollTo=NEX_jqVFFwS5>`_
