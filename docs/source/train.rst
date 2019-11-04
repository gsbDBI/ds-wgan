.. _section_train:

Training Models
^^^^^^^^^^^^^^^

The function `train` trains the model, more specifically the generator and the critic (discriminator). If a `context_var` is specified, a cWGAN is trained, the default is a regular WGAN.
The training procedure is described in detail in `Gulrajani et al 2017 <http://papers.nips.cc/paper/7159-improved-training-of-wasserstein-gans.pdf>`_.

  .. code-block:: python

    x, context = data_wrappers.preprocess(df)
    wgan.train(generators, critics, x, context, specs)


See the function :ref:`train` in Section :ref:`section_api` for more details on the code.
