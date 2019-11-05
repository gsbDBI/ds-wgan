.. _section_evaluate:

Evaluating Models
=================

The function `compare_dfs` compares the real data set `df` and the artificially generated data set `df_generated` from the WGANs. The output are a comparison of means, comparisons of standard deviations, histograms and scatterplots to evaluate the performance of the WGAN.

  .. code-block:: python

    wgan.compare_dfs(df, df_generated,
                 scatterplot=dict(x=["continuous_var_1"], y=["continuous_var_2"], samples=400, smooth=0),
                 table_groupby=["context_var"],
                 histogram=dict(variables=["continuous_var_1", "continuous_var_2"], nrow=2, ncol=2),
                 figsize=3)



See the function :ref:`compare_dfs` in the section :ref:`section_api` for more details on the code and the required parameters.
