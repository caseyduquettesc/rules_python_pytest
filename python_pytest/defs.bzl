"""Public API"""

load("@rules_python//python:defs.bzl", "py_test")
load("@pytest_requirements//:requirements.bzl", "requirement")

def py_pytest_test(name, srcs, deps = [], args = [], **kwargs):
    """Use pytest to run tests, using a wrapper script to interface with Bazel.

    ```py
    py_pytest_test(
      name = "test_w_pytest",
      size = "small",
      srcs = ["test.py"],
      deps = [
      ],
    )
    ```
    """
    shim_label = Label("//python_pytest:pytest_shim.py")

    py_test(
        name = name,
        srcs = [
            shim_label,
        ] + srcs,
        main = shim_label,
        args = [
            "--capture=no",
        ] + args + ["$(location :%s)" % x for x in srcs],
        # python_version = "PY3",
        # srcs_version = "PY3",
        deps = deps + [
             requirement("pytest"),
             requirement("pluggy"),
        ],
        **kwargs
    )
