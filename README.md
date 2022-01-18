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
copy the WORKSPACE snippet into your `WORKSPACE` file.
