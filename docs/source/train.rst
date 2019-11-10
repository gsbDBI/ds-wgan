.. _section_train:

Training Models
^^^^^^^^^^^^^^^

The function :ref:`train` trains the WGAN model, which is made up of the :ref:`generator` and :ref:`critic` (discriminator). If ``context`` is non-empty, a cWGAN is trained, otherwise the default is a regular WGAN.
The function is trained using stochastic optimization as described in detail in `Gulrajani et al 2017 <http://papers.nips.cc/paper/7159-improved-training-of-wasserstein-gans.pdf>`_.

  .. code-block:: python

    wgan.train(generator, critic, x, context, specs)
