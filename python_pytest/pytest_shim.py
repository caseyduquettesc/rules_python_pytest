"""A shim for executing pytest that supports test filtering."""

import sys
import os

import pytest


if __name__ == "__main__":
    pytest_args = ["--ignore=external"]

    # pytest runs tests twice if __init__.py is passed explicitly as an argument. Remove any __init__.py file to avoid that.
    # https://github.com/pytest-dev/pytest/issues/9313
    args = [arg for arg in sys.argv[1:] if arg.startswith("-") or os.path.basename(arg) != "__init__.py"]

    if os.environ.get("XML_OUTPUT_FILE"):
        pytest_args.append("--junitxml={xml_output_file}".format(xml_output_file=os.environ.get("XML_OUTPUT_FILE")))

    if os.environ.get("TESTBRIDGE_TEST_ONLY"):
        # TestClass.test_fn -> TestClass::test_fn
        module_name = os.environ.get("TESTBRIDGE_TEST_ONLY").replace(".", "::")

        # If the test filter does not start with a class-like name, then use test filtering instead
        # --test_filter=test_fn
        if not module_name[0].isupper():
            pytest_args.extend(args)
            pytest_args.append("-k={filter}".format(filter=module_name))
        else:
            # --test_filter=TestClass.test_fn
            # Add test filter to path-like args
            for arg in args:
                if not arg.startswith("--"):
                    # Maybe a src file? Add test class/method selection to it. Not sure if this will work if the
                    # symbol can't be found in the test file.
                    arg = "{arg}::{module_fn}".format(arg=arg, module_fn=module_name)
                pytest_args.append(arg)
    else:
        pytest_args.extend(args)

    print(pytest_args, file=sys.stderr)
    raise SystemExit(pytest.main(pytest_args))
