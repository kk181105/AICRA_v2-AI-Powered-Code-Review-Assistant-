import subprocess
import tempfile


def run_python_code(code):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
        f.write(code.encode())
        filename = f.name

    result = subprocess.run(
        ["python", filename],
        capture_output=True,
        text=True
    )

    return result.stdout + result.stderr