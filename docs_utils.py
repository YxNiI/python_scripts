import os
from pprint import pprint

def write_internals_into_file(object: object, file_name: str) -> None:
    script_directory: str = os.path.dirname(os.path.realpath(__file__))
    full_path: str = os.path.join(script_directory, file_name)

    if not os.path.exists(full_path):
        os.mknod(full_path)

    with open(full_path, 'w') as file:
        for line in dir(object):
            pprint(line, stream=file)
