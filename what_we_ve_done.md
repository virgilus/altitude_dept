# What we've done

## Git

- We created a git repo. Then we cloned it into a new directory. 

- **TIP**: Make sure this directory is not tracked by Google Drive, Dropbox, iCloud, etc. Because git and these services don't work well together. Creating a folder named "code" inside your main user folder is usually a good idea.

- We modified .gitignore to ignore unnecessary files (like data files). We don't want to push data files to the repo because data are usually large and can bloat the repo.

## Conda env

We created a conda environment using the provided `requirements.txt` file.

To create the environment, run:

```conda create --n YOUR_ENV_NAME python=3.14```

If you have a channel error, try adding `-c conda-forge` at the end of the command. Like this :

```conda create --n YOUR_ENV_NAME python=3.14 -c conda-forge```

Then, activate the environment:

```conda activate YOUR_ENV_NAME```

To install the required packages, run:

```pip install -r requirements.txt```

Inside requirements.txt, we specified the packages we need. This is important to ensure compatibility and reproducibility.

It's better to specify the versions, but you can leave them out if you want the latest versions.

## Package

We created our own package called `altitude_dept` with a function to read the data file.

To make the package work, we added an `__init__.py` file that imports the functions from `func.py`.


## Folders

- We created a `notebooks` folder to store our Jupyter notebooks.
And a data folder to store our data files.

- Also inside the notebook we added '..' to the sys.path to be able to import the package from any notebook inside the `notebooks` folder.


## Workflow

The typical workflow consists of using a ipynb to test and experiment with the code, and then, as soon as it works, moving the code to the package.

It makes the code cleaner and more reusable and this will help us in the future when the project grows, especially when we are going to use visualisation libraries.