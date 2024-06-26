## **Operation**

### CLI

The directory _cli/_ contains the instructions and contents for building a [Docker](https://docker.io) container to contain and execute CLI commands to interact with the services.  It is also used to bootstrap the configuration.

- **make** builds a container image _hamframe-cli_ with can be used to interact with _cli/cli.py_.
- **make clean** prepares for another build.
- **make dist-clean** executes _clean_ and blows away all cached, unreferenced, and _hamframe-cli_ container images.

**docker run --rm hamframe-cli** _args_ executes a command known to _cli/cli.py_.

The CLI understands the following commands:

#### help

    Produces the command line help. Takes an optional argument to produce more detailed help for another command.

#### status

    Reports system status information.
    
    Required:
        --instance
        --confdir | --redis

---

### Configuration

#### Files 

Prototypes for configuration are stored in _config/_. The file _config/hamframe.toml_ contains the bootstrap for this specific instance _"instance_name"_. By convention, the files associated with this instance are located in a subdirectory _config/instance__name/_. The providers enabled are defined within _hamframe.toml_ for each instance.  Each provider name is present in the _instance_name/_ directory as _provider.toml_.

---
<P>

73 Christian AK7VV