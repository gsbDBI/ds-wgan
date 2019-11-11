Training Models and Generating Artificial Data
==============================================

.. _section_train:

Training Models
^^^^^^^^^^^^^^^

The function :ref:`train` trains the WGAN model, which is made up of the :ref:`generator` and :ref:`critic` (discriminator). If ``context`` is non-empty, a cWGAN is trained, otherwise the default is a regular WGAN.
The function is trained using stochastic optimization as described in detail in `Gulrajani et al 2017 <http://papers.nips.cc/paper/7159-improved-training-of-wasserstein-gans.pdf>`_.

  .. code-block:: python

    wgan.train(generator, critic, x, context, specs)


.. _section_gendata:

Generating Artificial Data
^^^^^^^^^^^^^^^^^^^^^^^^^^

The function ``apply_generator`` from class :ref:`data_wrapper` replaces columns in ``df``
that are produced by the generator. The generated data is of size equal to the number of rows in ``df``. Variables in ``def`` that are not
produced by the generator are not modified.

``df_generated`` contains the artificially generated data.

  .. code-block:: python

    df_generated = data_wrapper.apply_generator(generator, df.sample(int(1e6), replace=True))
