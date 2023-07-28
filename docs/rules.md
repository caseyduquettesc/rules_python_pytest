<!-- Generated with Stardoc: http://skydoc.bazel.build -->

Public API

<a id="py_pytest_test"></a>

## py_pytest_test

<pre>
py_pytest_test(<a href="#py_pytest_test-name">name</a>, <a href="#py_pytest_test-srcs">srcs</a>, <a href="#py_pytest_test-deps">deps</a>, <a href="#py_pytest_test-args">args</a>, <a href="#py_pytest_test-kwargs">kwargs</a>)
</pre>

Use pytest to run tests, using a wrapper script to interface with Bazel.

```py
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

**PARAMETERS**


| Name  | Description | Default Value |
| :------------- | :------------- | :------------- |
| <a id="py_pytest_test-name"></a>name |  <p align="center"> - </p>   |  none |
| <a id="py_pytest_test-srcs"></a>srcs |  <p align="center"> - </p>   |  none |
| <a id="py_pytest_test-deps"></a>deps |  <p align="center"> - </p>   |  <code>[]</code> |
| <a id="py_pytest_test-args"></a>args |  <p align="center"> - </p>   |  <code>[]</code> |
| <a id="py_pytest_test-kwargs"></a>kwargs |  <p align="center"> - </p>   |  none |


