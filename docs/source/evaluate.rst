.. _section_evaluate:

Evaluating Models
=================

  .. code-block:: python

    wgan.compare_dfs(df, df_generated,
                 scatterplot=dict(x=["continuous_var_1"], y=["continuous_var_2"], samples=400, smooth=0),
                 table_groupby=["context_var"],
                 histogram=dict(variables=["continuous_var_1", "continuous_var_2"], nrow=2, ncol=2),
                 figsize=3)



See the function :ref:`compare_dfs` in the section :ref:`section_api` for more details on the code.
