.. _section_data:

Setting up Data
===============

In the following example we are interested in fitting the distribution of ``X`` (covariates) on ``t`` (treatment). The data set ``df`` includes all variables and has a control and treatment group, which are indicated by the variable ``context_var``. ``df`` is balanced with respect to ``context_var``.

We need to categorize the variables in ``df`` in the following way:

+ ``continuous_vars``: list of continuous variables to be generated
+ ``continuous_lower_bounds``: define lower bound of continuous variables (if applicable)
+ ``categorical_vars``: list of categorical variables to be generated
+ ``context_vars``: list of variables that are conditioned on for cWGANs (conditional Wasserstein Generative Adversarial Networks)


  .. code-block:: python

    continuous_vars = ["continuous_var_1", "continuous_var_2"]
    continuous_lower_bounds = {"continuous_var_1": 0}
    categorical_vars = ["categorical_var"]
    context_vars = ["context_var"]

:ref:`data_wrapper` prepares the data in ``df``. Before the training of the :ref:`generator` and :ref:`critic`, ``df`` is scaled using the function ``preprocess``. After the training procedure, ``df`` is rescaled to the original data set.

  .. code-block:: python

    data_wrappers = wgan.DataWrapper(df, continuous_vars, categorical_vars,
                                  context_vars, continuous_lower_bound)


:ref:`specifications` sets up the training specifications based on ``data_wrappers`` before training the :ref:`generator` and :ref:`critic`. The resulting object ``specs`` includes all the tuning parameters for the training process.
EVAN: add information on default specifications and when to use them

.. code-block:: python

    specs = wgan.Specifications(data_wrappers, batch_size=2048, max_epochs=600, critic_lr=1e-3,
                                generator_lr=1e-3, print_every=50, device = "cuda")

:ref:`generator` is the generator in the WGAN setup and generates new observations based on the distributions in the data set ``df``. The underlying function is a dense neural network. The only input required are the specifications ``specs``.

.. code-block:: python

    generators = wgan.Generator(specs)

:ref:`critic` is the discriminator in the WGAN setup and classifies observations as coming from ``df`` rather than from :ref:`generator`. The underlying function is a dense neural network.

.. code-block:: python

    critics = wgan.Critic(specs)


See the classes :ref:`data_wrapper`, :ref:`specifications`, :ref:`generator`, :ref:`critic` in Section :ref:`section_api` for more details on the code and the required parameters.
