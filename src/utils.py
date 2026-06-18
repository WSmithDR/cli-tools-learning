import os


def ensure_dir(p):
    # TODO: handle permissions error
    os.makedirs(p, exist_ok=True)
