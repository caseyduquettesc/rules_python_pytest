<!-- Generated with Stardoc: http://skydoc.bazel.build -->

Use pytest to run tests, using a wrapper script to interface with Bazel.

Example:

```starlark
load("@caseyduquettesc_rules_python_pytest//python_pytest:defs.bzl", "py_pytest_test")

py_pytest_test(
    name = "test_w_pytest",
    size = "small",
    srcs = ["test.py"],
)
```

By default, `@pip//pytest` is added to `deps`.
If sharding is used (when `shard_count &gt; 1`) then `@pip//pytest_shard` is also added.
To instead provide explicit deps for the pytest library, set `pytest_deps`:

```starlark
py_pytest_test(
    name = "test_w_my_pytest",
    shard_count = 2,
    srcs = ["test.py"],
    pytest_deps = [requirement("pytest"), requirement("pytest-shard"), ...],
)
```


<a id="py_pytest_test"></a>

## py_pytest_test

<pre>
py_pytest_test(<a href="#py_pytest_test-name">name</a>, <a href="#py_pytest_test-srcs">srcs</a>, <a href="#py_pytest_test-deps">deps</a>, <a href="#py_pytest_test-args">args</a>, <a href="#py_pytest_test-pytest_deps">pytest_deps</a>, <a href="#py_pytest_test-pip_repo">pip_repo</a>, <a href="#py_pytest_test-kwargs">kwargs</a>)
</pre>

    Wrapper macro for `py_test` which supports pytest.

**PARAMETERS**


| Name  | Description | Default Value |
| :------------- | :------------- | :------------- |
| <a id="py_pytest_test-name"></a>name |  A unique name for this target.   |  none |
| <a id="py_pytest_test-srcs"></a>srcs |  Python source files.   |  none |
| <a id="py_pytest_test-deps"></a>deps |  Dependencies, typically <code>py_library</code>.   |  <code>[]</code> |
| <a id="py_pytest_test-args"></a>args |  Additional command-line arguments to pytest. See https://docs.pytest.org/en/latest/how-to/usage.html   |  <code>[]</code> |
| <a id="py_pytest_test-pytest_deps"></a>pytest_deps |  Labels of the pytest tool and other packages it may import.   |  <code>None</code> |
| <a id="py_pytest_test-pip_repo"></a>pip_repo |  Name of the external repository where Python packages are installed. It's typically created by <code>pip.parse</code>. This attribute is used only when <code>pytest_deps</code> is unset.   |  <code>"pip"</code> |
| <a id="py_pytest_test-kwargs"></a>kwargs |  Additional named parameters to py_test.   |  none |


