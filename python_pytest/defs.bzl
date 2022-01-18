"""Public API"""

load("@rules_python//python:defs.bzl", "py_test")
# load("@py_deps//:requirements.bzl", "requirement")

def py_pytest_test(name, srcs, deps = [], args = [], **kwargs):
    """Use pytest to run tests, using a wrapper script to interface with Bazel.

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
        # TODO It'd be nice to implicitly include pytest, but I don't know how to know the requirements repo nme
        # deps = deps + [
        #     requirement("pytest"),
        # ],
        deps = deps,
        **kwargs
    )
