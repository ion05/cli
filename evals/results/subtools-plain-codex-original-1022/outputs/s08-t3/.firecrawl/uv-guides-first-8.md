Source: https://docs.astral.sh/uv/guides/install-python/

[Skip to content](https://docs.astral.sh/uv/guides/install-python/#installing-python)

# [Installing Python](https://docs.astral.sh/uv/guides/install-python/\#installing-python)

If Python is already installed on your system, uv will
[detect and use](https://docs.astral.sh/uv/guides/install-python/#using-existing-python-versions) it without configuration. However, uv can also
install and manage Python versions. uv [automatically installs](https://docs.astral.sh/uv/guides/install-python/#automatic-python-downloads) missing
Python versions as needed — you don't need to install Python to get started.

## [Getting started](https://docs.astral.sh/uv/guides/install-python/\#getting-started)

To install the latest Python version:

```
$ uv python install
```

Note

Python does not publish official distributable binaries. As such, uv uses distributions from the Astral [`python-build-standalone`](https://github.com/astral-sh/python-build-standalone) project. See the [Python distributions](https://docs.astral.sh/uv/concepts/python-versions/#managed-python-distributions) documentation for more details.

Once Python is installed, it will be used by `uv` commands automatically. uv also adds the installed
version to your `PATH`:

```
$ python3.15
```

uv only installs a _versioned_ executable by default. To install `python` and `python3` executables,
include the experimental `--default` option:

```
$ uv python install --default
```

Tip

See the documentation on [installing Python executables](https://docs.astral.sh/uv/concepts/python-versions/#installing-python-executables)
for more details.

## [Installing a specific version](https://docs.astral.sh/uv/guides/install-python/\#installing-a-specific-version)

To install a specific Python version:

```
$ uv python install 3.12
```

To install multiple Python versions:

```
$ uv python install 3.11 3.12
```

To install an alternative Python implementation, e.g., PyPy:

```
$ uv python install pypy@3.10
```

See the [`python install`](https://docs.astral.sh/uv/concepts/python-versions/#installing-a-python-version) documentation
for more details.

## [Reinstalling Python](https://docs.astral.sh/uv/guides/install-python/\#reinstalling-python)

To reinstall uv-managed Python versions, use `--reinstall`, e.g.:

```
$ uv python install --reinstall
```

This will reinstall all previously installed Python versions. Improvements are constantly being
added to the Python distributions, so reinstalling may resolve bugs even if the Python version does
not change.

## [Viewing Python installations](https://docs.astral.sh/uv/guides/install-python/\#viewing-python-installations)

To view available and installed Python versions:

```
$ uv python list
```

See the [`python list`](https://docs.astral.sh/uv/concepts/python-versions/#viewing-available-python-versions)
documentation for more details.

## [Automatic Python downloads](https://docs.astral.sh/uv/guides/install-python/\#automatic-python-downloads)

Python does not need to be explicitly installed to use uv. By default, uv will automatically
download Python versions when they are required. For example, the following would download Python
3.12 if it was not installed:

```
$ uvx python@3.12 -c "print('hello world')"
```

Even if a specific Python version is not requested, uv will download the latest version on demand.
For example, if there are no Python versions on your system, the following will install Python
before creating a new virtual environment:

```
$ uv venv
```

Tip

Automatic Python downloads can be [easily disabled](https://docs.astral.sh/uv/concepts/python-versions/#disabling-automatic-python-downloads) if you want more control over when Python is downloaded.

## [Using existing Python versions](https://docs.astral.sh/uv/guides/install-python/\#using-existing-python-versions)

uv will use existing Python installations if present on your system. There is no configuration
necessary for this behavior: uv will use the system Python if it satisfies the requirements of the
command invocation. See the
[Python discovery](https://docs.astral.sh/uv/concepts/python-versions/#discovery-of-python-versions) documentation for
details.

To force uv to use the system Python, provide the `--no-managed-python` flag. See the
[Python version preference](https://docs.astral.sh/uv/concepts/python-versions/#requiring-or-disabling-managed-python-versions)
documentation for more details.

## [Upgrading Python versions](https://docs.astral.sh/uv/guides/install-python/\#upgrading-python-versions)

To upgrade a Python version to the latest supported patch release:

```
$ uv python upgrade 3.12
```

To upgrade all uv-managed Python versions:

```
$ uv python upgrade
```

See the [`python upgrade`](https://docs.astral.sh/uv/concepts/python-versions/#upgrading-python-versions) documentation
for more details.

## [Next steps](https://docs.astral.sh/uv/guides/install-python/\#next-steps)

To learn more about `uv python`, see the [Python version concept](https://docs.astral.sh/uv/concepts/python-versions/)
page and the [command reference](https://docs.astral.sh/uv/reference/cli/#uv-python).

Or, read on to learn how to [run scripts](https://docs.astral.sh/uv/guides/scripts/) and invoke Python with uv.

Back to top

---

Source: https://docs.astral.sh/uv/guides/scripts/

[Skip to content](https://docs.astral.sh/uv/guides/scripts/#running-scripts)

# [Running scripts](https://docs.astral.sh/uv/guides/scripts/\#running-scripts)

A Python script is a file intended for standalone execution, e.g., with `python <script>.py`. Using
uv to execute scripts ensures that script dependencies are managed without manually managing
environments.

Note

If you are not familiar with Python environments: every Python installation has an environment
that packages can be installed in. Typically, creating [_virtual_ environments](https://docs.python.org/3/library/venv.html) is recommended to
isolate packages required by each script. uv automatically manages virtual environments for you
and prefers a [declarative](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies) approach to dependencies.

## [Running a script without dependencies](https://docs.astral.sh/uv/guides/scripts/\#running-a-script-without-dependencies)

If your script has no dependencies, you can execute it with `uv run`:

example.py

```
print("Hello world")
```

```
$ uv run example.py
Hello world
```

Similarly, if your script depends on a module in the standard library, there's nothing more to do:

example.py

```
import os

print(os.path.expanduser("~"))
```

```
$ uv run example.py
/Users/astral
```

Arguments may be provided to the script:

example.py

```
import sys

print(" ".join(sys.argv[1:]))
```

```
$ uv run example.py test
test

$ uv run example.py hello world!
hello world!
```

Additionally, your script can be read directly from stdin:

```
$ echo 'print("hello world!")' | uv run -
```

Or, if your shell supports [here-documents](https://en.wikipedia.org/wiki/Here_document):

```
uv run - <<EOF
print("hello world!")
EOF
```

Note that if you use `uv run` in a _project_, i.e., a directory with a `pyproject.toml`, it will
install the current project before running the script. If your script does not depend on the
project, use the `--no-project` flag to skip this:

```
$ # Note: the `--no-project` flag must be provided _before_ the script name.
$ uv run --no-project example.py
```

See the [projects guide](https://docs.astral.sh/uv/guides/projects/) for more details on working in projects.

## [Running a script with dependencies](https://docs.astral.sh/uv/guides/scripts/\#running-a-script-with-dependencies)

When your script requires other packages, they must be installed into the environment that the
script runs in. uv prefers to create these environments on-demand instead of using a long-lived
virtual environment with manually managed dependencies. This requires explicit declaration of
dependencies that are required for the script. Generally, it's recommended to use a
[project](https://docs.astral.sh/uv/guides/projects/) or [inline metadata](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies) to declare
dependencies, but uv supports requesting dependencies per invocation as well.

For example, the following script requires `rich`.

example.py

```
import time
from rich.progress import track

for i in track(range(20), description="For example:"):
    time.sleep(0.05)
```

If executed without specifying a dependency, this script will fail:

```
$ uv run --no-project example.py
Traceback (most recent call last):
  File "/Users/astral/example.py", line 2, in <module>
    from rich.progress import track
ModuleNotFoundError: No module named 'rich'
```

Request the dependency using the `--with` option:

```
$ uv run --with rich example.py
For example: ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:01
```

Constraints can be added to the requested dependency if specific versions are needed:

```
$ uv run --with 'rich>12,<13' example.py
```

Multiple dependencies can be requested by repeating the `--with` option.

Note that if `uv run` is used in a _project_, these dependencies will be included _in addition_ to
the project's dependencies. To opt-out of this behavior, use the `--no-project` flag.

## [Creating a Python script](https://docs.astral.sh/uv/guides/scripts/\#creating-a-python-script)

Python recently added a standard format for
[inline script metadata](https://packaging.python.org/en/latest/specifications/inline-script-metadata/#inline-script-metadata).
It allows for selecting Python versions and defining dependencies. Use `uv init --script` to
initialize scripts with the inline metadata:

```
$ uv init --script example.py --python 3.12
```

## [Declaring script dependencies](https://docs.astral.sh/uv/guides/scripts/\#declaring-script-dependencies)

The inline metadata format allows the dependencies for a script to be declared in the script itself.

uv supports adding and updating inline script metadata for you. Use `uv add --script` to declare the
dependencies for the script:

```
$ uv add --script example.py 'requests<3' 'rich'
```

This will add a `script` section at the top of the script declaring the dependencies using TOML:

example.py

```
# /// script
# dependencies = [\
#   "requests<3",\
#   "rich",\
# ]
# ///

import requests
from rich.pretty import pprint

resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
```

uv will automatically create an environment with the dependencies necessary to run the script, e.g.:

```
$ uv run example.py
[\
│   ('1', 'PEP Purpose and Guidelines'),\
│   ('2', 'Procedure for Adding New Modules'),\
│   ('3', 'Guidelines for Handling Bug Reports'),\
│   ('4', 'Deprecation of Standard Modules'),\
│   ('5', 'Guidelines for Language Evolution'),\
│   ('6', 'Bug Fix Releases'),\
│   ('7', 'Style Guide for C Code'),\
│   ('8', 'Style Guide for Python Code'),\
│   ('9', 'Sample Plaintext PEP Template'),\
│   ('10', 'Voting Guidelines')\
]
```

Important

When using inline script metadata, even if `uv run` is [used in a _project_](https://docs.astral.sh/uv/concepts/projects/run/), the project's dependencies will be ignored. The `--no-project` flag is not required.

uv also respects Python version requirements:

example.py

```
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

# Use some syntax added in Python 3.12
type Point = tuple[float, float]
print(Point)
```

Note

The `dependencies` field must be provided even if empty.

`uv run` will search for and use the required Python version. The Python version will download if it
is not installed — see the documentation on [Python versions](https://docs.astral.sh/uv/concepts/python-versions/) for
more details.

## [Using a shebang to create an executable file](https://docs.astral.sh/uv/guides/scripts/\#using-a-shebang-to-create-an-executable-file)

A shebang can be added to make a script executable without using `uv run` — this makes it easy to
run scripts that are on your `PATH` or in the current folder.

For example, create a file called `greet` with the following contents:

greet

```
#!/usr/bin/env -S uv run --script

print("Hello, world!")
```

Ensure that your script is executable, e.g., with `chmod +x greet`, then run the script:

```
$ ./greet
Hello, world!
```

Declaration of dependencies is also supported in this context, for example:

example

```
#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx"]
# ///

import httpx

print(httpx.get("https://example.com"))
```

## [Using alternative package indexes](https://docs.astral.sh/uv/guides/scripts/\#using-alternative-package-indexes)

If you wish to use an alternative [package index](https://docs.astral.sh/uv/concepts/indexes/) to resolve dependencies,
you can provide the index with the `--index` option:

```
$ uv add --index "https://example.com/simple" --script example.py 'requests<3' 'rich'
```

This will include the package data in the inline metadata:

```
# [[tool.uv.index]]
# url = "https://example.com/simple"
```

If you require authentication to access the package index, then please refer to the
[package index](https://docs.astral.sh/uv/concepts/indexes/) documentation.

## [Locking dependencies](https://docs.astral.sh/uv/guides/scripts/\#locking-dependencies)

uv supports locking dependencies for PEP 723 scripts using the `uv.lock` file format. Unlike with
projects, scripts must be explicitly locked using `uv lock`:

```
$ uv lock --script example.py
```

Running `uv lock --script` will create a `.lock` file adjacent to the script (e.g.,
`example.py.lock`).

Once locked, subsequent operations like `uv run --script`, `uv add --script`, `uv export --script`,
and `uv tree --script` will reuse the locked dependencies, updating the lockfile if necessary.

If no such lockfile is present, commands like `uv export --script` will still function as expected,
but will not create a lockfile.

## [Improving reproducibility](https://docs.astral.sh/uv/guides/scripts/\#improving-reproducibility)

In addition to locking dependencies, uv supports an `exclude-newer` field in the `tool.uv` section
of inline script metadata to limit uv to only considering distributions released before a specific
date. This is useful for improving the reproducibility of your script when run at a later point in
time.

The date should be specified as an [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html) timestamp
(e.g., `2006-12-02T02:07:43Z`).

example.py

```
# /// script
# dependencies = [\
#   "requests",\
# ]
# [tool.uv]
# exclude-newer = "2023-10-16T00:00:00Z"
# ///

import requests

print(requests.__version__)
```

## [Using different Python versions](https://docs.astral.sh/uv/guides/scripts/\#using-different-python-versions)

uv allows arbitrary Python versions to be requested on each script invocation, for example:

example.py

```
import sys

print(".".join(map(str, sys.version_info[:3])))
```

```
$ # Use the default Python version, may differ on your machine
$ uv run example.py
3.12.6
```

```
$ # Use a specific Python version
$ uv run --python 3.10 example.py
3.10.15
```

See the [Python version request](https://docs.astral.sh/uv/concepts/python-versions/#requesting-a-version) documentation
for more details on requesting Python versions.

## [Using GUI scripts](https://docs.astral.sh/uv/guides/scripts/\#using-gui-scripts)

On Windows `uv` will run your script ending with `.pyw` extension using `pythonw`:

example.pyw

```
from tkinter import Tk, ttk

root = Tk()
root.title("uv")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World").grid(column=0, row=0)
root.mainloop()
```

```
PS> uv run example.pyw
```

![Run Result](https://docs.astral.sh/uv/assets/uv_gui_script_hello_world.png)

Similarly, it works with dependencies as well:

example\_pyqt.pyw

```
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout

app = QApplication(sys.argv)
widget = QWidget()
grid = QGridLayout()

text_label = QLabel()
text_label.setText("Hello World!")
grid.addWidget(text_label)

widget.setLayout(grid)
widget.setGeometry(100, 100, 200, 50)
widget.setWindowTitle("uv")
widget.show()
sys.exit(app.exec_())
```

```
PS> uv run --with PyQt5 example_pyqt.pyw
```

![Run Result](https://docs.astral.sh/uv/assets/uv_gui_script_hello_world_pyqt.png)

## [Next steps](https://docs.astral.sh/uv/guides/scripts/\#next-steps)

To learn more about `uv run`, see the [command reference](https://docs.astral.sh/uv/reference/cli/#uv-run).

Or, read on to learn how to [run and install tools](https://docs.astral.sh/uv/guides/tools/) with uv.

Back to top

---

Source: https://docs.astral.sh/uv/guides/tools/

[Skip to content](https://docs.astral.sh/uv/guides/tools/#using-tools)

# [Using tools](https://docs.astral.sh/uv/guides/tools/\#using-tools)

Many Python packages provide applications that can be used as tools. uv has specialized support for
easily invoking and installing tools.

## [Running tools](https://docs.astral.sh/uv/guides/tools/\#running-tools)

The `uvx` command invokes a tool without installing it.

For example, to run `ruff`:

```
$ uvx ruff
```

Note

This is exactly equivalent to:

```
$ uv tool run ruff
```

`uvx` is provided as an alias for convenience.

Arguments can be provided after the tool name:

```
$ uvx pycowsay hello from uv

  -------------
< hello from uv >
  -------------
   \   ^__^
    \  (oo)\_______
       (__)\       )\/\
           ||----w |
           ||     ||
```

Tools are installed into temporary, isolated environments when using `uvx`.

Note

If you are running a tool in a [_project_](https://docs.astral.sh/uv/concepts/projects/) and the tool requires that
your project is installed, e.g., when using `pytest` or `mypy`, you'll want to use
[`uv run`](https://docs.astral.sh/uv/guides/projects/#running-commands) instead of `uvx`. Otherwise, the tool will be run in
a virtual environment that is isolated from your project.

If your project has a flat structure, e.g., instead of using a `src` directory for modules,
the project itself does not need to be installed and `uvx` is fine. In this case, using
`uv run` is only beneficial if you want to pin the version of the tool in the project's
dependencies.

## [Commands with different package names](https://docs.astral.sh/uv/guides/tools/\#commands-with-different-package-names)

When `uvx ruff` is invoked, uv installs the `ruff` package which provides the `ruff` command.
However, sometimes the package and command names differ.

The `--from` option can be used to invoke a command from a specific package, e.g., `http` which is
provided by `httpie`:

```
$ uvx --from httpie http
```

## [Requesting specific versions](https://docs.astral.sh/uv/guides/tools/\#requesting-specific-versions)

To run a tool at a specific version, use `command@<version>`:

```
$ uvx ruff@0.3.0 check
```

To run a tool at the latest version, use `command@latest`:

```
$ uvx ruff@latest check
```

The `--from` option can also be used to specify package versions, as above:

```
$ uvx --from 'ruff==0.3.0' ruff check
```

Or, to constrain to a range of versions:

```
$ uvx --from 'ruff>0.2.0,<0.3.0' ruff check
```

Note the `@` syntax cannot be used for anything other than an exact version.

## [Requesting extras](https://docs.astral.sh/uv/guides/tools/\#requesting-extras)

The `--from` option can be used to run a tool with extras:

```
$ uvx --from 'mypy[faster-cache,reports]' mypy --xml-report mypy_report
```

This can also be combined with version selection:

```
$ uvx --from 'mypy[faster-cache,reports]==1.13.0' mypy --xml-report mypy_report
```

## [Requesting different sources](https://docs.astral.sh/uv/guides/tools/\#requesting-different-sources)

The `--from` option can also be used to install from alternative sources.

For example, to pull from git:

```
$ uvx --from git+https://github.com/httpie/cli httpie
```

You can also pull the latest commit from a specific named branch:

```
$ uvx --from git+https://github.com/httpie/cli@master httpie
```

Or pull a specific tag:

```
$ uvx --from git+https://github.com/httpie/cli@3.2.4 httpie
```

Or even a specific commit:

```
$ uvx --from git+https://github.com/httpie/cli@2843b87 httpie
```

Or with [Git LFS](https://git-lfs.com/) support:

```
$ uvx --lfs --from git+https://github.com/astral-sh/lfs-cowsay lfs-cowsay
```

## [Commands with plugins](https://docs.astral.sh/uv/guides/tools/\#commands-with-plugins)

Additional dependencies can be included, e.g., to include `mkdocs-material` when running `mkdocs`:

```
$ uvx --with mkdocs-material mkdocs --help
```

## [Installing tools](https://docs.astral.sh/uv/guides/tools/\#installing-tools)

If a tool is used often, it is useful to install it to a persistent environment and add it to the
`PATH` instead of invoking `uvx` repeatedly.

Tip

`uvx` is a convenient alias for `uv tool run`. All of the other commands for interacting with
tools require the full `uv tool` prefix.

To install `ruff`:

```
$ uv tool install ruff
```

When a tool is installed, its executables are placed in a `bin` directory in the `PATH` which allows
the tool to be run without uv. If it's not on the `PATH`, a warning will be displayed and
`uv tool update-shell` can be used to add it to the `PATH`.

After installing `ruff`, it should be available:

```
$ ruff --version
```

Unlike `uv pip install`, installing a tool does not make its modules available in the current
environment. For example, the following command will fail:

```
$ python -c "import ruff"
```

This isolation is important for reducing interactions and conflicts between dependencies of tools,
scripts, and projects.

Unlike `uvx`, `uv tool install` operates on a _package_ and will install all executables provided by
the tool.

For example, the following will install the `http`, `https`, and `httpie` executables:

```
$ uv tool install httpie
```

Additionally, package versions can be included without `--from`:

```
$ uv tool install 'httpie>0.1.0'
```

And, similarly, for package sources:

```
$ uv tool install git+https://github.com/httpie/cli
```

Or package sources with [Git LFS](https://git-lfs.com/):

```
$ uv tool install --lfs git+https://github.com/astral-sh/lfs-cowsay
```

As with `uvx`, installations can include additional packages:

```
$ uv tool install mkdocs --with mkdocs-material
```

Multiple related executables can be installed together in the same tool environment, using the
`--with-executables-from` flag. For example, the following will install the executables from
`ansible`, plus those provided by `ansible-core` and `ansible-lint`:

```
$ uv tool install --with-executables-from ansible-core,ansible-lint ansible
```

## [Upgrading tools](https://docs.astral.sh/uv/guides/tools/\#upgrading-tools)

To upgrade a tool, use `uv tool upgrade`:

```
$ uv tool upgrade ruff
```

Tool upgrades will respect the version constraints provided when installing the tool. For example,
`uv tool install ruff >=0.3,<0.4` followed by `uv tool upgrade ruff` will upgrade Ruff to the latest
version in the range `>=0.3,<0.4`.

To instead replace the version constraints, re-install the tool with `uv tool install`:

```
$ uv tool install ruff>=0.4
```

To instead upgrade all tools:

```
$ uv tool upgrade --all
```

## [Requesting Python versions](https://docs.astral.sh/uv/guides/tools/\#requesting-python-versions)

By default, uv will use your default Python interpreter (the first it finds) when running,
installing, or upgrading tools. You can specify the Python interpreter to use with the `--python`
option.

For example, to request a specific Python version when running a tool:

```
$ uvx --python 3.10 ruff
```

Or, when installing a tool:

```
$ uv tool install --python 3.10 ruff
```

Or, when upgrading a tool:

```
$ uv tool upgrade --python 3.10 ruff
```

For more details on requesting Python versions, see the
[Python version](https://docs.astral.sh/uv/concepts/python-versions/#requesting-a-version) concept page.

## [Legacy Windows Scripts](https://docs.astral.sh/uv/guides/tools/\#legacy-windows-scripts)

Tools also support running
[legacy setuptools scripts](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#scripts).
These scripts are available via `$(uv tool dir)\<tool-name>\Scripts` when installed.

Currently only legacy scripts with the `.ps1`, `.cmd`, and `.bat` extensions are supported.

For example, to run a Command Prompt script:

```
$ uv tool run --from nuitka==2.6.7 nuitka.cmd --version
```

In addition, you don't need to specify the extension. `uvx` will automatically look for files ending
in `.ps1`, `.cmd`, and `.bat` in that order of execution on your behalf.

```
$ uv tool run --from nuitka==2.6.7 nuitka --version
```

## [Next steps](https://docs.astral.sh/uv/guides/tools/\#next-steps)

To learn more about managing tools with uv, see the [Tools concept](https://docs.astral.sh/uv/concepts/tools/) page and
the [command reference](https://docs.astral.sh/uv/reference/cli/#uv-tool).

Or, read on to learn how to [work on projects](https://docs.astral.sh/uv/guides/projects/).

Back to top

---

Source: https://docs.astral.sh/uv/guides/projects/

[Skip to content](https://docs.astral.sh/uv/guides/projects/#working-on-projects)

# [Working on projects](https://docs.astral.sh/uv/guides/projects/\#working-on-projects)

uv supports managing Python projects, which define their dependencies in a `pyproject.toml` file.

## [Creating a new project](https://docs.astral.sh/uv/guides/projects/\#creating-a-new-project)

You can create a new Python project using the `uv init` command:

```
$ uv init hello-world
$ cd hello-world
```

Alternatively, you can initialize a project in the working directory:

```
$ mkdir hello-world
$ cd hello-world
$ uv init
```

uv will create the following files and directories:

```
├── .git/
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── src
    └── hello_world
        └── __init__.py
```

The `pyproject.toml` defines a `hello-world` entrypoint referring to a simple "Hello world" program
in `__init__.py`. Try it out with `uv run`:

```
$ uv run hello-world
Hello from hello-world!
```

## [Project structure](https://docs.astral.sh/uv/guides/projects/\#project-structure)

A project consists of a few important parts that work together and allow uv to manage your project.
In addition to the files created by `uv init`, uv will create a virtual environment and `uv.lock`
file in the root of your project the first time you run a project command, i.e., `uv run`,
`uv sync`, or `uv lock`.

A complete listing would look like:

```
.
├── .git/
├── .venv/
│   ├── bin
│   ├── lib
│   └── pyvenv.cfg
├── .gitignore
├── .python-version
├── README.md
├── src
│   └── hello_world
│       └── __init__.py
├── pyproject.toml
└── uv.lock
```

### [`pyproject.toml`](https://docs.astral.sh/uv/guides/projects/\#pyprojecttoml)

The `pyproject.toml` contains metadata about your project:

pyproject.toml

```
[project]
name = "hello-world"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [\
  { name = "ferris", email = "ferris@example.org" }\
]
requires-python = ">=3.14"
dependencies = []

[project.scripts]
hello-world = "hello_world:main"

[build-system]
requires = ["uv_build>=0.13.4,<0.14"]
build-backend = "uv_build"
```

You'll use this file to specify dependencies, as well as details about the project such as its
description or license. You can edit this file manually, or use commands like `uv add` and
`uv remove` to manage your project from the terminal.

Tip

See the official [`pyproject.toml` guide](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
for more details on getting started with the `pyproject.toml` format.

You'll also use this file to specify uv [configuration options](https://docs.astral.sh/uv/concepts/configuration-files/)
in a [`[tool.uv]`](https://docs.astral.sh/uv/reference/settings/) section.

### [`.python-version`](https://docs.astral.sh/uv/guides/projects/\#python-version)

The `.python-version` file contains the project's default Python version. This file tells uv which
Python version to use when creating the project's virtual environment.

### [`.venv`](https://docs.astral.sh/uv/guides/projects/\#venv)

The `.venv` folder contains your project's virtual environment, a Python environment that is
isolated from the rest of your system. This is where uv will install your project's dependencies.

See the [project environment](https://docs.astral.sh/uv/concepts/projects/layout/#the-project-environment) documentation
for more details.

### [`uv.lock`](https://docs.astral.sh/uv/guides/projects/\#uvlock)

`uv.lock` is a cross-platform lockfile that contains exact information about your project's
dependencies. Unlike the `pyproject.toml` which is used to specify the broad requirements of your
project, the lockfile contains the exact resolved versions that are installed in the project
environment. This file should be checked into version control, allowing for consistent and
reproducible installations across machines.

`uv.lock` is a human-readable TOML file but is managed by uv and should not be edited manually.

See the [lockfile](https://docs.astral.sh/uv/concepts/projects/layout/#the-lockfile) documentation for more details.

## [Managing dependencies](https://docs.astral.sh/uv/guides/projects/\#managing-dependencies)

You can add dependencies to your `pyproject.toml` with the `uv add` command. This will also update
the lockfile and project environment:

```
$ uv add requests
```

You can also specify version constraints or alternative sources:

```
$ # Specify a version constraint
$ uv add 'requests==2.31.0'

$ # Add a git dependency
$ uv add git+https://github.com/psf/requests
```

If you're migrating from a `requirements.txt` file, you can use `uv add` with the `-r` flag to add
all dependencies from the file:

```
$ # Add all dependencies from `requirements.txt`.
$ uv add -r requirements.txt -c constraints.txt
```

To remove a package, you can use `uv remove`:

```
$ uv remove requests
```

To upgrade a package, run `uv lock` with the `--upgrade-package` flag:

```
$ uv lock --upgrade-package requests
```

The `--upgrade-package` flag will attempt to update the specified package to the latest compatible
version, while keeping the rest of the lockfile intact.

See the documentation on [managing dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/) for more
details.

## [Viewing your version](https://docs.astral.sh/uv/guides/projects/\#viewing-your-version)

The `uv version` command can be used to read your package's version.

To get the version of your package, run `uv version`:

```
$ uv version
hello-world 0.7.0
```

To get the version without the package name, use the `--short` option:

```
$ uv version --short
0.7.0
```

To get version information in a JSON format, use the `--output-format json` option:

```
$ uv version --output-format json
{
    "package_name": "hello-world",
    "version": "0.7.0",
    "commit_info": null
}
```

See the [publishing guide](https://docs.astral.sh/uv/guides/package/#updating-your-version) for details on updating your package
version.

## [Running commands](https://docs.astral.sh/uv/guides/projects/\#running-commands)

`uv run` can be used to run arbitrary scripts or commands in your project environment.

Prior to every `uv run` invocation, uv will verify that the lockfile is up-to-date with the
`pyproject.toml`, and that the environment is up-to-date with the lockfile, keeping your project
in-sync without the need for manual intervention. `uv run` guarantees that your command is run in an
environment with all required dependencies at their locked versions.

Note

`uv run` does not remove extraneous packages (those not in the lockfile) from the environment
by default. See [handling of extraneous packages](https://docs.astral.sh/uv/concepts/projects/sync/#handling-of-extraneous-packages)
for details.

For example, to use `flask`:

```
$ uv add flask
$ uv run -- flask run -p 3000
```

Or, to run a script:

example.py

```
# Require a project dependency
import flask

print("hello world")
```

```
$ uv run example.py
```

Alternatively, you can use `uv sync` to manually update the environment then activate it before
executing a command:

[macOS and Linux](https://docs.astral.sh/uv/guides/projects/#__tabbed_1_1)[Windows](https://docs.astral.sh/uv/guides/projects/#__tabbed_1_2)

```
$ uv sync
$ source .venv/bin/activate
$ flask run -p 3000
$ python example.py
```

```
PS> uv sync
PS> .venv\Scripts\activate
PS> flask run -p 3000
PS> python example.py
```

Note

The virtual environment must be active to run scripts and commands in the project without `uv run`. Virtual environment activation differs per shell and platform.

See the documentation on [running commands and scripts](https://docs.astral.sh/uv/concepts/projects/run/) in projects for
more details.

## [Building distributions](https://docs.astral.sh/uv/guides/projects/\#building-distributions)

`uv build` can be used to build source distributions and binary distributions (wheel) for your
project.

By default, `uv build` will build the project in the current directory, and place the built
artifacts in a `dist/` subdirectory:

```
$ uv build
$ ls dist/
hello_world-0.1.0-py3-none-any.whl
hello_world-0.1.0.tar.gz
```

See the documentation on [building projects](https://docs.astral.sh/uv/concepts/projects/build/) for more details.

## [Next steps](https://docs.astral.sh/uv/guides/projects/\#next-steps)

To learn more about working on projects with uv, see the
[projects concept](https://docs.astral.sh/uv/concepts/projects/) page and the
[command reference](https://docs.astral.sh/uv/reference/cli/#uv).

Or, read on to learn how to
[export a uv lockfile to different formats](https://docs.astral.sh/uv/concepts/projects/export/).

Back to top

---

Source: https://docs.astral.sh/uv/guides/package/

[Skip to content](https://docs.astral.sh/uv/guides/package/#building-and-publishing-a-package)

# [Building and publishing a package](https://docs.astral.sh/uv/guides/package/\#building-and-publishing-a-package)

uv supports building Python packages into source and binary distributions via `uv build` and
uploading them to a registry with `uv publish`.

## [Preparing your project](https://docs.astral.sh/uv/guides/package/\#preparing-your-project)

Before attempting to publish your project, you'll want to make sure it's ready to be packaged for
distribution.

If your project does not include a `[build-system]` definition in the `pyproject.toml`, uv will not
build it during `uv sync` operations in the project, but will fall back to the legacy setuptools
build system during `uv build`.

Note

Projects created with `uv init` include a `[build-system]` definition by default.

We strongly recommend configuring a build system. Read more about build systems in the
[project configuration](https://docs.astral.sh/uv/concepts/projects/config/#build-systems) documentation.

## [Building your package](https://docs.astral.sh/uv/guides/package/\#building-your-package)

Build your package with `uv build`:

```
$ uv build
```

By default, `uv build` will build the project in the current directory, and place the built
artifacts in a `dist/` subdirectory.

Alternatively, `uv build <SRC>` will build the package in the specified directory, while
`uv build --package <PACKAGE>` will build the specified package within the current workspace.

Info

By default, `uv build` respects `tool.uv.sources` when resolving build dependencies from the
`build-system.requires` section of the `pyproject.toml`. When publishing a package, we recommend
running `uv build --no-sources` to ensure that the package builds correctly when `tool.uv.sources`
is disabled, as is the case when using other build tools, like [`pypa/build`](https://github.com/pypa/build).

## [Updating your version](https://docs.astral.sh/uv/guides/package/\#updating-your-version)

The `uv version` command provides conveniences for updating the version of your package before you
publish it.
[See the project docs for reading your package's version](https://docs.astral.sh/uv/guides/projects/#viewing-your-version).

To update to an exact version, provide it as a positional argument:

```
$ uv version 1.0.0
hello-world 0.7.0 => 1.0.0
```

To preview the change without updating the `pyproject.toml`, use the `--dry-run` flag:

```
$ uv version 2.0.0 --dry-run
hello-world 1.0.0 => 2.0.0
$ uv version
hello-world 1.0.0
```

To increment a component of your package version, use the `--bump` option:

```
$ uv version --bump minor
hello-world 1.2.3 => 1.3.0
```

The `--bump` option supports the following common version components: `major`, `minor`, `patch`,
`stable`, `alpha`, `beta`, `rc`, `post`, and `dev`. When provided more than once, the components
will be applied in order, from largest (`major`) to smallest (`dev`).

You can optionally provide a numeric value with `--bump <component>=<value>` to set the resulting
component explicitly:

```
$ uv version --bump patch --bump dev=66463664
hello-world 0.0.1 => 0.0.2.dev66463664
```

To move from a stable to pre-release version, bump one of the major, minor, or patch components in
addition to the pre-release component:

```
$ uv version --bump patch --bump beta
hello-world 1.3.0 => 1.3.1b1
$ uv version --bump major --bump alpha
hello-world 1.3.0 => 2.0.0a1
```

When moving from a pre-release to a new pre-release version, just bump the relevant pre-release
component:

```
$ uv version --bump beta
hello-world 1.3.0b1 => 1.3.0b2
```

When moving from a pre-release to a stable version, the `stable` option can be used to clear the
pre-release component:

```
$ uv version --bump stable
hello-world 1.3.1b2 => 1.3.1
```

Info

By default, when `uv version` modifies the project it will perform a lock and sync. To
prevent locking and syncing, use `--frozen`. To prevent only syncing, use `--no-sync`.

## [Publishing your package](https://docs.astral.sh/uv/guides/package/\#publishing-your-package)

Note

A complete guide to publishing from GitHub Actions to PyPI can be found in the
[GitHub Guide](https://docs.astral.sh/uv/guides/integration/github/#publishing-to-pypi)

Publish your package with `uv publish`:

```
$ uv publish
```

Set a PyPI token with `--token` or `UV_PUBLISH_TOKEN`, or set a username with `--username` or
`UV_PUBLISH_USERNAME` and password with `--password` or `UV_PUBLISH_PASSWORD`. For publishing to
PyPI from GitHub Actions or another Trusted Publisher, you don't need to set any credentials.
Instead,
[add a trusted publisher to the PyPI project](https://docs.pypi.org/trusted-publishers/adding-a-publisher/).

When using trusted publishing, uv will attempt to invalidate the short-lived PyPI token after
publishing, even if publishing fails. This further reduces the exposure period for the short-lived
token, beyond its already short lifetime.

If invalidation fails, uv emits a warning without changing the publishing result. Tokens provided
explicitly with `--token` or `UV_PUBLISH_TOKEN` are not revoked.

Note

PyPI does not support publishing with username and password anymore, instead you need to
generate a token. Using a token is equivalent to setting `--username __token__` and using the
token as password.

If you're using a custom index through `[[tool.uv.index]]`, add `publish-url` and use
`uv publish --index <name>`. For example:

```
[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
publish-url = "https://test.pypi.org/legacy/"
explicit = true
```

Note

When using `uv publish --index <name>`, the `pyproject.toml` must be present, i.e., you need to
have a checkout step in a publish CI job.

Even though `uv publish` retries failed uploads, it can happen that publishing fails in the middle,
with some files uploaded and some files still missing. With PyPI, you can retry the exact same
command; existing identical files will be ignored. With other registries, use
`--check-url <index url>` with the index URL (not the publishing URL) the packages belong to. When
using `--index`, the index URL is used as check URL. uv will skip uploading files that are identical
to files in the registry, and it will also handle raced parallel uploads. Note that existing files
need to match exactly with those previously uploaded to the registry. This avoids accidentally
publishing source distribution and wheels with different contents for the same version.

### [Uploading attestations with your package](https://docs.astral.sh/uv/guides/package/\#uploading-attestations-with-your-package)

Note

Some third-party package indexes may not support attestations, and may
reject uploads that include them (rather than silently ignoring them).
If you encounter issues when uploading, you can use `--no-attestations` or
`UV_PUBLISH_NO_ATTESTATIONS` to disable uv's default behavior.

Tip

`uv publish` does not currently generate attestations; attestations must
be created separately before publishing.

`uv publish` supports uploading [attestations](https://peps.python.org/pep-0740/) to registries that
support them, like PyPI.

uv will automatically discover and match attestations. For example, given the following `dist/`
directory, `uv publish` will upload the attestations along with their corresponding distributions:

```
$ ls dist/
hello_world-1.0.0-py3-none-any.whl
hello_world-1.0.0-py3-none-any.whl.publish.attestation
hello_world-1.0.0.tar.gz
hello_world-1.0.0.tar.gz.publish.attestation
```

## [Installing your package](https://docs.astral.sh/uv/guides/package/\#installing-your-package)

Test that the package can be installed and imported with `uv run`:

```
$ uv run --with <PACKAGE> --no-project -- python -c "import <PACKAGE>"
```

The `--no-project` flag is used to avoid installing the package from your local project directory.

Tip

If you have recently installed the package, you may need to include the
`--refresh-package <PACKAGE>` option to avoid using a cached version of the package.

## [Next steps](https://docs.astral.sh/uv/guides/package/\#next-steps)

To learn more about publishing packages, check out the
[PyPA guides](https://packaging.python.org/en/latest/guides/section-build-and-publish/) on building
and publishing.

Or, read on for [guides](https://docs.astral.sh/uv/guides/integration/) on integrating uv with other software.

Back to top

---

Source: https://docs.astral.sh/uv/guides/migration/

[Skip to content](https://docs.astral.sh/uv/guides/migration/#migration-guides)

# [Migration guides](https://docs.astral.sh/uv/guides/migration/\#migration-guides)

Learn how to migrate from other tools to uv:

- [Migrate from pip to uv projects](https://docs.astral.sh/uv/guides/migration/pip-to-project/)

Note

Other guides, such as migrating from another project management tool, or from pip to `uv pip`
are not yet available. See [#5200](https://github.com/astral-sh/uv/issues/5200) to track
progress.

Or, explore the [integration guides](https://docs.astral.sh/uv/guides/integration/) to learn how to use uv with other
software.

Back to top

---

Source: https://docs.astral.sh/uv/guides/migration/pip-to-project/

[Skip to content](https://docs.astral.sh/uv/guides/migration/pip-to-project/#migrating-from-pip-to-a-uv-project)

# [Migrating from pip to a uv project](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#migrating-from-pip-to-a-uv-project)

This guide will discuss converting from a `pip` and `pip-tools` workflow centered on `requirements`
files to uv's project workflow using a `pyproject.toml` and `uv.lock` file.

Note

If you're looking to migrate from `pip` and `pip-tools` to uv's drop-in interface or from an
existing workflow where you're already using a `pyproject.toml`, those guides are not yet
written. See [#5200](https://github.com/astral-sh/uv/issues/5200) to track progress.

We'll start with an overview of developing with `pip`, then discuss migrating to uv.

Tip

If you're familiar with the ecosystem, you can jump ahead to the
[requirements file import](https://docs.astral.sh/uv/guides/migration/pip-to-project/#importing-requirements-files) instructions.

## [Understanding pip workflows](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#understanding-pip-workflows)

### [Project dependencies](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#project-dependencies)

When you want to use a package in your project, you need to install it first. `pip` supports
imperative installation of packages, e.g.:

```
$ pip install fastapi
```

This installs the package into the environment that `pip` is installed in. This may be a virtual
environment, or, the global environment of your system's Python installation.

Then, you can run a Python script that requires the package:

example.py

```
import fastapi
```

It's best practice to create a virtual environment for each project, to avoid mixing packages
between them. For example:

```
$ python -m venv
$ source .venv/bin/activate
$ pip ...
```

We will revisit this topic in the [project environments section](https://docs.astral.sh/uv/guides/migration/pip-to-project/#project-environments) below.

### [Requirements files](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#requirements-files)

When sharing projects with others, it's useful to declare all the packages you require upfront.
`pip` supports installing requirements from a file, e.g.:

requirements.txt

```
fastapi
```

```
$ pip install -r requirements.txt
```

Notice above that `fastapi` is not "locked" to a specific version — each person working on the
project may have a different version of `fastapi` installed. `pip-tools` was created to improve this
experience.

When using `pip-tools`, requirements files specify both the dependencies for your project and lock
dependencies to a specific version — the file extension is used to differentiate between the two.
For example, if you require `fastapi` and `pydantic`, you'd specify these in a `requirements.in`
file:

requirements.in

```
fastapi
pydantic>2
```

Notice there's a version constraint on `pydantic` — this means only `pydantic` versions later than
`2.0.0` can be used. In contrast, `fastapi` does not have a version constraint — any version can be
used.

These dependencies can be compiled into a `requirements.txt` file:

```
$ pip-compile requirements.in -o requirements.txt
```

requirements.txt

```
annotated-types==0.7.0
    # via pydantic
anyio==4.8.0
    # via starlette
fastapi==0.115.11
    # via -r requirements.in
idna==3.10
    # via anyio
pydantic==2.10.6
    # via
    #   -r requirements.in
    #   fastapi
pydantic-core==2.27.2
    # via pydantic
sniffio==1.3.1
    # via anyio
starlette==0.46.1
    # via fastapi
typing-extensions==4.12.2
    # via
    #   fastapi
    #   pydantic
    #   pydantic-core
```

Here, all the version constraints are _exact_. Only a single version of each package can be used.
The above example was generated with `uv pip compile`, but could also be generated with
`pip-compile` from `pip-tools`.

Though less common, the `requirements.txt` can also be generated using `pip freeze`, by first
installing the input dependencies into the environment then exporting the installed versions:

```
$ pip install -r requirements.in
$ pip freeze > requirements.txt
```

requirements.txt

```
annotated-types==0.7.0
anyio==4.8.0
fastapi==0.115.11
idna==3.10
pydantic==2.10.6
pydantic-core==2.27.2
sniffio==1.3.1
starlette==0.46.1
typing-extensions==4.12.2
```

After compiling dependencies into a locked set of versions, these files are committed to version
control and distributed with the project.

Then, when someone wants to use the project, they install from the requirements file:

```
$ pip install -r requirements.txt
```

### [Development dependencies](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#development-dependencies)

The requirements file format can only describe a single set of dependencies at once. This means if
you have additional _groups_ of dependencies, such as development dependencies, they need separate
files. For example, we'll create a `-dev` dependency file:

requirements-dev.in

```
-r requirements.in
-c requirements.txt

pytest
```

Notice the base requirements are included with `-r requirements.in`. This ensures your development
environment considers _all_ of the dependencies together. The `-c requirements.txt` _constrains_ the
package version to ensure that the `requirements-dev.txt` uses the same versions as
`requirements.txt`.

Note

It's common to use `-r requirements.txt` directly instead of using both
`-r requirements.in`, and `-c requirements.txt`. There's no difference in the resulting package
versions, but using both files produces annotations which allow you to determine which
dependencies are _direct_ (annotated with `-r requirements.in`) and which are _indirect_ (only
annotated with `-c requirements.txt`).

The compiled development dependencies look like:

requirements-dev.txt

```
annotated-types==0.7.0
    # via
    #   -c requirements.txt
    #   pydantic
anyio==4.8.0
    # via
    #   -c requirements.txt
    #   starlette
fastapi==0.115.11
    # via
    #   -c requirements.txt
    #   -r requirements.in
idna==3.10
    # via
    #   -c requirements.txt
    #   anyio
iniconfig==2.0.0
    # via pytest
packaging==24.2
    # via pytest
pluggy==1.5.0
    # via pytest
pydantic==2.10.6
    # via
    #   -c requirements.txt
    #   -r requirements.in
    #   fastapi
pydantic-core==2.27.2
    # via
    #   -c requirements.txt
    #   pydantic
pytest==8.3.5
    # via -r requirements-dev.in
sniffio==1.3.1
    # via
    #   -c requirements.txt
    #   anyio
starlette==0.46.1
    # via
    #   -c requirements.txt
    #   fastapi
typing-extensions==4.12.2
    # via
    #   -c requirements.txt
    #   fastapi
    #   pydantic
    #   pydantic-core
```

As with the base dependency files, these are committed to version control and distributed with the
project. When someone wants to work on the project, they'll install from the requirements file:

```
$ pip install -r requirements-dev.txt
```

### [Platform-specific dependencies](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#platform-specific-dependencies)

When compiling dependencies with `pip` or `pip-tools`, the result is only usable on the same
platform as it is generated on. This poses a problem for projects which need to be usable on
multiple platforms, such as Windows and macOS.

For example, take a simple dependency:

requirements.in

```
tqdm
```

On Linux, this compiles to:

requirements-linux.txt

```
tqdm==4.67.1
    # via -r requirements.in
```

While on Windows, this compiles to:

requirements-win.txt

```
colorama==0.4.6
    # via tqdm
tqdm==4.67.1
    # via -r requirements.in
```

`colorama` is a Windows-only dependency of `tqdm`.

When using `pip` and `pip-tools`, a project needs to declare a requirements lock file for each
supported platform.

Note

uv's resolver can compile dependencies for multiple platforms at once (see ["universal resolution"](https://docs.astral.sh/uv/concepts/resolution/#universal-resolution)),
allowing you to use a single `requirements.txt` for all platforms:

```
$ uv pip compile --universal requirements.in
```

requirements.txt

```
colorama==0.4.6 ; sys_platform == 'win32'
    # via tqdm
tqdm==4.67.1
    # via -r requirements.in
```

This resolution mode is also used when using a `pyproject.toml` and `uv.lock`.

## [Migrating to a uv project](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#migrating-to-a-uv-project)

### [The `pyproject.toml`](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#the-pyprojecttoml)

The `pyproject.toml` is a standardized file for Python project metadata. It replaces
`requirements.in` files, allowing you to represent arbitrary groups of project dependencies. It also
provides a centralized location for metadata about your project, such as the build system or tool
settings.

For example, the `requirements.in` and `requirements-dev.in` files above can be translated to a
`pyproject.toml` as follows:

pyproject.toml

```
[project]
name = "example"
version = "0.0.1"
dependencies = [\
    "fastapi",\
    "pydantic>2"\
]

[dependency-groups]
dev = ["pytest"]
```

We'll discuss the commands necessary to automate these imports below.

### [The uv lockfile](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#the-uv-lockfile)

uv uses a lockfile (`uv.lock`) to lock package versions. The format of this file is specific to uv,
allowing uv to support advanced features. It replaces `requirements.txt` files.

The lockfile will be automatically created and populated when adding dependencies, but you can
explicitly create it with `uv lock`.

Unlike `requirements.txt` files, the `uv.lock` file can represent arbitrary groups of dependencies,
so multiple files are not needed to lock development dependencies.

The uv lockfile is always [universal](https://docs.astral.sh/uv/concepts/resolution/#universal-resolution), so
multiple files are not needed to
[lock dependencies for each platform](https://docs.astral.sh/uv/guides/migration/pip-to-project/#platform-specific-dependencies). This ensures that all
developers are using consistent, locked versions of dependencies regardless of their machine.

The uv lockfile also supports concepts like
[pinning packages to specific indexes](https://docs.astral.sh/uv/concepts/indexes/#pinning-a-package-to-an-index),
which is not representable in `requirements.txt` files.

Tip

If you only need to lock for a subset of platforms, use the
[`tool.uv.environments`](https://docs.astral.sh/uv/concepts/resolution/#limited-resolution-environments) setting
to limit the resolution and lockfile.

To learn more, see the [lockfile](https://docs.astral.sh/uv/concepts/projects/layout/#the-lockfile) documentation.

### [Importing requirements files](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#importing-requirements-files)

First, create a `pyproject.toml` if you have not already:

```
$ uv init
```

Then, the easiest way to import requirements is with `uv add`:

```
$ uv add -r requirements.in
```

However, there is some nuance to this transition. Notice we used the `requirements.in` file, which
does not pin to exact versions of packages so uv will solve for new versions of these packages. You
may want to continue using your previously locked versions from your `requirements.txt` so, when
switching over to uv, none of your dependency versions change.

The solution is to add your locked versions as _constraints_. uv supports using these on `add` to
preserve locked versions:

```
$ uv add -r requirements.in -c requirements.txt
```

Your existing versions will be retained when producing a `uv.lock` file.

#### [Importing platform-specific constraints](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#importing-platform-specific-constraints)

If your platform-specific dependencies have been compiled into separate files, you can still
transition to a universal lockfile. However, you cannot just use `-c` to specify constraints from
your existing platform-specific `requirements.txt` files because they do not include markers
describing the environment and will consequently conflict.

To add the necessary markers, use `uv pip compile` to convert your existing files. For example,
given the following:

requirements-win.txt

```
colorama==0.4.6
    # via tqdm
tqdm==4.67.1
    # via -r requirements.in
```

The markers can be added with:

```
$ uv pip compile requirements.in -o requirements-win.txt --python-platform windows --no-strip-markers
```

Notice the resulting output includes a Windows marker on `colorama`:

requirements-win.txt

```
colorama==0.4.6 ; sys_platform == 'win32'
    # via tqdm
tqdm==4.67.1
    # via -r requirements.in
```

When using `-o`, uv will constrain the versions to match the existing output file, if it can.

Markers can be added for other platforms by changing the `--python-platform` and `-o` values for
each requirements file you need to import, e.g., to `linux` and `macos`.

Once each `requirements.txt` file has been transformed, the dependencies can be imported to the
`pyproject.toml` and `uv.lock` with `uv add`:

```
$ uv add -r requirements.in -c requirements-win.txt -c requirements-linux.txt
```

#### [Importing development dependency files](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#importing-development-dependency-files)

As discussed in the [development dependencies](https://docs.astral.sh/uv/guides/migration/pip-to-project/#development-dependencies) section, it's common to
have groups of dependencies for development purposes.

To import development dependencies, use the `--dev` flag during `uv add`:

```
$ uv add --dev -r requirements-dev.in -c requirements-dev.txt
```

If the `requirements-dev.in` includes the parent `requirements.in` via `-r`, it will need to be
stripped to avoid adding the base requirements to the `dev` dependency group. The following example
uses `sed` to strip lines that start with `-r`, then pipes the result to `uv add`:

```
$ sed '/^-r /d' requirements-dev.in | uv add --dev -r - -c requirements-dev.txt
```

In addition to the `dev` dependency group, uv supports arbitrary group names. For example, if you
also have a dedicated set of dependencies for building your documentation, those can be imported to
a `docs` group:

```
$ uv add -r requirements-docs.in -c requirements-docs.txt --group docs
```

#### [Importing dependency sources](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#importing-dependency-sources)

When importing requirements on local paths or Git repositories, for example:

requirements.in

```
./path-dep
-e ./editable-path-dep
git-dep @ git+https://github.com/astral-sh/git-dep
```

uv will map them to [dependency sources](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-sources)
in the `[tool.uv.sources]` table of the `pyproject.toml`:

pyproject.toml

```
[project]
dependencies = [\
    "path-dep",\
    "editable-path-dep",\
    "git-dep",\
]

[tool.uv.sources]
path-dep = { path = "./path-dep" }
editable-path-dep = { path = "./editable-path-dep", editable = true }
git-dep = { git = "https://github.com/astral-sh/git-dep" }
```

### [Project environments](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#project-environments)

Unlike `pip`, uv is not centered around the concept of an "active" virtual environment. Instead, uv
uses a dedicated virtual environment for each project in a `.venv` directory. This environment is
automatically managed, so when you run a command, like `uv add`, the environment is synced with the
project dependencies.

The preferred way to execute commands in the environment is with `uv run`, e.g.:

```
$ uv run pytest
```

Prior to every `uv run` invocation, uv will verify that the lockfile is up-to-date with the
`pyproject.toml`, and that the environment is up-to-date with the lockfile, keeping your project
in-sync without the need for manual intervention. `uv run` guarantees that your command is run in a
consistent, locked environment.

The project environment can also be explicitly created with `uv sync`, e.g., for use with editors.

Note

When in projects, uv will prefer a `.venv` in the project directory and ignore the active
environment as declared by the `VIRTUAL_ENV` variable by default. You can opt-in to using the
active environment with the `--active` flag.

To learn more, see the
[project environment](https://docs.astral.sh/uv/concepts/projects/layout/#the-project-environment) documentation.

## [Next steps](https://docs.astral.sh/uv/guides/migration/pip-to-project/\#next-steps)

Now that you've migrated to uv, take a look at the
[project concept](https://docs.astral.sh/uv/concepts/projects/) page for more details about uv projects.

Back to top

---

Source: https://docs.astral.sh/uv/guides/integration/

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