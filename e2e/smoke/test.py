import platform
import sys
import subprocess


def cmd(args):
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    out, _ = process.communicate()
    return out.decode("ascii").strip()


class TestPythonVersion:
    def test_version(self):
        bazel_python_path = f"Python executable used by Bazel is: {sys.executable} \n\n"
        bazel_python_version = (
            f"Python version used by Bazel is: {platform.python_version()} \n\n"
        )
        host_python_path = f'Python executable on the HOST machine is: {cmd(["which", "python3"])} \n\n'
        host_python_version = f'Python version on the HOST machine is: {cmd(["python3", "-c", "import platform; print(platform.python_version())"])}'
        python_string = (
            bazel_python_path
            + bazel_python_version
            + host_python_path
            + host_python_version
        )
        print(python_string)

        assert platform.python_version().startswith("3.9")
