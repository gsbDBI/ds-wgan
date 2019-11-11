.. _section_data:

Setting up Data and Models
==========================

In the following example we are interested in fitting the distribution of covariates conditional on a treatment.
The data set ``df`` includes covariates and the context variable, the treatment. Note that in some applications
where the original dataset is very unbalanced, for best results it may be necessary to balance the dataset
before training with respect to context variable.

To set up the :ref:`data_wrapper`, we need to categorize the variables in ``df`` in the following way:

+ ``continuous_vars``: list of continuous variables to be generated
+ ``continuous_lower_bounds``: define lower bound of continuous variables (if applicable)
+ ``continuous_upper_bounds``: define upper bound of continuous variables (if applicable)
+ ``categorical_vars``: list of categorical variables to be generated
+ ``context_vars``: list of variables that are conditioned on when generating data (cWGAN)

The default value for each of these settings is an empty list, but at least one of ``continuous_vars``
and ``categorical_vars`` must be non-empty when setting up a :ref:`data_wrapper`.

  .. code-block:: python

    continuous_vars = ["continuous_var_1", "continuous_var_2"]
    continuous_lower_bounds = {"continuous_var_1": 0}
    categorical_vars = ["categorical_var"]
    context_vars = ["t"]
    data_wrapper = wgan.DataWrapper(df, continuous_vars, categorical_vars,
                                  context_vars, continuous_lower_bound)

:ref:`data_wrapper` prepares the data in ``df``. Before the training of the :ref:`generator` and :ref:`critic`, ``df`` is scaled using the function :ref:`preprocess <data_wrapper>`.
After the training procedure, generated data is rescaled to the original data set.

  .. code-block:: python

    x, context = data_wrapper.preprocess(df)

If ``context_vars`` is an empty list, then :ref:`preprocess <data_wrapper>` will return an empty ``context``.
:ref:`specifications` specifies the tuning parameters for the training process based on a :ref:`data_wrapper`
before training the :ref:`generator` and :ref:`critic`.
The resulting object ``specs`` includes all the tuning parameters for the training process.

We include some suggested guidelines for the tuning parameters that we find need adjusting from the default values most frequently.
Training GANs is not always easy, so some experimentation is likely necessary with a new dataset before getting good results for the generated data. For a dataset
with `N` observations and `p` covariates:

+ ``batch_size`` should be a fraction of `N`, we found between 0.1 and 0.5 tends to work best
+ ``max_epochs`` is dataset specific: smaller `N` tends to require larger `max_epochs`
+ ``critic_d_hidden`` and ``generator_d_hidden`` should have larger widths for larger `p`

.. code-block:: python

    specs = wgan.Specifications(data_wrapper, batch_size=2048, max_epochs=600)

:ref:`generator` is the generator in the WGAN setup and generates new observations based on the distributions in the data set ``df``. The underlying function is a dense neural network. The only input required are the specifications ``specs``.

.. code-block:: python

    generator = wgan.Generator(specs)

:ref:`critic` is the discriminator in the WGAN setup and classifies observations as coming from ``df`` rather than from the :ref:`generator`. The underlying function is a dense neural network.

.. code-block:: python

    critic = wgan.Critic(specs)


See the classes :ref:`data_wrapper`, :ref:`specifications`, :ref:`generator`, :ref:`critic` in the :ref:`section_api` for more details, including
additional tuning parameters for advanced users.
