import os
import shutil


def main():
    dir_path: str = "./"
    file_names: list[dir_path] = os.listdir(dir_path)

    prefix: str = "bash_"
    new_prefix: str = "linux_cmd_"

    file_names = list(filter(
        lambda path: path.startswith(prefix),
        file_names
    ))

    new_file_names = list(map(
        lambda name: new_prefix + name[len(prefix):],
        file_names
    ))

    for pair in zip(file_names, new_file_names):
        shutil.move(*pair)


if "__main__" == __name__:
    main()
