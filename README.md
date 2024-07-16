# A Framework for Ham Radio

![GitHub Actions Workflow Status for CLI build](https://img.shields.io/github/actions/workflow/status/ak7vv/hamframe/cli.yml?branch=main&style=plastic&logo=github&label=CLI%20docker%20build-n-push&labelColor=purple&cacheSeconds=30&link=https%3A%2F%2Fgithub.com%2Fak7vv%2Fhamframe%2Factions%2Fworkflows%2Fcli.yml)
![GitHub Actions Workflow Status for API build](https://img.shields.io/github/actions/workflow/status/ak7vv/hamframe/api.yml?branch=main&style=plastic&logo=github&label=API%20docker%20build-n-push&labelColor=purple&cacheSeconds=30&link=https%3A%2F%2Fgithub.com%2Fak7vv%2Fhamframe%2Factions%2Fworkflows%2Fapi.yml)
![GitHub issues current open count](https://img.shields.io/github/issues-search?query=repo%3Aak7vv%2Fhamframe%20state%3Aopen&logo=github&label=current%20open%20issues%20count&labelColor=purple&style=plastic&color=teal)
![GitHub commit activity per month (main branch)](https://img.shields.io/github/commit-activity/m/ak7vv/hamframe/main)

## Intro

This repo contains an experimental framework for automating the workflow of an amateur radio operator (ham). This work is currently in the early stages and probably not terribly useful as-is. The goal is to develop a disaggregated software stack that allows the end user to easily tailor the specific structure to a particular need by removing, modifying, or adding components.

You can read more about some of my thoughts [here](https://holdmybeer.io/2024/06/04/ham-stack-modernizing-the-wheel/), which may or may not be in sync with this repo. ¯\\\_(ツ)\_/¯ But they may explain some of the insanity behind this well-intentioned effort.

And it probably goes without saying.. feedback is very welcome.

## Repo layout

```text
.
├── api
│   ├── api.py
│   ├── api.sh
│   ├── Dockerfile
│   ├── README.md
│   ├── requirements.txt
│   └── routers
│       ├── configuration
│       │   ├── operations.py
│       │   ├── put.py
│       │   ├── get.py
|       |   ├── update
│       │   └── delete.py
│       ├── database
│       │   ├── operations.py
│       │   └── ..
│       └── internal
│           ├── operations.py
│           └── ..
├── cli
│   ├── cli.py
│   ├── Dockerfile
│   ├── Makefile
│   └── requirements.txt
├── config
│   ├── ak7vv
│   │   └── ..
│   └── instance_name
│       ├── clublog.toml
│       ├── couchbase.toml
│       ├── hamframe.toml
│       ├── n0nbh.toml
│       ├── qrz.toml
│       ├── redis.toml
│       └── ..
├── doc
│   └── README.md
├── hamframe.code-workspace
├── LICENSE
├── README.md
└── requirements.txt
```

## **Contributing**

This is developed on multiple different \*NIX platforms (most work is done on Debian related distros).  If it doesn't work on whatever it is you're using, please [open a github issue](https://github.com/ak7vv/hamframe/issues) with details and maybe it will get fixed.  If you know how to fix it, please [submit a PR](https://github.com/ak7vv/hamframe/pulls). Thank you!

- Optional: Check the [open issues](https://github.com/ak7vv/hamframe/issues) to see if there's anything interesting just in case.
- Fork the repo.
- Open the _hamframe.code-workspace_ file in Visual Studio Code.
- Open _command palette_, Python: Create Environment, follow prompts

---

73 Christian AK7VV
