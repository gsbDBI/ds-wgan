.. _section_data:

Setting up Data
===============

In the following example we are interested in fitting the distribution of `X` (covariates) on `t` (treatment). The data set `df` includes all variables and has a control and treatment group, which are indicated by the variable `context_var`. `df` is balanced with respect to `context_var`.

We need to categorize the variables in `df` in the following way:

+ `continuous_vars`: list of continuous variables to be generated
+ `continuous_lower_bounds`: define lower bound of continuous variables (if applicable)
+ `categorical_vars`: list of categorical variables to be generated
+ `context_vars`: list of variables that are conditioned on for cWGANs (conditional Wasserstein Generative Adversarial Networks)


  .. code-block:: python

    continuous_vars = ["continuous_var_1", "continuous_var_2"]
    continuous_lower_bounds = {"continuous_var_1": 0}
    categorical_vars = ["categorical_var"]
    context_vars = ["context_var"]

The function `DataWrapper` prepares the data.

  .. code-block:: python

    data_wrappers = wgan.DataWrapper(df, continuous_vars, categorical_vars,
                                  context_vars, continuous_lower_bound)

`Specifications` sets up the training specifications before training the `Generator` and `Critic`.

.. code-block:: python

    specs = wgan.Specifications(dw, batch_size=2048, max_epochs=epochs, critic_lr=1e-3, generator_lr=1e-3,
                               print_every=50, device = "cuda") for dw, epochs in zip(data_wrappers, [600, 600])

`Generator` generates new observations based on the distributions in the original data set in the WGAN setup. The underlying function is a dense neural network.

.. code-block:: python

    generators = wgan.Generator(specs)

`Critic` is the discriminator in the WGAN setup. The underlying function is a dense neural network.

.. code-block:: python

    critics = wgan.Critic(specs)


See the classes :ref:`data_wrapper`, :ref:`specifications`, :ref:`generator`, :ref:`critic` in Section :ref:`section_api` for more details on the code.
