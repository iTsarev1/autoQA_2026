from pathlib import Path

import tests


def path (file_name):
    return str(Path(tests._file_).parent.joinpath(f'resources/{file_name}').absolute())