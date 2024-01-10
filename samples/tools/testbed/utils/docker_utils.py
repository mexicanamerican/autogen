from os import os
from time import time

import docker
from autogen.code_utils import pathlib


def pull_image(image_name):
    client = docker.from_env()
    image = client.images.pull(image_name)

def run_container(image_name, command, working_dir, volumes, timeout=600):
    client = docker.from_env()
    abs_path = str(pathlib.Path(working_dir).absolute())
    container = client.containers.run(
        image_name,
        command=command,
        working_dir=working_dir,
        detach=True,
        volumes={abs_path: {"bind": working_dir, "mode": "rw"}},
    )
    start_time = time.time()
    while container.status != "exited" and time.time() - start_time < timeout:
        container.reload()
    if container.status != "exited":
        container.stop()
        logs = container.logs().decode("utf-8").rstrip() + "\nDocker timed out."
        with open(os.path.join(working_dir, "console_log.txt"), "wt") as f:
            f.write(logs)
        container.remove()
        return
    logs = container.logs().decode("utf-8").rstrip()
    container.remove()
    return logs

def stop_container(container):
    container.stop()

def remove_container(container):
    container.remove()

def get_container_logs(container):
    logs = container.logs().decode("utf-8").rstrip()
    return logs

def get_container_status(container):
    return container.status
