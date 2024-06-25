# A Framework for Ham Radio

This repo contains an experimental framework for automating the workflow of an amateur radio operator (ham). This work is currently in the early stages and probably not terribly useful as-is. The goal is to develop a disaggregated software stack that allows the end user to easily tailor the specific structure to a particular need by removing, modifying, or adding components.

This is developed on multiple different \*NIX platforms (most work is done on Debian related distros).  If it doesn't work on whatever it is you're using, please [open a github issue](https://github.com/ckuhtz/hamframe/issues) with details and maybe it will get fixed.  If you know how to fix it, please [submit a PR](https://github.com/ckuhtz/hamframe/pulls). Thank you!

You can read more about some of my thoughts [here](https://holdmybeer.io/2024/06/04/ham-stack-modernizing-the-wheel/), which may or may not be in sync with this repo. ¯\\\_(ツ)\_/¯ But they may explain some of the insanity behind this well-intentioned effort.

73 Christian AK7VV

### **Contributing**

- Clone the repo.
- Open the _hamframe.code-workspace_ file in Visual Studio Code.
- Open _command palette_, Python: Create Environment, follow prompts

### **Operation**

#### CLI

The directory _cli/_ contains the instructions and contents for building a [Docker](https://docker.io) container to contain and execute CLI commands to interact with the services.  It is also used to bootstrap the configuration.

- **make** builds a container image _hamframe-cli_ with can be used to interact with _cli/cli.py_.
- **make clean** prepares for another build.
- **make dist-clean** executes _clean_ and blows away all cached, unreferenced, and _hamframe-cli_ container images.

**docker run hamframe-cli** ___command___ executes a command known to _cli/cli.py_.

#### Configuration

##### Files 

Prototypes for configuration are stored in _config/_. The file _config/hamframe.toml_ contains the bootstrap for this specific instance _"instance_name"_. By convention, the files associated with this instance are located in a subdirectory _config/instance__name/_. The providers enabled are defined within _hamframe.toml_ for each instance.  Each provider name is present in the _instance_name/_ directory as _provider.toml_.
