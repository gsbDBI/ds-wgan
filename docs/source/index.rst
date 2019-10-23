

Source Code Documentation
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Introduction
   Setting Up Data
   Training Models
   Generating Artificial Data
   Evaluating Models


Introduction
^^^^^^^^^^^^

Setting up Data
^^^^^^^^^^^^^^^

Define the type of variables

  .. code-block:: python

    continuous_vars_0 = ["age", "education", "re74", "re75"]
    continuous_lower_bounds_0 = {"re74": 0, "re75": 0}
    categorical_vars_0 = ["black", "hispanic", "married", "nodegree"]
    context_vars_0 = ["t"]


Normal text

  .. code-block:: python

    data_wrappers = [wgan.DataWrapper(df_balanced, continuous_vars_0, categorical_vars_0,
                                  context_vars_0, continuous_lower_bounds_0),
                 wgan.DataWrapper(df_balanced, continuous_vars_1, categorical_vars_1,
                                  context_vars_1, continuous_lower_bounds_1)]
    specs = [wgan.Specifications(dw, batch_size=2048, max_epochs=epochs, critic_lr=1e-3, generator_lr=1e-3,
                               print_every=50, device = "cuda") for dw, epochs in zip(data_wrappers, [600, 600])]
    generators = [wgan.Generator(spec) for spec in specs]
    critics = [wgan.Critic(spec) for spec in specs]

.. autoapimodule:: wgan
   :members: DataWrapper, Specifications, Generator, Critic
   :undoc-members:

Training Models
^^^^^^^^^^^^^^^

text

  .. code-block:: python

    x, context = data_wrappers[0].preprocess(df_balanced)
    wgan.train(generators[0], critics[0], x, context, specs[0])

.. autoapimodule:: wgan
   :members: train

Generating Artifical Data
^^^^^^^^^^^^^^^^^^^^^^^^^

  .. code-block:: python

    df_generated = data_wrappers[0].apply_generator(generators[0], df.sample(int(1e6), replace=True))
    df_generated = data_wrappers[1].apply_generator(generators[1], df_generated)
    df_generated_cf = copy(df_generated)
    df_generated_cf["t"] = 1 - df_generated_cf["t"]
    df_generated["re78_cf"] = data_wrappers[1].apply_generator(generators[1], df_generated_cf)["re78"]



Evaluating Models
^^^^^^^^^^^^^^^^^

  .. code-block:: python

    wgan.compare_dfs(df, df_generated,
                 scatterplot=dict(x=["re74", "age", "education"], y=["re78", "re75"], samples=400, smooth=0),
                 table_groupby=["t"],
                 histogram=dict(variables=["re78", "re74", "age", "education"], nrow=2, ncol=2),
                 figsize=3)



.. autoapimodule:: wgan
  :members: compare_dfs


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
