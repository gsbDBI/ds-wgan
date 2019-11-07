.. _section_train:

Training Models
^^^^^^^^^^^^^^^

The function :ref:`train` trains the model, more specifically the :ref:`generator` and the :ref:`critic` (discriminator). If a ``context_var`` is specified, a cWGAN is trained, the default is a regular WGAN.
The function is trained using a stochastic optimization given an optimizer and a gradient penalty as described in detail in `Gulrajani et al 2017 <http://papers.nips.cc/paper/7159-improved-training-of-wasserstein-gans.pdf>`_.

The function ``preprocess`` scales ``df``.

  .. code-block:: python

    wgan.train(generators, critics, x, context, specs)


See the function :ref:`train` in Section :ref:`section_api` for more details on the code and the required parameters.
