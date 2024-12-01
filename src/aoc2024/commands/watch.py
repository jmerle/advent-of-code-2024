import subprocess
import sys
from pathlib import Path
from typing import TextIO

import click
import watchfiles

from aoc2024.commands.common import PROJECT_ROOT


@click.command()
@click.argument("data_type", type=click.Choice(["example", "full"], case_sensitive=False))
def watch(data_type: str) -> None:
    """Automatically runs part1.py and part2.py on save."""
    print(f"Starting watcher for {data_type}")

    process: subprocess.Popen | None = None
    process_code_file: Path | None = None
    process_data_file_fd: TextIO | None = None

    try:
        for changes in watchfiles.watch(PROJECT_ROOT):
            for change, changed_file in changes:
                if change != watchfiles.Change.modified:
                    continue

                changed_file = Path(changed_file)
                if not changed_file.is_file():
                    continue

                if changed_file.name in ["part1.py", "part2.py"]:
                    code_file = changed_file
                elif changed_file.stem == data_type and process_code_file is not None:
                    code_file = process_code_file
                else:
                    continue

                data_file = code_file.parent / f"{data_type}.txt"

                print(f"\nRunning {code_file.relative_to(PROJECT_ROOT)} on {data_file.relative_to(PROJECT_ROOT)}")

                if process is not None and process.poll() is None:
                    print("Killing current process")
                    process.kill()
                    process_data_file_fd.close()

                if len(data_file.read_text(encoding="utf-8")) == 0:
                    print(f"{data_file.relative_to(PROJECT_ROOT)} is empty!")

                data_file_fd = data_file.open("r")
                print()

                process = subprocess.Popen([sys.executable, str(code_file)], cwd=PROJECT_ROOT, stdin=data_file_fd)
                process_code_file = code_file
                process_data_file_fd = data_file_fd
    except KeyboardInterrupt:
        if process is not None and process.poll() is None:
            print("Killing current process")
            process.kill()
            process_data_file_fd.close()

        sys.exit(1)
