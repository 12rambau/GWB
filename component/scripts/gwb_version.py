import subprocess
import re


def get_gwb_version():
    """Get the version of GWB installed on the system and write it to CHANGELOG.md."""

    try:
        # Run the command and capture output
        result = subprocess.run(["GWB"], capture_output=True, text=True)
        output = result.stdout.splitlines()

        # Find and capture the version number
        version = None
        for line in output:
            match = re.search(r"Installed version: (\d+\.\d+\.\d+)", line)
            if match:
                version = match.group(1)
                break

    except Exception as e:
        version = "There is no GWB installation on this system."
        print(e)

    return version or "There is no GWB installation on this system."


if __name__ == "__main__":
    get_gwb_version()
