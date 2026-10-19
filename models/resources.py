from pathlib import Path

import tests


def resource_path (file_name):
    str(Path(tests._file_).parent.joinpath(f'resources/{file_name}').absolute())