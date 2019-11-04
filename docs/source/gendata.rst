.. _section_gendata:

Generating Artifical Data
=========================

  .. code-block:: python

    df_generated = data_wrappers.apply_generator(generators, df.sample(int(1e6), replace=True))
    df_generated_cf = copy(df_generated)
    df_generated_cf["context_var"] = 1 - df_generated_cf["context_var"]

See the class :ref:`data_wrapper` in Section :ref:`section_api` for more details on the code.
