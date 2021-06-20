from os import PathLike
from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    if not path:
        return path
    # ./ ignore
    # ../ remove current folder
    if path[0] == "/":
        path = path[1:]
        root = "/"
    else:
        root = ""

    path_stack = []
    for _path in path.split("/"):
        if _path == "." or _path == "":
            pass
        elif _path == ".." and path_stack and path_stack[-1] != "..":
            path_stack.pop()
        else:
            path_stack.append(_path)
        
    return root + "/".join(path_stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
