.. _section_train:

Training Models
^^^^^^^^^^^^^^^

The function `train` trains the model.

  .. code-block:: python

    x, context = data_wrappers.preprocess(df)
    wgan.train(generators, critics, x, context, specs)


See the function :ref:`train` in Section :ref:`section_api` for more details on the code.
