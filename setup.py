import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dswgan",
    version="0.1",
    author="Jonas Metzger and Evan Munro",
    author_email="munro@stanford.edu",
    description="Package for generating artificial data using Wasserstein Generative Adversarial Networks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gsDBI/ds-wgan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
