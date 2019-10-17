
import os
import pandas as pd
import torch
import wgan
from utils import *


# Output setup
out_dir = get_write_dir(__file__)
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

# Simulation setup
if on_sherlock():
    batch_sizes = [1024, 2048]
    batch_size = choice(batch_sizes)
    max_epoch = 100
else:
    max_epoch = 100
    batch_size = 35

# Hardware setup
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
device = "cuda" if torch.cuda.is_available() else "cpu"


# Loading and sampling data
file = "data/generated/welfare_dropNA.csv"
df = pd.read_csv(file, na_values=-999)

df["t"] = df["w"]
df_balanced = df.sample(2*len(df), weights=(1-df.t.mean())*df.t+df.t.mean()*(1-df.t), replace=True) # balanced df for training


# X | t
continuous_vars_0 = ["hrs1", "prestg80", "sibs", "childs",  "age", "educ", "maeduc", "hompop", "babies", "preteen", "teens", "adults"]
categorical_vars_0 = ["wrkstat", "wrkslf", "occ80", "indus80", "marital", "degree",
                      "sex", "race", "res16", "reg16", "mobile16", "family16", "born",
                      "parborn", "partyid", "polviews",  "income", "rincome", "earnrs"]
context_vars_0 = ["t"]

# Y | X, t
continuous_vars_1 = ["y"]
continuous_lower_bounds_1 = {"y": 0}
context_vars_1 = ["w", "wrkstat", "hrs1", "wrkslf", "occ80", "prestg80", "indus80",
                  "marital", "sibs", "childs", "age", "educ", "maeduc", "degree",
                  "sex", "race", "res16", "reg16",  "mobile16", "family16", "born",
                  "parborn", "hompop", "babies", "preteen", "teens", "adults",
                  "earnrs", "income" , "rincome", "partyid", "polviews"]

# Data transformers
data_wrappers = [
    wgan.DataWrapper(df_balanced,
                     continuous_vars_0,
                     categorical_vars_0,
                     context_vars_0
                     ),
    wgan.DataWrapper(df_balanced,

                     context_vars_1,
                     continuous_lower_bounds_1)
]
specs = [
    wgan.Specifications(dw,
                        batch_size=batch_size,
                        max_epochs=max_epoch,
                        print_every=50,
                        device=device)
    for dw in data_wrappers
]

# Initialize generator and critic
generators = [wgan.Generator(spec) for spec in specs]
critics = [wgan.Critic(spec) for spec in specs]

# train X | t
x, context = data_wrappers[0].preprocess(df_balanced)
wgan.train(generators[0], critics[0], x, context, specs[0])

# train Y | X, t
x, context = data_wrappers[1].preprocess(df_balanced)
wgan.train(generators[1], critics[1], x, context, specs[1])

# simulate data with conditional WGANs
df_generated = data_wrappers[0].apply_generator(generators[0], df.sample(int(1e5), replace=True))
df_generated = data_wrappers[1].apply_generator(generators[1], df_generated)

# add counterfactual outcomes
df_generated_cf = df_generated
df_generated_cf["t"] = 1 - df_generated_cf["t"]
df_generated["y_cf"] = data_wrappers[1].apply_generator(generators[1], df_generated_cf)["y"]

# Save all configurations
df_generated["batch_size"] = batch_size
df_generated["max_epoch"] = max_epoch
df_generated["complexity"] = specs[0].settings["gaussian_similarity_penalty"]

filename = f"{get_id()}.feather"
# save to .feather
output_filename = join(out_dir, filename)
df_generated.to_feather(output_filename)

print("att:", ((df_generated.y - df_generated.y_cf) * (2 * df_generated.t - 1)).mean())

#wgan.compare_dfs(df,
    #             df_generated,
    #             scatterplot=dict(x=["re74", "age", "education"],
     #                             y=["re78", "re75"],
     #                             samples=400,
      #                            smooth=0),
      #           table_groupby=["t"],
       #          histogram=dict(variables=["re78", "re74", "age", "education"],
       #                         nrow=2,
       #                         ncol=2),
        #         figsize=3)
