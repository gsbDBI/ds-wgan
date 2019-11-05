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

`DataWrapper` prepares the data in `df` in several ways. The attributes of the resulting object `data_wrappers` are the following:

+ list of variable names categorized above
+ list of means and standard deviations of continuous and context variables
+ list of dimensions of categorical variables
+ formatted lower bounds of continuous variables

  .. code-block:: python

    data_wrappers = wgan.DataWrapper(df, continuous_vars, categorical_vars,
                                  context_vars, continuous_lower_bound)


`Specifications` sets up the training specifications based on `data_wrappers` before training the `Generator` and `Critic`. The resulting object `specs` includes all the tuning parameters for the training process and its attributes are the following:

+ neural-network-related settings for training
+ settings related to the data dimensions and bounds


.. code-block:: python

    specs = wgan.Specifications(data_wrappers, batch_size=2048, max_epochs=600, critic_lr=1e-3, generator_lr=1e-3,
                               print_every=50, device = "cuda")

`Generator` is the generator in the WGAN setup and generates new observations based on the distributions in the data set `df`. The underlying function is a dense neural network. The only input required are the specifications `specs`.
The attributes of the resuting object `generators` are the following:

+ the formatted bounds of the continuous variables
+ the dimensions of each categorical variable
+ the total dimension of continuous variables
+ the total dimension of categorical variables
+ the dimension of noise input to generator
+ the dense neural network layers making up the generator
+ the dropout layer based on the specifications

.. code-block:: python

    generators = wgan.Generator(specs)

`Critic` is the discriminator in the WGAN setup and classifies observations as coming from `df` rather than from `Generator`. The underlying function is a dense neural network.

.. code-block:: python

    critics = wgan.Critic(specs)


See the classes :ref:`data_wrapper`, :ref:`specifications`, :ref:`generator`, :ref:`critic` in Section :ref:`section_api` for more details on the code and the required parameters.
