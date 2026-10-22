[Skip to content](https://docs.astral.sh/uv/guides/#guides-overview)

# [Guides overview](https://docs.astral.sh/uv/guides/\#guides-overview)

Check out one of the core guides to get started:

- [Installing Python versions](https://docs.astral.sh/uv/guides/install-python/)
- [Running scripts and declaring dependencies](https://docs.astral.sh/uv/guides/scripts/)
- [Running and installing applications as tools](https://docs.astral.sh/uv/guides/tools/)
- [Creating and working on projects](https://docs.astral.sh/uv/guides/projects/)
- [Building and publishing packages](https://docs.astral.sh/uv/guides/package/)
- [Integrate uv with other software, e.g., Docker, GitHub, PyTorch, and more](https://docs.astral.sh/uv/guides/integration/)

Or, explore the [concept documentation](https://docs.astral.sh/uv/concepts/) for a comprehensive breakdown of each
feature.

Back to top

---

[Skip to content](https://docs.astral.sh/uv/guides/integration/jupyter/#using-uv-with-jupyter)

# [Using uv with Jupyter](https://docs.astral.sh/uv/guides/integration/jupyter/\#using-uv-with-jupyter)

The [Jupyter](https://jupyter.org/) notebook is a popular tool for interactive computing, data
analysis, and visualization. You can use Jupyter with uv in a few different ways, either to interact
with a project, or as a standalone tool.

## [Using Jupyter within a project](https://docs.astral.sh/uv/guides/integration/jupyter/\#using-jupyter-within-a-project)

If you're working within a [project](https://docs.astral.sh/uv/concepts/projects/), you can start a Jupyter
server with access to the project's virtual environment via the following:

```
$ uv run --with jupyter jupyter lab
```

By default, `jupyter lab` will start the server at
[http://localhost:8888/lab](http://localhost:8888/lab).

Within a notebook, you can import your project's modules as you would in any other file in the
project. For example, if your project depends on `requests`, `import requests` will import
`requests` from the project's virtual environment.

If you're looking for read-only access to the project's virtual environment, then there's nothing
more to it. However, if you need to install additional packages from within the notebook, there are
a few extra details to consider.

### [Creating a kernel](https://docs.astral.sh/uv/guides/integration/jupyter/\#creating-a-kernel)

If you need to install packages from within the notebook, we recommend creating a dedicated kernel
for your project. Kernels enable the Jupyter server to run in one environment, with individual
notebooks running in their own, separate environments.

In the context of uv, we can create a kernel for a project while installing Jupyter itself in an
isolated environment, as in `uv run --with jupyter jupyter lab`. Creating a kernel for the project
ensures that the notebook is hooked up to the correct environment, and that any packages installed
from within the notebook are installed into the project's virtual environment.

To create a kernel, you'll need to install `ipykernel` as a development dependency:

```
$ uv add --dev ipykernel
```

Then, you can create the kernel for `project` with:

```
$ uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=project
```

From there, start the server with:

```
$ uv run --with jupyter jupyter lab
```

When creating a notebook, select the `project` kernel from the dropdown. Then use `!uv add pydantic`
to add `pydantic` to the project's dependencies, or `!uv pip install pydantic` to install `pydantic`
into the project's virtual environment without persisting the change to the project `pyproject.toml`
or `uv.lock` files. Either command will make `import pydantic` work within the notebook.

### [Installing packages without a kernel](https://docs.astral.sh/uv/guides/integration/jupyter/\#installing-packages-without-a-kernel)

If you don't want to create a kernel, you can still install packages from within the notebook.
However, there are a few caveats to consider.

Though `uv run --with jupyter` runs in an isolated environment, within the notebook itself,
`!uv add` and related commands will modify the _project's_ environment, even without a kernel.

For example, running `!uv add pydantic` from within a notebook will add `pydantic` to the project's
dependencies and virtual environment, such that `import pydantic` will work immediately, without
further configuration or a server restart.

However, since the Jupyter server is the "active" environment, `!uv pip install` will install
packages into _Jupyter's_ environment, not the project environment. Such dependencies will persist
for the lifetime of the Jupyter server, but may disappear on subsequent `jupyter` invocations.

If you're working with a notebook that relies on pip (e.g., via the `%pip` magic), you can include
pip in your project's virtual environment by running `uv venv --seed` prior to starting the Jupyter
server. For example, given:

```
$ uv venv --seed
$ uv run --with jupyter jupyter lab
```

Subsequent `%pip install` invocations within the notebook will install packages into the project's
virtual environment. However, such modifications will _not_ be reflected in the project's
`pyproject.toml` or `uv.lock` files.

## [Using Jupyter as a standalone tool](https://docs.astral.sh/uv/guides/integration/jupyter/\#using-jupyter-as-a-standalone-tool)

If you ever need ad hoc access to a notebook (i.e., to run a Python snippet interactively), you can
start a Jupyter server at any time with `uv tool run jupyter lab`. This will run a Jupyter server in
an isolated environment.

## [Using Jupyter with a non-project environment](https://docs.astral.sh/uv/guides/integration/jupyter/\#using-jupyter-with-a-non-project-environment)

If you need to run Jupyter in a virtual environment that isn't associated with a
[project](https://docs.astral.sh/uv/concepts/projects/) (e.g., has no `pyproject.toml` or `uv.lock`), you can do
so by adding Jupyter to the environment directly. For example:

[macOS and Linux](https://docs.astral.sh/uv/guides/integration/jupyter/#__tabbed_1_1)[Windows](https://docs.astral.sh/uv/guides/integration/jupyter/#__tabbed_1_2)

```
$ uv venv --seed
$ uv pip install pydantic
$ uv pip install jupyterlab
$ .venv/bin/jupyter lab
```

```
PS> uv venv --seed
PS> uv pip install pydantic
PS> uv pip install jupyterlab
PS> .venv\Scripts\jupyter lab
```

From here, `import pydantic` will work within the notebook, and you can install additional packages
via `!uv pip install`, or even `!pip install`.

## [Using Jupyter from VS Code](https://docs.astral.sh/uv/guides/integration/jupyter/\#using-jupyter-from-vs-code)

You can also engage with Jupyter notebooks from within an editor like VS Code. To connect a
uv-managed project to a Jupyter notebook within VS Code, we recommend creating a kernel for the
project, as in the following:

```
# Create a project.
$ uv init project

# Move into the project directory.
$ cd project

# Add ipykernel as a dev dependency.
$ uv add --dev ipykernel

# Open the project in VS Code.
$ code .
```

Once the project directory is open in VS Code, you can create a new Jupyter notebook by selecting
"Create: New Jupyter Notebook" from the command palette. When prompted to select a kernel, choose
"Python Environments" and select the virtual environment you created earlier (e.g.,
`.venv/bin/python` on macOS and Linux, or `.venv\Scripts\python` on Windows).

Note

VS Code requires `ipykernel` to be present in the project environment. If you'd prefer to avoid
adding `ipykernel` as a dev dependency, you can install it directly into the project environment
with `uv pip install ipykernel`.

If you need to manipulate the project's environment from within the notebook, you may need to add
`uv` as an explicit development dependency:

```
$ uv add --dev uv
```

From there, you can use `!uv add pydantic` to add `pydantic` to the project's dependencies, or
`!uv pip install pydantic` to install `pydantic` into the project's virtual environment without
updating the project's `pyproject.toml` or `uv.lock` files.

---

[Skip to content](https://docs.astral.sh/uv/guides/integration/pre-commit/#using-uv-in-pre-commit)

# [Using uv in pre-commit](https://docs.astral.sh/uv/guides/integration/pre-commit/\#using-uv-in-pre-commit)

An official pre-commit hook is provided at
[`astral-sh/uv-pre-commit`](https://github.com/astral-sh/uv-pre-commit).

To use uv with pre-commit, add one of the following examples to the `repos` list in the
`.pre-commit-config.yaml`.

To make sure your `uv.lock` file is up to date even if your `pyproject.toml` file was changed:

.pre-commit-config.yaml

```
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.13.4
    hooks:
      - id: uv-lock
```

To keep a `requirements.txt` file in sync with your `uv.lock` file:

.pre-commit-config.yaml

```
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.13.4
    hooks:
      - id: uv-export
```

To compile requirements files:

.pre-commit-config.yaml

```
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.13.4
    hooks:
      # Compile requirements
      - id: pip-compile
        args: [requirements.in, -o, requirements.txt]
```

To compile alternative requirements files, modify `args` and `files`:

.pre-commit-config.yaml

```
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.13.4
    hooks:
      # Compile requirements
      - id: pip-compile
        args: [requirements-dev.in, -o, requirements-dev.txt]
        files: ^requirements-dev\.(in|txt)$
```

To run the hook over multiple files at the same time, add additional entries:

.pre-commit-config.yaml

```
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.13.4
    hooks:
      # Compile requirements
      - id: pip-compile
        name: pip-compile requirements.in
        args: [requirements.in, -o, requirements.txt]
      - id: pip-compile
        name: pip-compile requirements-dev.in
        args: [requirements-dev.in, -o, requirements-dev.txt]
        files: ^requirements-dev\.(in|txt)$
```

Back to top

---

[Skip to content](https://docs.astral.sh/uv/guides/integration/aws/#aws-codeartifact)

# [AWS CodeArtifact](https://docs.astral.sh/uv/guides/integration/aws/\#aws-codeartifact)

uv can install packages from
[AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html), either by
using an access token, or using the [`keyring`](https://github.com/jaraco/keyring) package.

Note

This guide assumes that [`awscli`](https://aws.amazon.com/cli/) is installed and authenticated.

The index can be declared like so:

pyproject.toml

```
[[tool.uv.index]]
name = "private-registry"
url = "https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/simple/"
```

## [Authenticate with an AWS access token](https://docs.astral.sh/uv/guides/integration/aws/\#authenticate-with-an-aws-access-token)

Credentials can be provided via the "Basic" HTTP authentication scheme. Include the access token in
the password field of the URL. The username must be `aws`, otherwise authentication will fail.

Generate a token with `awscli`:

```
export AWS_CODEARTIFACT_TOKEN="$(
    aws codeartifact get-authorization-token \
    --domain <DOMAIN> \
    --domain-owner <ACCOUNT_ID> \
    --query authorizationToken \
    --output text
)"
```

Note

This is a basic example; you might need to pass extra parameters to generate the token, such as
`--region`.

Then set credentials for the index with:

```
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=aws
export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="$AWS_CODEARTIFACT_TOKEN"
```

Note

`PRIVATE_REGISTRY` should match the name of the index defined in your `pyproject.toml`.

## [Authenticate with `keyring` and `keyrings.codeartifact`](https://docs.astral.sh/uv/guides/integration/aws/\#authenticate-with-keyring-and-keyringscodeartifact)

You can also authenticate to CodeArtifact using the [`keyring`](https://github.com/jaraco/keyring)
package with the [`keyrings.codeartifact` plugin](https://github.com/jmkeyes/keyrings.codeartifact).
Because these two packages are required to authenticate to CodeArtifact, they must be pre-installed
from a source other than CodeArtifact.

The `keyrings.codeartifact` plugin wraps [boto3](https://pypi.org/project/boto3/) to generate
short-lived access tokens, securely store them in system keyring, and refresh them when they are
expired.

uv only supports using the `keyring` package in
[subprocess mode](https://docs.astral.sh/uv/reference/settings/#keyring-provider). The `keyring` executable must be in
the `PATH`, i.e., installed globally or in the active environment. The `keyring` CLI requires a
username in the URL and it must be `aws`.

```
# Pre-install keyring and AWS CodeArtifact plugin from the public PyPI
uv tool install keyring --with keyrings.codeartifact

# Enable keyring authentication
export UV_KEYRING_PROVIDER=subprocess

# Set the username for the index
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=aws
```

Note

The [`tool.uv.keyring-provider`](https://docs.astral.sh/uv/reference/settings/#keyring-provider)
setting can be used to enable keyring in your `uv.toml` or `pyproject.toml`.

Similarly, the username for the index can be added directly to the index URL.

## [Publishing packages](https://docs.astral.sh/uv/guides/integration/aws/\#publishing-packages)

If you also want to publish your own packages to AWS CodeArtifact, you can use `uv publish` as
described in the [Building and publishing guide](https://docs.astral.sh/uv/guides/package/).

First, add a `publish-url` to the index you want to publish packages to. For example:

pyproject.toml

```
[[tool.uv.index]]
name = "private-registry"
url = "https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/simple/"
publish-url = "https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/"
```

Then, configure credentials (if not using keyring):

```
$ export UV_PUBLISH_USERNAME=aws
$ export UV_PUBLISH_PASSWORD="$AWS_CODEARTIFACT_TOKEN"
```

And publish the package:

```
$ uv publish --index private-registry
```

To use `uv publish` without adding the `publish-url` to the project, you can set `UV_PUBLISH_URL`:

```
$ export UV_PUBLISH_URL=https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/
$ uv publish
```

Note this method is not preferable because uv cannot check if the package is already published
before uploading artifacts.

Back to top

---

[Skip to content](https://docs.astral.sh/uv/guides/integration/marimo/#using-uv-with-marimo)

# [Using uv with marimo](https://docs.astral.sh/uv/guides/integration/marimo/\#using-uv-with-marimo)

[marimo](https://github.com/marimo-team/marimo) is an open-source Python notebook that blends
interactive computing with the reproducibility and reusability of traditional software, letting you
version with Git, run as scripts, and share as apps. Because marimo notebooks are stored as pure
Python scripts, they are able to integrate tightly with uv.

You can readily use marimo as a standalone tool, as self-contained scripts, in projects, and in
non-project environments.

## [Using marimo as a standalone tool](https://docs.astral.sh/uv/guides/integration/marimo/\#using-marimo-as-a-standalone-tool)

For ad-hoc access to marimo notebooks, start a marimo server at any time in an isolated environment
with:

```
$ uvx marimo edit
```

Start a specific notebook with:

```
$ uvx marimo edit my_notebook.py
```

## [Using marimo with inline script metadata](https://docs.astral.sh/uv/guides/integration/marimo/\#using-marimo-with-inline-script-metadata)

Because marimo notebooks are stored as Python scripts, they can encapsulate their own dependencies
using inline script metadata, via uv's [support for scripts](https://docs.astral.sh/uv/guides/scripts/). For example,
to add `numpy` as a dependency to your notebook, use this command:

```
$ uv add --script my_notebook.py numpy
```

To interactively edit a notebook containing inline script metadata, use:

```
$ uvx marimo edit --sandbox my_notebook.py
```

marimo will automatically use uv to start your notebook in an isolated virtual environment with your
script's dependencies. Packages installed from the marimo UI will automatically be added to the
notebook's script metadata.

You can optionally run these notebooks as Python scripts, without opening an interactive session:

```
$ uv run my_notebook.py
```

## [Using marimo within a project](https://docs.astral.sh/uv/guides/integration/marimo/\#using-marimo-within-a-project)

If you're working within a [project](https://docs.astral.sh/uv/concepts/projects/), you can start a marimo
notebook with access to the project's virtual environment via the following command (assuming marimo
is a project dependency):

```
$ uv run marimo edit my_notebook.py
```

To make additional packages available to your notebook, either add them to your project with
`uv add`, or use marimo's built-in package installation UI, which will invoke `uv add` on your
behalf.

If marimo is not a project dependency, you can still run a notebook with the following command:

```
$ uv run --with marimo marimo edit my_notebook.py
```

This will let you import your project's modules while editing your notebook. However, packages
installed via marimo's UI when running in this way will not be added to your project, and may
disappear on subsequent marimo invocations.

## [Using marimo in a non-project environment](https://docs.astral.sh/uv/guides/integration/marimo/\#using-marimo-in-a-non-project-environment)

To run marimo in a virtual environment that isn't associated with a
[project](https://docs.astral.sh/uv/concepts/projects/), add marimo to the environment directly:

```
$ uv venv
$ uv pip install numpy
$ uv pip install marimo
$ uv run marimo edit
```

From here, `import numpy` will work within the notebook, and marimo's UI installer will add packages
to the environment with `uv pip install` on your behalf.

## [Running marimo notebooks as scripts](https://docs.astral.sh/uv/guides/integration/marimo/\#running-marimo-notebooks-as-scripts)

Regardless of how your dependencies are managed (with inline script metadata, within a project, or
with a non-project environment), you can run marimo notebooks as scripts with:

```
$ uv run my_notebook.py
```

This executes your notebook as a Python script, without opening an interactive session in your
browser.

Back to top

---

[Skip to content](https://docs.astral.sh/uv/guides/integration/#integration-guides)

# [Integration guides](https://docs.astral.sh/uv/guides/integration/\#integration-guides)

Learn how to integrate uv with other software:

- [Using in Docker images](https://docs.astral.sh/uv/guides/integration/docker/)
- [Using with Jupyter notebooks](https://docs.astral.sh/uv/guides/integration/jupyter/)
- [Using with marimo notebooks](https://docs.astral.sh/uv/guides/integration/marimo/)
- [Using with pre-commit](https://docs.astral.sh/uv/guides/integration/pre-commit/)
- [Using in GitHub Actions](https://docs.astral.sh/uv/guides/integration/github/)
- [Using in GitLab CI/CD](https://docs.astral.sh/uv/guides/integration/gitlab/)
- [Installing PyTorch](https://docs.astral.sh/uv/guides/integration/pytorch/)
- [Building a FastAPI application](https://docs.astral.sh/uv/guides/integration/fastapi/)
- [Using with Bazel](https://docs.astral.sh/uv/guides/integration/bazel/)
- [Using with Azure Artifacts](https://docs.astral.sh/uv/guides/integration/azure/)
- [Using with Google Artifact Registry](https://docs.astral.sh/uv/guides/integration/google/)
- [Using with AWS CodeArtifact](https://docs.astral.sh/uv/guides/integration/aws/)
- [Using with JFrog Artifactory](https://docs.astral.sh/uv/guides/integration/jfrog/)
- [Using with Renovate](https://docs.astral.sh/uv/guides/integration/renovate/)
- [Using with Dependabot](https://docs.astral.sh/uv/guides/integration/dependabot/)
- [Using with AWS Lambda](https://docs.astral.sh/uv/guides/integration/aws-lambda/)
- [Using with Coiled](https://docs.astral.sh/uv/guides/integration/coiled/)

Or, explore the [concept documentation](https://docs.astral.sh/uv/concepts/) for a comprehensive breakdown of
each feature.

Back to top

---

[Skip to content](https://docs.astral.sh/uv/guides/integration/pytorch/#using-uv-with-pytorch)

# [Using uv with PyTorch](https://docs.astral.sh/uv/guides/integration/pytorch/\#using-uv-with-pytorch)

The [PyTorch](https://pytorch.org/) ecosystem is a popular choice for deep learning research and
development. You can use uv to manage PyTorch projects and PyTorch dependencies across different
Python versions and environments, even controlling for the choice of accelerator (e.g., CPU-only vs.
CUDA).

Note

Some of the features outlined in this guide require uv version 0.5.3 or later. We recommend upgrading prior to configuring PyTorch.

## [Installing PyTorch](https://docs.astral.sh/uv/guides/integration/pytorch/\#installing-pytorch)

From a packaging perspective, PyTorch has a few uncommon characteristics:

- Many PyTorch wheels are hosted on a dedicated index, rather than the Python Package Index (PyPI).
As such, installing PyTorch often requires configuring a project to use the PyTorch index.
- PyTorch produces distinct builds for each accelerator (e.g., CPU-only, CUDA). Since there's no
standardized mechanism for specifying these accelerators when publishing or installing, PyTorch
encodes them in the local version specifier. As such, PyTorch versions will often look like
`2.11.0+cpu`, `2.11.0+cu130`, etc.
- Builds for different accelerators are published to different indexes. For example, the `+cpu`
builds are published on [https://download.pytorch.org/whl/cpu](https://download.pytorch.org/whl/cpu), while the `+cu130` builds are
published on [https://download.pytorch.org/whl/cu130](https://download.pytorch.org/whl/cu130).

As such, the necessary packaging configuration will vary depending on both the platforms you need to
support and the accelerators you want to enable.

To start, consider the following (default) configuration, which would be generated by running
`uv init --python 3.14` followed by `uv add torch torchvision`.

In this case, PyTorch would be installed from PyPI, which hosts CPU-only wheels for Windows and
macOS, and GPU-accelerated wheels on Linux (targeting CUDA 13.0, as of PyTorch 2.11.0):

```
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [\
  "torch>=2.11.0",\
  "torchvision>=0.26.0",\
]
```

This is a valid configuration for projects that want to use CPU builds on Windows and macOS, and
CUDA-enabled builds on Linux. However, if you need to support different platforms or accelerators,
you'll need to configure the project accordingly.

## [Using a PyTorch index](https://docs.astral.sh/uv/guides/integration/pytorch/\#using-a-pytorch-index)

In some cases, you may want to use a specific PyTorch variant across all platforms. For example, you
may want to use the CPU-only builds on Linux too.

In such cases, the first step is to add the relevant PyTorch index to your `pyproject.toml`:

[CPU-only](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_1_1)[CUDA 11.8](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_1_2)[CUDA 12.6](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_1_3)[CUDA 12.8](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_1_4)[CUDA 13.0](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_1_5)[ROCm 7.2](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_1_6)[Intel GPUs](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_1_7)

```
[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true
```

```
[[tool.uv.index]]
name = "pytorch-cu118"
url = "https://download.pytorch.org/whl/cu118"
explicit = true
```

```
[[tool.uv.index]]
name = "pytorch-cu126"
url = "https://download.pytorch.org/whl/cu126"
explicit = true
```

```
[[tool.uv.index]]
name = "pytorch-cu128"
url = "https://download.pytorch.org/whl/cu128"
explicit = true
```

```
[[tool.uv.index]]
name = "pytorch-cu130"
url = "https://download.pytorch.org/whl/cu130"
explicit = true
```

```
[[tool.uv.index]]
name = "pytorch-rocm"
url = "https://download.pytorch.org/whl/rocm7.2"
explicit = true
```

```
[[tool.uv.index]]
name = "pytorch-xpu"
url = "https://download.pytorch.org/whl/xpu"
explicit = true
```

We recommend the use of `explicit = true` to ensure that the index is _only_ used for `torch`,
`torchvision`, and other PyTorch-related packages, as opposed to generic dependencies like `jinja2`,
which should continue to be sourced from the default index (PyPI).

Next, update the `pyproject.toml` to point `torch` and `torchvision` to the desired index:

[CPU-only](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_2_1)[CUDA 11.8](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_2_2)[CUDA 12.6](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_2_3)[CUDA 12.8](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_2_4)[CUDA 13.0](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_2_5)[ROCm 7.2](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_2_6)[Intel GPUs](https://docs.astral.sh/uv/guides/integration/pytorch/#__tabbed_2_7)

```
[tool.uv.sources]
torch = [\
  { index = "pytorch-cpu" },\
]
torchvision = [\
  { index = "pytorch-cpu" },\
]
```

PyTorch doesn't publish CUDA builds for macOS. As such, we gate on `sys_platform` to instruct uv to use
the PyTorch index on Linux and Windows, but fall back to PyPI on macOS:

```
[tool.uv.sources]
torch = [\
  { index = "pytorch-cu118", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },\
]
torchvision = [\
  { index = "pytorch-cu118", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },\
]
```

PyTorch doesn't publish CUDA builds for macOS. As such, we gate on `sys_platform` to instruct uv to limit
the PyTorch index to Linux and Windows, falling back to PyPI on macOS:

```
[tool.uv.sources]
torch = [\
  { index = "pytorch-cu126", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },\
]
torchvision = [\
  { index = "pytorch-cu126", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },\
]
```

PyTorch doesn't publish CUDA builds for macOS. As such, we gate on `sys_platform` to instruct uv to limit
the PyTorch index to Linux and Windows, falling back to PyPI on macOS:

```
[tool.uv.sources]
torch = [\
  { index = "pytorch-cu128", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },\
]
torchvision = [\
  { index = "pytorch-cu128", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },\
]
```

PyTorch doesn't publish CUDA builds for macOS. As such, we gate on `sys_platform` to instruct uv to limit
the PyTorch index to Linux and Windows, falling back to PyPI on macOS:

```
[tool.uv.sources]
torch = [\
  { index = "pytorch-cu130", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },\
]
torchvision = [\
  { index = "pytorch-cu130", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },\
]
```

PyTorch doesn't publish ROCm builds for macOS or Windows. As such, we gate on `sys_platform` to instruct uv
to limit the PyTorch index to Linux, falling back to PyPI on macOS and Windows:

```
[tool.uv.sources]
torch = [\
  { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },\
]
torchvision = [\
  { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },\
]
# ROCm support relies on both Triton packages, which should also be installed from
# the PyTorch index (and included in `project.dependencies`).
pytorch-triton-rocm = [\
  { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },\
]
triton-rocm = [\
  { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },\
]
```

PyTorch doesn't publish Intel GPU builds for macOS. As such, we gate on `sys_platform` to instruct uv to limit
the PyTorch index to Linux and Windows, falling back to PyPI on macOS:

```
[tool.uv.sources]
torch = [\
  { index = "pytorch-xpu", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },\
]
torchvision = [\
  { index = "pytorch-xpu", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },\
]
# Intel GPU support relies on `triton-xpu`, which should also be installed from the PyTorch index
# (and included in `project.dependencies`).
triton-xpu = [\
  { index = "pytorch-xpu", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },\
]
```

As a complete example, the following project would use PyTorch's CPU-only builds on all platforms:

```
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.14.0"
dependencies = [\
  "torch>=2.11.0",\
  "torchvision>=0.26.0",\
]

[tool.uv.sources]
torch = [\
    { index = "pytorch-cpu" },\
]
torchvision = [\
    { index = "pytorch-cpu" },\
]

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true
```

## [Configuring accelerators with environment markers](https://docs.astral.sh/uv/guides/integration/pytorch/\#configuring-accelerators-with-environment-markers)

In some cases, you may want to use CPU-only builds in one environment (e.g., macOS and Windows), and
CUDA-enabled builds in another (e.g., Linux).

With `tool.uv.sources`, you can use environment markers to specify the desired index for each
platform. For example, the following configuration would use PyTorch's CUDA-enabled builds on Linux,
and CPU-only builds on all other platforms (e.g., macOS and Windows):

```
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.14.0"
dependencies = [\
  "torch>=2.11.0",\
  "torchvision>=0.26.0",\
]

[tool.uv.sources]
torch = [\
  { index = "pytorch-cpu", marker = "sys_platform != 'linux'" },\
  { index = "pytorch-cu130", marker = "sys_platform == 'linux'" },\
]
torchvision = [\
  { index = "pytorch-cpu", marker = "sys_platform != 'linux'" },\
  { index = "pytorch-cu130", marker = "sys_platform == 'linux'" },\
]

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true

[[tool.uv.index]]
name = "pytorch-cu130"
url = "https://download.pytorch.org/whl/cu130"
explicit = true
```

Similarly, the following configuration would use PyTorch's AMD GPU builds on Linux, and CPU-only
builds on Windows and macOS (by way of falling back to PyPI):

```
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.14.0"
dependencies = [\
  "torch>=2.11.0",\
  "torchvision>=0.26.0",\
  "pytorch-triton-rocm>=3.5.1 ; sys_platform == 'linux'",\
  "triton-rocm>=3.6.0 ; sys_platform == 'linux'",\
]

[tool.uv.sources]
torch = [\
  { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },\
]
torchvision = [\
  { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },\
]
pytorch-triton-rocm = [\
  { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },\
]
triton-rocm = [\
  { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },\
]

[[tool.uv.index]]
name = "pytorch-rocm"
url = "https://download.pytorch.org/whl/rocm7.2"
explicit = true
```

Or, for Intel GPU builds:

```
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.14.0"
dependencies = [\
  "torch>=2.11.0",\
  "torchvision>=0.26.0",\
  "triton-xpu>=3.7.0 ; sys_platform == 'win32' or sys_platform == 'linux'",\
]

[tool.uv.sources]
torch = [\
  { index = "pytorch-xpu", marker = "sys_platform == 'win32' or sys_platform == 'linux'" },\
]
torchvision = [\
  { index = "pytorch-xpu", marker = "sys_platform == 'win32' or sys_platform == 'linux'" },\
]
triton-xpu = [\
  { index = "pytorch-xpu", marker = "sys_platform == 'win32' or sys_platform == 'linux'" },\
]

[[tool.uv.index]]
name = "pytorch-xpu"
url = "https://download.pytorch.org/whl/xpu"
explicit = true
```

## [Configuring accelerators with optional dependencies](https://docs.astral.sh/uv/guides/integration/pytorch/\#configuring-accelerators-with-optional-dependencies)

In some cases, you may want to use CPU-only builds in some cases, but CUDA-enabled builds in others,
with the choice toggled by a user-provided extra (e.g., `uv sync --extra cpu` vs.
`uv sync --extra cu130`).

With `tool.uv.sources`, you can use extra markers to specify the desired index for each enabled
extra. For example, the following configuration would use PyTorch's CPU-only builds for
`uv sync --extra cpu` and CUDA-enabled builds for `uv sync --extra cu130`:

```
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.14.0"
dependencies = []

[project.optional-dependencies]
cpu = [\
  "torch>=2.11.0",\
  "torchvision>=0.26.0",\
]
cu130 = [\
  "torch>=2.11.0",\
  "torchvision>=0.26.0",\
]

[tool.uv]
conflicts = [\
  [\
    { extra = "cpu" },\
    { extra = "cu130" },\
  ],\
]

[tool.uv.sources]
torch = [\
  { index = "pytorch-cpu", extra = "cpu" },\
  { index = "pytorch-cu130", extra = "cu130" },\
]
torchvision = [\
  { index = "pytorch-cpu", extra = "cpu" },\
  { index = "pytorch-cu130", extra = "cu130" },\
]

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true

[[tool.uv.index]]
name = "pytorch-cu130"
url = "https://download.pytorch.org/whl/cu130"
explicit = true
```

Note

Since GPU-accelerated builds aren't available on macOS, the above configuration will fail to install
on macOS when the `cu130` extra is enabled.

## [Installing GPU-enabled PyTorch extensions](https://docs.astral.sh/uv/guides/integration/pytorch/\#installing-gpu-enabled-pytorch-extensions)

Many packages in the PyTorch ecosystem include GPU-enabled extensions that are compiled for a
specific combination of CUDA and PyTorch versions. Building these packages from source often
requires access to the CUDA development toolkit and additional build configuration.

The [Astral GPU indexes](https://wheels.astral.sh/) provide pre-built wheels for packages like
`flash-attn`, `deepspeed`, `deep-gemm`, `torch-scatter`, and `vllm`, across a range of Python, CUDA,
and PyTorch versions.

To install `flash-attn` from the index for CUDA 12.8, run:

```
$ uv add flash-attn --index astral-cu128=https://wheels.astral.sh/simple/cu128/
```

The command adds `flash-attn` to the project dependencies, configures the Astral GPU index, and pins
`flash-attn` to that index.

As with the PyTorch indexes, set `explicit = true` to restrict the Astral GPU index to packages that
are explicitly pinned to it:

pyproject.toml

```
[tool.uv.sources]
flash-attn = { index = "astral-cu128" }

[[tool.uv.index]]
name = "astral-cu128"
url = "https://wheels.astral.sh/simple/cu128/"
explicit = true
```

Each Astral GPU index targets a specific CUDA version, and its wheels are built for specific PyTorch
versions. For example, a wheel with a `+cu.12.8.torch.2.11` local version is built for CUDA 12.8 and
PyTorch 2.11. Select the index and wheel that match your Python version, platform, CUDA version, and
PyTorch installation.

For the available packages, CUDA versions, and PyTorch versions, see the
[Astral GPU indexes](https://wheels.astral.sh/).

## [The `uv pip` interface](https://docs.astral.sh/uv/guides/integration/pytorch/\#the-uv-pip-interface)

While the above examples are focused on uv's project interface (`uv lock`, `uv sync`, `uv run`,
etc.), PyTorch can also be installed via the `uv pip` interface.

PyTorch itself offers a [dedicated interface](https://pytorch.org/get-started/locally/) to determine
the appropriate pip command to run for a given target configuration. For example, you can install
stable, CPU-only PyTorch on Linux with:

```
$ pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

To use the same workflow with uv, replace `pip3` with `uv pip`:

```
$ uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

## [Automatic backend selection](https://docs.astral.sh/uv/guides/integration/pytorch/\#automatic-backend-selection)

uv supports automatic selection of the appropriate PyTorch index via the `--torch-backend=auto`
command-line argument (or the `UV_TORCH_BACKEND=auto` environment variable), as in:

```
$ # With a command-line argument.
$ uv pip install torch --torch-backend=auto

$ # With an environment variable.
$ UV_TORCH_BACKEND=auto uv pip install torch
```

When enabled, uv will query for the installed CUDA driver, AMD GPU versions, and Intel GPU presence,
then use the most-compatible PyTorch index for all relevant packages (e.g., `torch`, `torchvision`,
etc.). If no such GPU is found, uv will fall back to the CPU-only index. uv will continue to respect
existing index configuration for any packages outside the PyTorch ecosystem.

You can also select a specific backend (e.g., CUDA 13.0) with `--torch-backend=cu130` (or
`UV_TORCH_BACKEND=cu130`):

```
$ # With a command-line argument.
$ uv pip install torch torchvision --torch-backend=cu130

$ # With an environment variable.
$ UV_TORCH_BACKEND=cu130 uv pip install torch torchvision
```

At present, `--torch-backend` is only available in the `uv pip` interface.

Back to top

---

[Skip to content](https://docs.astral.sh/uv/guides/integration/aws-lambda/#using-uv-with-aws-lambda)

# [Using uv with AWS Lambda](https://docs.astral.sh/uv/guides/integration/aws-lambda/\#using-uv-with-aws-lambda)

[AWS Lambda](https://aws.amazon.com/lambda/) is a serverless computing service that lets you run
code without provisioning or managing servers.

You can use uv with AWS Lambda to manage your Python dependencies, build your deployment package,
and deploy your Lambda functions.

Tip

Check out the [`uv-aws-lambda-example`](https://github.com/astral-sh/uv-aws-lambda-example) project for
an example of best practices when using uv to deploy an application to AWS Lambda.

## [Getting started](https://docs.astral.sh/uv/guides/integration/aws-lambda/\#getting-started)

To start, assume we have a minimal FastAPI application with the following structure:

```
project
├── pyproject.toml
└── app
    ├── __init__.py
    └── main.py
```

Where the `pyproject.toml` contains:

pyproject.toml

```
[project]
name = "uv-aws-lambda-example"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [\
    # FastAPI is a modern web framework for building APIs with Python.\
    "fastapi",\
    # Mangum is a library that adapts ASGI applications to AWS Lambda and API Gateway.\
    "mangum",\
]

[dependency-groups]
dev = [\
    # In development mode, include the FastAPI development server.\
    "fastapi[standard]>=0.115",\
]
```

And the `main.py` file contains:

app/main.py

```
import logging

from fastapi import FastAPI
from mangum import Mangum

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def root() -> str:
    return "Hello, world!"
```

We can run this application locally with:

```
$ uv run fastapi dev
```

From there, opening [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a web browser will display "Hello, world!"

## [Deploying a Docker image](https://docs.astral.sh/uv/guides/integration/aws-lambda/\#deploying-a-docker-image)

To deploy to AWS Lambda, we need to build a container image that includes the application code and
dependencies in a single output directory.

We'll follow the principles outlined in the [Docker guide](https://docs.astral.sh/uv/guides/integration/docker/) (in particular, a
multi-stage build) to ensure that the final image is as small and cache-friendly as possible.

In the first stage, we'll populate a single directory with all application code and dependencies. In
the second stage, we'll copy this directory over to the final image, omitting the build tools and
other unnecessary files.

Dockerfile

```
FROM ghcr.io/astral-sh/uv:0.13.4 AS uv

# First, bundle the dependencies into the task root.
FROM public.ecr.aws/lambda/python:3.13 AS builder

# Enable bytecode compilation, to improve cold-start performance.
ENV UV_COMPILE_BYTECODE=1

# Disable installer metadata, to create a deterministic layer.
ENV UV_NO_INSTALLER_METADATA=1

# Enable copy mode to support bind mount caching.
ENV UV_LINK_MODE=copy

# Bundle the dependencies into the Lambda task root via `uv pip install --target`.
#
# Omit any local packages (`--no-emit-workspace`) and development dependencies (`--no-dev`).
# This keeps the layer cached across changes to the application code or `pyproject.toml`, as long as
# `uv.lock` is unchanged.
RUN --mount=from=uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv export --frozen --no-emit-workspace --no-dev --no-editable -o requirements.txt && \
    uv pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

FROM public.ecr.aws/lambda/python:3.13

# Copy the runtime dependencies from the builder stage.
COPY --from=builder ${LAMBDA_TASK_ROOT} ${LAMBDA_TASK_ROOT}

# Copy the application code.
COPY ./app ${LAMBDA_TASK_ROOT}/app

# Set the AWS Lambda handler.
CMD ["app.main.handler"]
```

Tip

To deploy to ARM-based AWS Lambda runtimes, replace `public.ecr.aws/lambda/python:3.13` with `public.ecr.aws/lambda/python:3.13-arm64`.

We can build the image with, e.g.:

```
$ uv lock
$ docker build -t fastapi-app .
```

The core benefits of this Dockerfile structure are as follows:

1. **Minimal image size.** By using a multi-stage build, we can ensure that the final image only
    includes the application code and dependencies. For example, the uv binary itself is not included
    in the final image.
2. **Maximal cache reuse.** By installing application dependencies separately from the application
    code, we can ensure that the Docker layer cache is only invalidated when the dependencies change.

Concretely, rebuilding the image after modifying the application source code can reuse the cached
layers, resulting in millisecond builds:

```
 => [internal] load build definition from Dockerfile                                                                 0.0s
 => => transferring dockerfile: 1.31kB                                                                               0.0s
 => [internal] load metadata for public.ecr.aws/lambda/python:3.13                                                   0.3s
 => [internal] load metadata for ghcr.io/astral-sh/uv:latest                                                         0.3s
 => [internal] load .dockerignore                                                                                    0.0s
 => => transferring context: 106B                                                                                    0.0s
 => [uv 1/1] FROM ghcr.io/astral-sh/uv:latest@sha256:ea61e006cfec0e8d81fae901ad703e09d2c6cf1aa58abcb6507d124b50286f  0.0s
 => [builder 1/2] FROM public.ecr.aws/lambda/python:3.13@sha256:f5b51b377b80bd303fe8055084e2763336ea8920d12955b23ef  0.0s
 => [internal] load build context                                                                                    0.0s
 => => transferring context: 185B                                                                                    0.0s
 => CACHED [builder 2/2] RUN --mount=from=uv,source=/uv,target=/bin/uv     --mount=type=cache,target=/root/.cache/u  0.0s
 => CACHED [stage-2 2/3] COPY --from=builder /var/task /var/task                                                     0.0s
 => CACHED [stage-2 3/3] COPY ./app /var/task                                                                        0.0s
 => exporting to image                                                                                               0.0s
 => => exporting layers                                                                                              0.0s
 => => writing image sha256:6f8f9ef715a7cda466b677a9df4046ebbb90c8e88595242ade3b4771f547652d                         0.0
```

After building, we can push the image to
[Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) with, e.g.:

```
$ aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
$ docker tag fastapi-app:latest aws_account_id.dkr.ecr.region.amazonaws.com/fastapi-app:latest
$ docker push aws_account_id.dkr.ecr.region.amazonaws.com/fastapi-app:latest
```

Finally, we can deploy the image to AWS Lambda using the AWS Management Console or the AWS CLI,
e.g.:

```
$ aws lambda create-function \
   --function-name myFunction \
   --package-type Image \
   --code ImageUri=aws_account_id.dkr.ecr.region.amazonaws.com/fastapi-app:latest \
   --role arn:aws:iam::111122223333:role/my-lambda-role
```

Where the
[execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html#permissions-executionrole-api)
is created via:

```
$ aws iam create-role \
   --role-name my-lambda-role \
   --assume-role-policy-document '{"Version": "2012-10-17", "Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
```

Or, update an existing function with:

```
$ aws lambda update-function-code \
   --function-name myFunction \
   --image-uri aws_account_id.dkr.ecr.region.amazonaws.com/fastapi-app:latest \
   --publish
```

To test the Lambda, we can invoke it via the AWS Management Console or the AWS CLI, e.g.:

```
$ aws lambda invoke \
   --function-name myFunction \
   --payload file://event.json \
   --cli-binary-format raw-in-base64-out \
   response.json
{
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST"
}
```

Where `event.json` contains the event payload to pass to the Lambda function:

event.json

```
{
  "httpMethod": "GET",
  "path": "/",
  "requestContext": {},
  "version": "1.0"
}
```

And `response.json` contains the response from the Lambda function:

response.json

```
{
  "statusCode": 200,
  "headers": {
    "content-length": "14",
    "content-type": "application/json"
  },
  "multiValueHeaders": {},
  "body": "\"Hello, world!\"",
  "isBase64Encoded": false
}
```

For details, see the
[AWS Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html).

### [Workspace support](https://docs.astral.sh/uv/guides/integration/aws-lambda/\#workspace-support)

If a project includes local dependencies (e.g., via
[Workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/)), those too must be included in the deployment
package.

We'll start by extending the above example to include a dependency on a locally-developed library
named `library`.

First, we'll create the library itself:

```
$ uv init --lib library
$ uv add ./library
```

Running `uv init` within the `project` directory will automatically convert `project` to a workspace
and add `library` as a workspace member:

pyproject.toml

```
[project]
name = "uv-aws-lambda-example"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [\
    # FastAPI is a modern web framework for building APIs with Python.\
    "fastapi",\
    # A local library.\
    "library",\
    # Mangum is a library that adapts ASGI applications to AWS Lambda and API Gateway.\
    "mangum",\
]

[dependency-groups]
dev = [\
    # In development mode, include the FastAPI development server.\
    "fastapi[standard]",\
]

[tool.uv.workspace]
members = ["library"]

[tool.uv.sources]
lib = { workspace = true }
```

By default, `uv init --lib` will create a package that exports a `hello` function. We'll modify the
application source code to call that function:

app/main.py

```
import logging

from fastapi import FastAPI
from mangum import Mangum

from library import hello

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def root() -> str:
    return hello()
```

We can run the modified application locally with:

```
$ uv run fastapi dev
```

And confirm that opening [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a web browser displays, "Hello from library!"
(instead of "Hello, World!")

Finally, we'll update the Dockerfile to include the local library in the deployment package:

Dockerfile

```
FROM ghcr.io/astral-sh/uv:0.13.4 AS uv

# First, bundle the dependencies into the task root.
FROM public.ecr.aws/lambda/python:3.13 AS builder

# Enable bytecode compilation, to improve cold-start performance.
ENV UV_COMPILE_BYTECODE=1

# Disable installer metadata, to create a deterministic layer.
ENV UV_NO_INSTALLER_METADATA=1

# Enable copy mode to support bind mount caching.
ENV UV_LINK_MODE=copy

# Bundle the dependencies into the Lambda task root via `uv pip install --target`.
#
# Omit any local packages (`--no-emit-workspace`) and development dependencies (`--no-dev`).
# This keeps the layer cached across changes to the application code or `pyproject.toml`, as long as
# `uv.lock` is unchanged.
RUN --mount=from=uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv export --frozen --no-emit-workspace --no-dev --no-editable -o requirements.txt && \
    uv pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# If you have a workspace, copy it over and install it too.
#
# By omitting `--no-emit-workspace`, `library` will be copied into the task root. Using a separate
# `RUN` command ensures that all third-party dependencies are cached separately and remain
# robust to changes in the workspace.
RUN --mount=from=uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=library,target=library \
    uv export --frozen --no-dev --no-editable -o requirements.txt && \
    uv pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

FROM public.ecr.aws/lambda/python:3.13

# Copy the runtime dependencies from the builder stage.
COPY --from=builder ${LAMBDA_TASK_ROOT} ${LAMBDA_TASK_ROOT}

# Copy the application code.
COPY ./app ${LAMBDA_TASK_ROOT}/app

# Set the AWS Lambda handler.
CMD ["app.main.handler"]
```

Tip

To deploy to ARM-based AWS Lambda runtimes, replace `public.ecr.aws/lambda/python:3.13` with `public.ecr.aws/lambda/python:3.13-arm64`.

From there, we can build and deploy the updated image as before.

## [Deploying a zip archive](https://docs.astral.sh/uv/guides/integration/aws-lambda/\#deploying-a-zip-archive)

AWS Lambda also supports deployment via zip archives. For simple applications, zip archives can be a
more straightforward and efficient deployment method than Docker images; however, zip archives are
limited to
[250 MB](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html#python-package-create-update)
in size.

Returning to the FastAPI example, we can bundle the application dependencies into a local directory
for AWS Lambda via:

```
$ uv export --frozen --no-dev --no-editable -o requirements.txt
$ uv pip install \
   --no-installer-metadata \
   --no-compile-bytecode \
   --python-platform x86_64-manylinux2014 \
   --python 3.13 \
   --target packages \
   -r requirements.txt
```

Tip

To deploy to ARM-based AWS Lambda runtimes, replace `x86_64-manylinux2014` with `aarch64-manylinux2014`.

Following the
[AWS Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html), we can
then bundle these dependencies into a zip as follows:

```
$ cd packages
$ zip -r ../package.zip .
$ cd ..
```

Finally, we can add the application code to the zip archive:

```
$ zip -r package.zip app
```

We can then deploy the zip archive to AWS Lambda via the AWS Management Console or the AWS CLI,
e.g.:

```
$ aws lambda create-function \
   --function-name myFunction \
   --runtime python3.13 \
   --zip-file fileb://package.zip \
   --handler app.main.handler \
   --role arn:aws:iam::111122223333:role/service-role/my-lambda-role
```

Where the
[execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html#permissions-executionrole-api)
is created via:

```
$ aws iam create-role \
   --role-name my-lambda-role \
   --assume-role-policy-document '{"Version": "2012-10-17", "Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
```

Or, update an existing function with:

```
$ aws lambda update-function-code \
   --function-name myFunction \
   --zip-file fileb://package.zip
```

Note

By default, the AWS Management Console assumes a Lambda entrypoint of `lambda_function.lambda_handler`.
If your application uses a different entrypoint, you'll need to modify it in the AWS Management Console.
For example, the above FastAPI application uses `app.main.handler`.

To test the Lambda, we can invoke it via the AWS Management Console or the AWS CLI, e.g.:

```
$ aws lambda invoke \
   --function-name myFunction \
   --payload file://event.json \
   --cli-binary-format raw-in-base64-out \
   response.json
{
  "StatusCode": 200,
  "ExecutedVersion": "$LATEST"
}
```

Where `event.json` contains the event payload to pass to the Lambda function:

event.json

```
{
  "httpMethod": "GET",
  "path": "/",
  "requestContext": {},
  "version": "1.0"
}
```

And `response.json` contains the response from the Lambda function:

response.json

```
{
  "statusCode": 200,
  "headers": {
    "content-length": "14",
    "content-type": "application/json"
  },
  "multiValueHeaders": {},
  "body": "\"Hello, world!\"",
  "isBase64Encoded": false
}
```

### [Using a Lambda layer](https://docs.astral.sh/uv/guides/integration/aws-lambda/\#using-a-lambda-layer)

AWS Lambda also supports the deployment of multiple composed
[Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/python-layers.html) when working with
zip archives. These layers are conceptually similar to layers in a Docker image, allowing you to
separate application code from dependencies.

In particular, we can create a lambda layer for application dependencies and attach it to the Lambda
function, separate from the application code itself. This setup can improve cold-start performance
for application updates, as the dependencies layer can be reused across deployments.

To create a Lambda layer, we'll follow similar steps, but create two separate zip archives: one for
the application code and one for the application dependencies.

First, we'll create the dependency layer. Lambda layers are expected to follow a slightly different
structure, so we'll use `--prefix` rather than `--target`:

```
$ uv export --frozen --no-dev --no-editable -o requirements.txt
$ uv pip install \
   --no-installer-metadata \
   --no-compile-bytecode \
   --python-platform x86_64-manylinux2014 \
   --python 3.13 \
   --prefix packages \
   -r requirements.txt
```

We'll then zip the dependencies in adherence with the expected layout for Lambda layers:

```
$ mkdir python
$ cp -r packages/lib python/
$ zip -r layer_content.zip python
```

Tip

To generate deterministic zip archives, consider passing the `-X` flag to `zip` to exclude
extended attributes and file system metadata.

And publish the Lambda layer:

```
$ aws lambda publish-layer-version --layer-name dependencies-layer \
   --zip-file fileb://layer_content.zip \
   --compatible-runtimes python3.13 \
   --compatible-architectures "x86_64"
```

We can then create the Lambda function as in the previous example, omitting the dependencies:

```
$ # Zip the application code.
$ zip -r app.zip app

$ # Create the Lambda function.
$ aws lambda create-function \
   --function-name myFunction \
   --runtime python3.13 \
   --zip-file fileb://app.zip \
   --handler app.main.handler \
   --role arn:aws:iam::111122223333:role/service-role/my-lambda-role
```

Finally, we can attach the dependencies layer to the Lambda function, using the ARN returned by the
`publish-layer-version` step:

```
$ aws lambda update-function-configuration --function-name myFunction \
    --cli-binary-format raw-in-base64-out \
    --layers "arn:aws:lambda:region:111122223333:layer:dependencies-layer:1"
```

When the application dependencies change, the layer can be updated independently of the application
by republishing the layer and updating the Lambda function configuration:

```
$ # Update the dependencies in the layer.
$ aws lambda publish-layer-version --layer-name dependencies-layer \
   --zip-file fileb://layer_content.zip \
   --compatible-runtimes python3.13 \
   --compatible-architectures "x86_64"

$ # Update the Lambda function configuration.
$ aws lambda update-function-configuration --function-name myFunction \
    --cli-binary-format raw-in-base64-out \
    --layers "arn:aws:lambda:region:111122223333:layer:dependencies-layer:2"
```

Back to top

---

