.. _section_gendata:

Generating Artificial Data
==========================

The function ``apply_generator`` from class :ref:`data_wrapper` replaces columns in ``df``
that are produced by the generator. The generated data is of size equal to the number of rows in ``df``. Variables in ``def`` that are not
produced by the generator are not modified.

``df_generated`` contains the artificially generated data.

  .. code-block:: python

    df_generated = data_wrapper.apply_generator(generator, df.sample(int(1e6), replace=True))
