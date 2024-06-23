# Framework for Ham Radio

## Intro
This repo contains an experimental framework for automating the workflow of an amateur radio operator (ham), which is currently in the early stages. The goal is to develop a disaggregated software stack that allows the end user to easily tailor the specific structure to a particular need by removing, modifying, or adding components.

This is developed on multiple different \*NIX platforms (most work is done on Debian related distros).  If it doesn't work on whatever it is you're using, please [open a github issue](https://github.com/ckuhtz/hamframe/issues) with details and maybe it will get fixed.  If you know how to fix it, please [submit a PR](https://github.com/ckuhtz/hamframe/pulls). Thank you!

You can read more about some of my thoughts [here](https://holdmybeer.io/2024/06/04/ham-stack-modernizing-the-wheel/), which may or may not be in sync with this repo. ¯\\\_(ツ)\_/¯ But they may explain some of the insanity behind this well-intentioned effort.

73 Christian AK7VV

## Dev

- Clone the repo.
- Make sure you have virtualenv (___apt install python3-virtualenv___)
- Run ___virtualenv hamframe___ and initialize the virtual environment with ___hamframe/bin/activate___
- Make sure you're using the virtual environment by executing ___which python___ and it should refer to _hamframe/bin/python_

If this doesn't make sense, perhaps start reading [here](https://realpython.com/python-virtual-environments-a-primer/).