import os


def load_config(path):
    # TODO: validate path exists
    return os.path.join(path, "config.yml")


def run(server):
    server.start()


def shutdown():
    print("bye")
