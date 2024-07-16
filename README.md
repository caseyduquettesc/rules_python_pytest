# Bazel rules for python_pytest

Bazel rules to run your Python unit tests with [pytest](https://docs.pytest.org/en/6.2.x/index.html).

`pytest` support in [rules_python](https://github.com/bazelbuild/rules_python) is not provided out of the box,
see https://github.com/bazelbuild/rules_python/issues/240 and https://github.com/bazelbuild/rules_python/pull/464.
Progress on the feature request seems to have stagnated so I've gone ahead and put at least something in
the public domain until `rules_python` offers it.

Features:

- Run unit tests with `pytest`
- Supports test filtering with Bazel's `--test_filter=` option

## Installation

From the release you wish to use:
<https://github.com/caseyduquettesc/rules_python_pytest/releases>
copy the WORKSPACE snippet into your `WORKSPACE` file or the `bazel_dep` if you use bzlmod.

#################################################

# loadup the requirements for pytest
load("@rules_python_pytest//python_pytest:repositories.bzl", "setup_pytest_requirements")
# this requires you to pass in your python interpreter
setup_pytest_requirements(interpreter = interpreter)
load("@pytest_requirements//:requirements.bzl", "install_deps")
install_deps()

#################################################


## Usage

```py
load("@rules_python_pytest//python_pytest:defs.bzl", "py_pytest_test")

py_pytest_test(
    name = "test_w_pytest",
    size = "small",
    srcs = ["test.py"],
    deps = [
      # TODO Add this for the user
      requirement("pytest"),
    ],
)
```

To use [test sharding](https://bazel.build/reference/test-encyclopedia#test-sharding), also add `requirement("pytest-shard")`
to `deps`.

## Disclaimer

I rely on this myself and will accept issue reports and contributions, however this only has a simple smoke test and isn't
documented terribly well. I will maintain this, however the expectation is that this will eventually be rolled into
`rules_python` and at that point these rules will be deprecated.
