import logging


def get_contents(path):
    logging.info(f"Received path: {path}")

    with open(path, "r") as context:
        for line in context:
            yield line
