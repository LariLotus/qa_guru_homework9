from imghdr import tests


def path(file_name):
    return str(
       (Path(tests.__file__).joinpath(f'resources/{file_name}').absolute()
    ))
    pass
